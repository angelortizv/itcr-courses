#include "animaterect.h"

AnimateRect::AnimateRect(int width, int height) {
    setRect(0, 0, width, height);
    setPen(QPen(Qt::transparent));
    setBrush(Qt::black);
    setOpacity(0.5);

    animate = new QPropertyAnimation();
    animate->setTargetObject(this);
    animate->setPropertyName("alpha");
    animate->setDuration(300);

    hide();
}

void AnimateRect::fadeIn() {
    show();
    animate->setStartValue(0);
    animate->setEndValue(0.5);
    animate->start();
}

void AnimateRect::fadeOut() {
    animate->setStartValue(0.5);
    animate->setEndValue(0);
    animate->start();
}
