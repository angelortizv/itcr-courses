#ifndef CLYDE_H
#define CLYDE_H

#include <QObject>
#include <QTimer>
#include <QEventLoop>
#include <QDebug>
#include "ghost.h"
#include "../compass.h"

class Clyde: public Ghost {
    Q_OBJECT
public:
    Clyde(Compass *compass_ipt);
    QPoint setTarget();

    void restore();

public slots:
    void sendOut();

private:
    Compass *compass;
};

#endif // CLYDE_H
