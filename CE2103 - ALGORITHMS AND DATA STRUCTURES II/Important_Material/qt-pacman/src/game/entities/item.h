#ifndef ITEM_H
#define ITEM_H

#include <QGraphicsItem>
#include <QObject>

class Item: public QObject, public QGraphicsPixmapItem {
    Q_OBJECT
public:
    virtual void shine() = 0;
    virtual void eaten() = 0;
};

#endif // ITEM_H
