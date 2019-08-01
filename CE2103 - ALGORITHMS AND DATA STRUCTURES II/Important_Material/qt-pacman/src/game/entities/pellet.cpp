#include "pellet.h"

Pellet::Pellet(Game *parent_ipt) {
    parent = parent_ipt;
    setPixmap(QPixmap(":/img/item/pellet.png").scaledToWidth(16));
    visible = true;
}

void Pellet::eaten() {
    emit pelletEaten();
    delete this;
}

void Pellet::shine() {
    visible = !visible;
    if (visible)
        show();
    else
        hide();
}
