#ifndef BLINKY_H
#define BLINKY_H

#include <QTimer>
#include <QObject>
#include <QString>
#include <cmath>
#include <QDebug>
#include "character.h"
#include "ghost.h"
#include "../compass.h"

class Blinky: public Ghost {
    Q_OBJECT
public:
    Blinky(Compass *compass_ipt);
    QPoint setTarget();
    void sendOut();

private:
    Compass *compass;
};

#endif // BLINKY_H
