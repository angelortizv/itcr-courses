#include "clyde.h"

Clyde::Clyde(Compass *compass_ipt): Ghost (compass_ipt), compass(compass_ipt) {
    loadPicture(":/img/ghost/clyde/");
    setCritical(QPoint(27, 1));
    setInitDirection(Dir::Down);
    setMode(Mode::Home);
    setKind('c');
    tmr = new QTimer();
}

QPoint Clyde::setTarget() {
    QPoint target;
    QPoint pos(int(y() - 35) / 16, int(x()) / 16);
    QPoint player = compass->getPlayerLoc();
    qreal dis = distance(pos, player);
    if (dis > 128){
        target = player;
    } else{
        target = QPoint(27, 1);
    }
    return target;
}

void Clyde::sendOut() {
    disconnect(tmr, SIGNAL(timeout()), this, SLOT(sendOut()));
    QEventLoop loop;
    setInitDirection(Dir::Left);
    connect(tmr, SIGNAL(timeout()), &loop, SLOT(quit()));
    tmr->start(352);
    loop.exec();
    setInitDirection(Dir::Up);
    home = false;
}

void Clyde::restore() {
    Ghost::restore();
    setMode(Mode::Home);
    setInitDirection(Dir::Down);
    connect(tmr, SIGNAL(timeout()), this, SLOT(sendOut()));
    tmr->start(10560);
}
