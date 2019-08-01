#include "pinky.h"

Pinky::Pinky(Compass *compass_ipt): Ghost(compass_ipt), compass(compass_ipt) {
    // set the origin point of the character
    setInitDirection(Dir::Up);
    loadPicture(":/img/ghost/pinky/");
    setCritical(QPoint(1, 1));
    setKind('p');
    setMode(Mode::Home);

    tmr = new QTimer();
}

QPoint Pinky::setTarget() {
    QPoint target = compass->getPlayerLoc(), dire = compass->getPlayerDir();
    target += 4 * QPoint(dire.y(), dire.x());

    return target;
}

void Pinky::sendOut() {
    home = false;
}

void Pinky::restore() {
    Ghost::restore();
    setInitDirection(Dir::Up);
    setMode(Mode::Home);
    connect(tmr, SIGNAL(timeout()), this, SLOT(sendOut()));
    tmr->start(1760);
}
