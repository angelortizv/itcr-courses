#ifndef DOT_H
#define DOT_H

#include "item.h"
#include "../../game.h"

class Dot: public Item {
    Q_OBJECT
public:
    Dot(Game *parent_ipt);

    void eaten();
    void shine();

signals:
    void dotEaten();

private:
    Game *parent;
};

#endif // DOT_H
