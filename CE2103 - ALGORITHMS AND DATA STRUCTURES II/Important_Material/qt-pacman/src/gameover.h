#ifndef GAMEOVER_H
#define GAMEOVER_H

#include <QDialog>
#include <QMovie>
#include "mainwindow.h"
#include "highscores.h"
#include "game/dashboard.h"

namespace Ui {
class GameOver;
}

class GameOver : public QDialog
{
    Q_OBJECT

public:
    explicit GameOver(QWidget *parent = 0);
    ~GameOver();
    Dashboard *board;

private slots:
    void on_goback_button_clicked();

    void on_ok_button_clicked();

private:
    Ui::GameOver *ui;
    static const int font_size = 15;
    static const int font_size_2 = 10;
    const QString font_family = "Joystix";
    void loadUI();
};

#endif // GAMEOVER_H
