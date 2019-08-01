#ifndef PINKY_H
#define PINKY_H

#include <QTimer>
#include <QObject>
#include <QString>
#include <cmath>
#include <QDebug>
#include "character.h"
#include "../compass.h"
#include "ghost.h"
#include "blinky.h"

class Pinky: public Ghost {
    Q_OBJECT
public:
    Pinky(Compass *compass_ipt);

    QPoint setTarget();
    void restore();

public slots:
    void sendOut();

private:
    Compass *compass;
};

#endif // PINKY_H
