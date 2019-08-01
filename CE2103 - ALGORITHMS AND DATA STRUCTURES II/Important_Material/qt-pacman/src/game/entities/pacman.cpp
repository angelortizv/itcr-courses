#include "pacman.h"

Pacman::Pacman(Compass *compass_ipt) {
    // set the origin to fit the coordinate
    setOffset(QPoint(-7, -7));
    direction = QPoint(0, 0);
    tmpDir = QPoint(0, 0);

    // load the picture in
    for (int i = 0; i < 3; i ++) {
        pic[i].load(":/img/pacman/" + QString::number(i) + ".png");
        pic[i] = pic[i].scaledToHeight(30);
    }
    setPixmap(pic[0]);
    setTransformOriginPoint(boundingRect().width() / 2 - 7, boundingRect().height() / 2 - 7);

    for (int i = 0; i < 11; i ++) {
        disolve[i].load(":/img/pacman/dead/" + QString::number(i) + ".png");
        disolve[i] = disolve[i].scaledToHeight(30);
    }

    // set the timer for moving
    switchTimer = new QTimer();
    connect(switchTimer, SIGNAL(timeout()), this, SLOT(switchAnimate()));
    switchTimer->setInterval(50);

    // create the compass object
    compass = compass_ipt;
    compass->setLoc(QPoint(14, 16), 'p');

    index = 0;
    add = 1;
    dead = false;
}

void Pacman::move() {
    if (dead)
        return;
    // handling bounding
    compass->setPos(pos());
    if (y() == 259. && (x() < 0 || x() >= 448)) {
        if (tmpDir == Dir::Left || tmpDir == Dir::Right)
            direction = tmpDir;
        if (direction == Dir::Left)
            setRotation(180);
        else if (direction == Dir::Right)
            setRotation(0);
        setPos(pos() + direction * 2);

        if (x() < -30)
            setX(478);
        else if (x() > 478)
            setX(-30);
    }
    // handling normal move
    else if (int(y() - 35) % 16 == 0 && int(x()) % 16 == 0) {
        compass->setLoc(QPoint(int(y() - 35) / 16, int(x()) / 16), 'a');
        if (tmpDir != direction && compass->canMove(pos(), tmpDir)) {
            direction = tmpDir;
            if (direction == Dir::Up)
                setRotation(270);
            else if (direction == Dir::Down)
                setRotation(90);
            else if (direction == Dir::Left)
                setRotation(180);
            else if (direction == Dir::Right)
                setRotation(0);
        }
        else if (compass->canMove(pos(), direction)) {
            compass->check(pos(), direction);
            setPos(pos() + direction * 2);
            switchTimer->start();
        }
        else {
            compass->check(pos(), direction);
            switchTimer->stop();
            setPixmap(pic[1]);
        }
    }
    else
        setPos(pos() + direction * 2);
}

void Pacman::setDirection(QPoint dir) {
    if (x() == 216. && y() == 403. && direction == QPoint(0, 0) && (dir == Dir::Left || dir == Dir::Right)) {
        direction = dir;
        if (direction == Dir::Left)
            setRotation(180);
        else if (direction == Dir::Right)
            setRotation(0);
    }
    tmpDir = dir;
}

void Pacman::switchAnimate() {
    if (!dead) {
        setPixmap(pic[index]);
        index += add;
        if (index >= 2 || index <= 0)
            add = -add;
    }
    else {
        if (index < 11) {
            setPixmap(disolve[index]);
            index += add;
        }
        else if (index >= 11) {
            switchTimer->stop();
            dead = false;
            hide();
        }

    }
}

void Pacman::die() {
    qDebug() << "die";
    dead = true;
    switchTimer->stop();
    setRotation(0);
    switchTimer->start(50);
//    index = 0;
//    add = 1;
}

void Pacman::pause() {
    switchTimer->stop();
}

void Pacman::start() {
    switchTimer->start();
}

void Pacman::restore() {
    direction = QPoint(0, 0);
    tmpDir = QPoint(0, 0);
    setPixmap(pic[0]);
    switchTimer->stop();
    compass->setPos(pos());
    dead = false;
    index = 0;
    add = 1;
}
