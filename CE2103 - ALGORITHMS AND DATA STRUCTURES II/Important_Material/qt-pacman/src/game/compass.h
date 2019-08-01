#ifndef COMPASS_H
#define COMPASS_H

#include <QObject>
#include <QGraphicsItem>
#include <QDebug>

class Compass: public QObject {
    Q_OBJECT
public:
    Compass(QObject *parent = 0);

    void initMap();
    void check(QPointF pos, QPoint dir);

    bool canMove(QPointF pos, QPointF direction);
    QList <QPoint> dots();
    QList <QPoint> pellets();
    QList <QPoint> remainDots();

    void setLoc(QPoint pos, char character);
    void setPos(QPointF pos);
    void setPowerUp(bool ipt);
    QPoint getPlayerLoc();
    QPointF getPlayerPos();
    QPoint getPlayerDir();
    QPoint getBlinkyPos();

signals:
    void eat(QPoint pos);
    void powerUp();
    void fail();

private:
    QList <QList <int> > map;
    QPoint player, blinky, inky, pinky, clyde;
    QPoint dir_player;
    QPointF player_pos;
    bool nerf;
};


#endif // COMPASS_H
