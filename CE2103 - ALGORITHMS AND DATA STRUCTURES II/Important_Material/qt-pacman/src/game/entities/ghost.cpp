#include "ghost.h"

Ghost::Ghost(Compass *compass_ipt): compass(compass_ipt) {
    setOffset(QPoint(-8, -8));
    tmpDir = QPoint(-1, -1);
    direction = QPointF(0, 0);

    connect(compass, SIGNAL(powerUp()), this, SLOT(nerfInterval()));

    switchTimer = new QTimer();
    connect(switchTimer, SIGNAL(timeout()), this, SLOT(switchAnimate()));
    switchTimer->start(80);

    chaseTimer = new QTimer();
    connect(chaseTimer, SIGNAL(timeout()), this, SLOT(changeMode()));
    chaseTimer->start(20000);

    nerfTimer = new QTimer();
    connect(nerfTimer, SIGNAL(timeout()), this, SLOT(timeLeft()));

    shine = new QTimer();
    connect(shine, SIGNAL(timeout()), this, SLOT(shining()));

    step_size = 1;

    // load the nerf picture
    for (int i = 0; i < 2; i ++) {
        for (int j = 0; j < 2; j ++) {
            fright[i][j].load(":/img/ghost/nerf/nerf" + QString::number(i) + QString::number(j + 1) +".png");
            fright[i][j] = fright[i][j].scaledToHeight(32);
        }
    }

    // load the dead ghost picture
    QString dire = "udlr";
    for (int i = 0; i < 4; i ++) {
        dead[i].load(":/img/ghost/dead/" + dire[i] +".png");
        dead[i] = dead[i].scaledToWidth(32);
    }

    index_i = 1;
    index_j = 0;

    nerf = false;
    home = false;
    remainNerf = 0;
}

void Ghost::move() {
    // check for the pos
    check();

    if (mode == Mode::Home) {
        setPos(pos() + direction * step_size);
        if (((y() <= 249) && home) || y() >= 269){
            direction = -direction;
        }
        return;
    }
    if ((x() < 0 || x() >= 448)) {
        setPos(pos() + direction * step_size);
        if (x() < -32){
            setX(448);
        } else if (x() > 480) {
            setX(-32);
        }
    }
    else if (int(y() - 35) % 16 == 0 && int(x()) % 16 == 0) {
        chase();
        compass->setLoc(QPoint(int(y() - 35) / 16, int(x()) / 16), kind);
        if (tmpDir != QPoint(-1, -1)) {
            if (compass->canMove(pos(), tmpDir)) {
                direction = tmpDir;
                tmpDir = QPoint(-1, -1);
            }
        }
        if (compass->canMove(pos(), direction)) {
            setPos(pos() + direction * step_size);
        }
        else {
            qDebug() << "stuck";
            QPoint arrow[4] = {Dir::Up, Dir::Down, Dir::Left, Dir::Right};
            for (int i = 0; i < 4; i ++) {
                if (compass->canMove(pos(), arrow[i])) {
                    qDebug() << "escape" << tmpDir;
                    direction = arrow[i];
                    break;
                }
            }
            chase();
        }
    }
    else {
        setPos(pos() + direction * step_size);
    }
}

void Ghost::setDirection(QPoint dir) {
    tmpDir = dir;
}

qreal Ghost::distance(QPoint a, QPoint b) {
    QPoint vector = b - a;
    return sqrt(pow(vector.x(), 2) + pow(vector.y(), 2));
}

void Ghost::loadPicture(QString filepath) {
    QString dire = "udlr";
    for (int i = 0; i < 4; i ++) {
        for (int j = 0; j < 2; j ++) {
            pic[i][j].load(filepath + dire[i] + QString::number(j + 1) + ".png");
            pic[i][j] = pic[i][j].scaledToHeight(32);
        }
    }
    setPixmap(pic[0][0]);
}

void Ghost::switchAnimate() {
    if (mode != Mode::Frighten) {
        if (direction == Dir::Up)
            index_i = 0;
        else if (direction == Dir::Down)
            index_i = 1;
        else if (direction == Dir::Left)
            index_i = 2;
        else
            index_i = 3;

        if (mode == Mode::Dead)
            setPixmap(dead[index_i]);
        else
            setPixmap(pic[index_i][index_j]);
    }
    else
        setPixmap(fright[index_i][index_j]);

    index_j ++;
    if (index_j >= 2)
        index_j = 0;
}

void Ghost::chase() {
    if (tmpDir != QPoint(-1, -1))
        return;
    int i = int(y() - 35) / 16;
    int j = int(x()) / 16;
    QPoint choice = QPoint(-1, -1);

    if (mode == Mode::Chase)
        target = setTarget();
    else if (mode == Mode::Scatter)
        target = critical;
    else if (mode == Mode::Frighten)
        target = compass->getPlayerLoc();
    else if (mode == Mode::Dead)
        target = QPoint(12, 14);

    if (compass->canMove(pos(), direction)) {
        QPoint arrow[4] = {Dir::Up, Dir::Down, Dir::Left, Dir::Right};
        qreal length;

        if (mode == Mode::Chase || mode == Mode::Scatter || mode == Mode::Dead)
            length = 9999999;
        else
            length = -1;

        // test for moving
        for (int a = 0; a < 4; a ++) {
            if (arrow[a] + direction == QPoint(0, 0))
                continue;

            if (mode == Mode::Chase || mode == Mode::Scatter || mode == Mode::Dead) {
                if (compass->canMove(pos() + direction * 16, arrow[a])) {
                    if (distance(target, QPoint(i + direction.y() + arrow[a].y(), j + direction.x() + arrow[a].x())) < length) {
                        length = distance(target, QPoint(i + direction.y() + arrow[a].y(), j + direction.x() + arrow[a].x()));
                        choice = arrow[a];
                    }
                }
            }
            else if (mode == Mode::Frighten) {
                if (compass->canMove(pos() + direction * 16, arrow[a])) {
                    if (distance(target, QPoint(i + direction.y() + arrow[a].y(), j + direction.x() + arrow[a].x())) > length) {
                        length = distance(target, QPoint(i + direction.y() + arrow[a].y(), j + direction.x() + arrow[a].x()));
                        choice = arrow[a];
                    }
                }
            }
        }
    }
    if (choice != QPoint(-1, -1)) {
        setDirection(choice);
    }
}

void Ghost::setCritical(QPoint pt) {
    critical = pt;
}

void Ghost::changeMode() {
    if (mode == Mode::Chase) {
        chaseTimer->setInterval(10000);
        mode = Mode::Scatter;
//        qDebug() << "start scatter";
    }
    else {
        chaseTimer->setInterval(20000);
        mode = Mode::Chase;
//        qDebug() << "start chase";
    }
}

void Ghost::nerfInterval() {
    if (home || mode == Mode::Home)
        return;
    chaseTimer->stop();
    if (mode != Mode::Frighten)
        prevMode = mode;
    mode = Mode::Frighten;
    remainNerf += 6;
    nerfTimer->start(1000);
    index_i = 1;
}

void Ghost::timeLeft() {
    remainNerf --;
    if (remainNerf > 3) {
        index_i = 1;
        shine->stop();
    }
    else if (remainNerf <= 3 && remainNerf > 0)
        shine->start(200);
    else if (remainNerf <= 0) {
        chaseTimer->start();
        mode = prevMode;
        shine->stop();
        nerfTimer->stop();
    }
}

void Ghost::die() {
    // emit the collide event and change the mode
    emit collide(this);
    step_size = 2;
    mode = Mode::Dead;

    // deal with the nerf mode end
    nerfTimer->stop();
    remainNerf = 0;
    shine->stop();

    // reposition to the coordinate
    setPos(int(x()) / 16 * 16, int(y() - 35) / 16 * 16 + 35);
    qDebug() << "the ghost is dead" << pos();

    // turn off the mode change timer
    chaseTimer->stop();
}

void Ghost::setKind(char ipt) {
    kind = ipt;
}

void Ghost::check() {
    if (mode == Mode::End)
        return;
    if (y() == 211. && mode == Mode::Home) {
        mode = Mode::Chase;
        chaseTimer->start();
        tmpDir = QPoint(-1, -1);

        // decide which direction should go
        QPoint arrow[2] = {Dir::Left, Dir::Right};
        QPoint target = setTarget(), choice;
        qreal length = 9999999;
        for (int a = 0; a < 2; a ++) {
            if (distance(target, QPoint(int(y() - 35) / 16, int(x()) / 16)) < length) {
                length = distance(target, QPoint(int(y() - 35) / 16 + arrow[a].y(), int(x()) / 16 + arrow[a].x()));
                choice = arrow[a];
            }
        }
        direction = choice;
    }
    else if (mode != Mode::Dead) {
        QPointF origin = pos() + QPointF(boundingRect().width() / 2 - 8, boundingRect().height() / 2 - 8);
        QPointF player = compass->getPlayerPos() - QPointF(7, 7) + QPointF(15, 15);

        if (int(origin.y()) / 16 == int(player.y()) / 16 && int(origin.x()) / 16 == int(player.x()) / 16) {
            if (mode == Mode::Frighten)
                die();
            else {
                // emit the signal to end the game
                mode = Mode::End;
                emit fail();
            }
        }
    }
    else  if (pos() == QPointF(216, 211) && mode == Mode::Dead)
        direction = Dir::Down;
    else if (pos() == QPointF(216, 259) && mode == Mode::Dead) {
        direction = Dir::Up;
        mode = Mode::Home;
        step_size = 1;
    }
}

void Ghost::shining() {
    index_i ++;
    index_i %= 2;
    setPixmap(fright[index_i][index_j]);
}

void Ghost::pause() {
    chaseTimer->stop();
    nerfTimer->stop();
    shine->stop();
    switchTimer->stop();
    tmr->stop();
}

void Ghost::start() {
    switchTimer->start();
    if (mode == Mode::Frighten)
        nerfTimer->start();
    else if (mode != Mode::Home)
        chaseTimer->start();
    else
        tmr->start();
}

void Ghost::restore() {
    mode = Mode::Chase;
    step_size = 1;
    index_i = 1;
    index_j = 0;
    nerf = false;
    tmpDir = QPoint(-1, -1);
    direction = Dir::Left;
}

void Ghost::setInitDirection(QPoint dir) {
    direction = dir;
}

void Ghost::setMode(int mode_ipt) {
    mode = mode_ipt;
    if (mode == Mode::Home) {
        chaseTimer->stop();
        home = true;
    }
}
