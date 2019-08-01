#include "compass.h"

Compass::Compass(QObject *parent): QObject (parent) {
    initMap();
}

bool Compass::canMove(QPointF pos, QPointF direction) {
    int x = int(pos.y() - 35) / 16;
    int y = int(pos.x()) / 16;

    if (x + direction.y() >= 0 && x + direction.y() < 31 && y + direction.x() >= 0 && y + direction.x() < 28) {
        if (map[x + direction.y()][y + direction.x()] != 0)
            return true;
        else
            return false;
    }
    else if (x == 14 && y + direction.x() < 0)
        return true;
    else if (x == 14 && y + direction.x() > 27)
        return true;
    return false;

}

QList <QPoint> Compass::dots() {
    QList <QPoint> list;
    for (int i = 0; i < 31; i ++) {
        for (int j = 0; j < 28; j ++) {
            if (map[i][j] == 1)
                list.push_back(QPoint(i, j));
        }
    }
    return list;
}

QList <QPoint> Compass::pellets() {
    QList <QPoint> list;
    for (int i = 0; i < 31; i ++) {
        for (int j = 0; j < 28; j ++) {
            if (map[i][j] == 2)
                list.push_back(QPoint(i, j));
        }
    }
    return list;
}

void Compass::initMap() {
    map = {
        {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0},
        {0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0},
        {0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0},
        {0, 2, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 2, 0},
        {0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0},
        {0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0},
        {0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0},
        {0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0},
        {0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0},
        {0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, -1, 0, 0, -1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0},
        {-1, -1, -1, -1, -1, 0, 1, 0, 0, 0, 0, 0, -1, 0, 0, -1, 0, 0, 0, 0, 0, 1, 0, -1, -1, -1, -1, -1},
        {-1, -1, -1, -1, -1, 0, 1, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 1, 0, -1, -1, -1, -1, -1},
        {-1, -1, -1, -1, -1, 0, 1, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 1, 0, -1, -1, -1, -1, -1},
        {0, 0, 0, 0, 0, 0, 1, 0, 0, -1, 0, -1, -1, -1, -1, -1, -1, 0, -1, 0, 0, 1, 0, 0, 0, 0, 0, 0},
        {-1, -1, -1, -1, -1, -1, 1, -1, -1, -1, 0, -1, -1, -1, -1, -1, -1, 0, -1, -1, -1, 1, -1, -1, -1, -1, -1, -1},
        {0, 0, 0, 0, 0, 0, 1, 0, 0, -1, 0, -1, -1, -1, -1, -1, -1, 0, -1, 0, 0, 1, 0, 0, 0, 0, 0, 0},
        {-1, -1, -1, -1, -1, 0, 1, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 1, 0, -1, -1, -1, -1, -1},
        {-1, -1, -1, -1, -1, 0, 1, 0, 0, -1, -1, -1, -1, -1, -1, -1, -1, -1, -1, 0, 0, 1, 0, -1, -1, -1, -1, -1},
        {-1, -1, -1, -1, -1, 0, 1, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 1, 0, -1, -1, -1, -1, -1},
        {0, 0, 0, 0, 0, 0, 1, 0, 0, -1, 0, 0, 0, 0, 0, 0, 0, 0, -1, 0, 0, 1, 0, 0, 0, 0, 0, 0},
        {0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0},
        {0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0},
        {0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 1, 0},
        {0, 2, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 1, -1, -1, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 2, 0},
        {0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0},
        {0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0},
        {0, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0},
        {0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0},
        {0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0},
        {0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0},
        {0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0}
    };
}

void Compass::check(QPointF pos, QPoint dir) {
    int x = int(pos.y() - 35) / 16;
    int y = int(pos.x()) / 16;

    if (map[x][y] != 0 && map[x][y] != -1) {
        if (map[x][y] == 2)
            emit powerUp();
        map[x][y] = -1;
        emit eat(QPoint(x, y));
    }
    dir_player = dir;
}

QPoint Compass::getPlayerLoc() {
    return player;
}

void Compass::setLoc(QPoint pos, char charcter) {
    switch (charcter) {
    case 'a':
        player = pos;
        if (!nerf && (player == blinky || player == pinky || player == clyde || player == inky))
            emit fail();
        break;
    case 'b':
        blinky = pos;
        break;
    case 'i':
        inky = pos;
        break;
    case 'p':
        pinky = pos;
        break;
    case 'c':
        clyde = pos;
        break;
    }
}

QPoint Compass::getPlayerDir() {
    return dir_player;
}

QPoint Compass::getBlinkyPos() {
    return blinky;
}

void Compass::setPowerUp(bool ipt) {
    if (ipt)
        nerf = ipt;
    else
        nerf = ipt;
}

QList <QPoint> Compass::remainDots() {
    QList <QPoint> list;
    for (int i = 0; i < 31; i ++) {
        for (int j = 0; j < 28; j ++) {
            if (map[i][j] == 1 || map[i][j] == 2)
                list.push_back(QPoint(i, j));
        }
    }
    return list;
}

void Compass::setPos(QPointF pos) {
    player_pos = pos;
}

QPointF Compass::getPlayerPos() {
    return player_pos;
}
