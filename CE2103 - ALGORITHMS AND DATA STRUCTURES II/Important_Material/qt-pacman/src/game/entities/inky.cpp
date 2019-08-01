#include "inky.h"

Inky::Inky(Compass *compass_ipt): Ghost (compass_ipt), compass(compass_ipt) {
    loadPicture(":/img/ghost/inky/");
    setInitDirection(Dir::Down);
    setCritical(QPoint(27, 27));
    setKind('i');
    setMode(Mode::Home);

    tmr = new QTimer();
}

QPoint Inky::setTarget() {
    QPoint blinky = compass->getBlinkyPos();
    QPoint pacman = compass->getPlayerLoc();
    QPoint dire = compass->getPlayerDir();

    QPoint target = blinky + 2 * (pacman + 2 * QPoint(dire.y(), dire.x()) - blinky);

    return target;
}

void Inky::sendOut() {
    disconnect(tmr, SIGNAL(timeout()), this, SLOT(sendOut()));
    QEventLoop loop;
    setInitDirection(Dir::Right);
    connect(tmr, SIGNAL(timeout()), &loop, SLOT(quit()));
    tmr->start(352);
    loop.exec();
    setInitDirection(Dir::Up);
    home = false;
}

void Inky::restore() {
    Ghost::restore();
    setInitDirection(Dir::Down);
    setMode(Mode::Home);
    connect(tmr, SIGNAL(timeout()), this, SLOT(sendOut()));
    tmr->start(5280);
}
