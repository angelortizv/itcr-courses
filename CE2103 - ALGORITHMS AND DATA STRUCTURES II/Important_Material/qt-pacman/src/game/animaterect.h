#ifndef ANIMATERECT_H
#define ANIMATERECT_H

#include <QGraphicsRectItem>
#include <QPropertyAnimation>
#include <QObject>
#include <QPen>

class AnimateRect: public QObject, public QGraphicsRectItem {
    Q_OBJECT
    Q_PROPERTY(QPointF pos READ pos WRITE setPos)
    Q_PROPERTY(qreal alpha READ opacity WRITE setOpacity)
public:
    AnimateRect(int width, int height);

    void fadeIn();
    void fadeOut();

private:
    QPropertyAnimation *animate;
};

#endif // ANIMATERECT_H
