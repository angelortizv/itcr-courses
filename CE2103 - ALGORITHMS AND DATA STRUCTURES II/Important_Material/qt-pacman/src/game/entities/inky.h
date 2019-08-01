#ifndef INKY_H
#define INKY_H

#include <QObject>
#include <QDebug>
#include <QEventLoop>
#include "ghost.h"
#include "../compass.h"

class Inky: public Ghost {
    Q_OBJECT
public:
    Inky(Compass *compass_ipt);

    QPoint setTarget();
    void restore();

public slots:
    void sendOut();

private:
    Compass *compass;
};

#endif // INKY_H
