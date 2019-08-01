#ifndef HIGHSCORES_H
#define HIGHSCORES_H

#include <QDialog>
#include <QGraphicsItem>
#include "mainwindow.h"

namespace Ui {
class HighScores;
}

class HighScores : public QDialog
{
    Q_OBJECT

public:
    explicit HighScores(QWidget *parent = 0);
    ~HighScores();
    void addHighScoresToTable(QString name, int score);
    void cleanTable();

private slots:
    void on_goback_button_clicked();

private:
    Ui::HighScores *ui;
    static const int font_size = 15;
    static const int font_size_2 = 8;
    static const int font_size_title = 22;
    const QString font_family = "Joystix";
    void loadUI();
};

#endif // HIGHSCORES_H
