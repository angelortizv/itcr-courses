#include "blinky.h"

Blinky::Blinky(Compass *compass_ipt): Ghost (compass_ipt), compass(compass_ipt) {
    loadPicture(":/img/ghost/blinky/");
    setInitDirection(Dir::Left);
    setCritical(QPoint(1, 27));
    setKind('b');
    tmr = new QTimer();
}

QPoint Blinky::setTarget() {
    QPoint player = compass->getPlayerLoc();
    compass->setLoc(QPoint(int(y() - 35) / 16, int(x()) / 16), 'b');
    return player;
}

void Blinky::sendOut() {}
