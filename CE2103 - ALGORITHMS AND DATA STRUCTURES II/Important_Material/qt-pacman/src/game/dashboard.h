#ifndef DASHBOARD_H
#define DASHBOARD_H

#include <QObject>
#include <QGraphicsItem>
#include <QGraphicsTextItem>
#include <QFontDatabase>
#include <algorithm>
#include <QLabel>

using std::max;

class Dashboard: public QObject, public QGraphicsItemGroup {
    Q_OBJECT
public:
    Dashboard(QObject *parent = 0);
    void addScore(int ipt);
    void reset();

    int getScore();
    int getHighScore();

    int getLifes() const;
    void setLifes(int value);

    int lifes = 3;

private:
    int score, high;
    QGraphicsTextItem *text_score;
    QGraphicsTextItem *text_high;

    static const int font_size = 20;
    const QString font_family = "Joystix";
};

#endif // DASHBOARD_H
