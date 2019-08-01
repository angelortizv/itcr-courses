#include "dashboard.h"
#include <QDebug>

Dashboard::Dashboard(QObject *parent): QObject (parent) {
    score = 0;
    high = 0;
}

void Dashboard::addScore(int ipt) {
    score += ipt;
    high = max(score, high);
}

void Dashboard::reset() {
    score = 0;
}

int Dashboard::getScore() {
    return score;
}

int Dashboard::getHighScore() {
    return high;
}

int Dashboard::getLifes() const
{
    return lifes;
}

void Dashboard::setLifes(int value)
{
    lifes = value;
}
