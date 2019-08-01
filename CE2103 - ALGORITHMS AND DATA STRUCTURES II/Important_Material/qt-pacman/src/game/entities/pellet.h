#ifndef PELLET_H
#define PELLET_H

#include "item.h"
#include "../../game.h"

class Pellet: public Item {
    Q_OBJECT
public:
    Pellet(Game *parent_ipt);

    void eaten();

signals:
    void pelletEaten();

public slots:
    void shine();

private:
    Game *parent;
    bool visible;
};

#endif // PELLET_H
