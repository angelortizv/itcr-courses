#ifndef CHARACTER_H
#define CHARACTER_H

#include <QObject>
#include <QGraphicsPixmapItem>
#include <cmath>

class Character : public QObject, public QGraphicsPixmapItem {
    Q_OBJECT
public:
    virtual void setDirection(QPoint dir) = 0;
    virtual void die() = 0;
    virtual void start() = 0;
    virtual void pause() = 0;
    virtual void restore() = 0;

public slots:
    virtual void move() = 0;
};

namespace Dir {
    const QPoint Up = QPoint(0, -1);
    const QPoint Down = QPoint(0, 1);
    const QPoint Left = QPoint(-1, 0);
    const QPoint Right = QPoint(1, 0);
}

#endif // CHARACTER_H
