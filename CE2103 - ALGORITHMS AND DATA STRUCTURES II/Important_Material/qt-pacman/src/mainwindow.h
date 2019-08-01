#ifndef MAINWINDOW_H
#define MAINWINDOW_H

#include <QMainWindow>
#include <QMovie>
#include <QFontDatabase>
#include "highscores.h"
#include "game.h"

namespace Ui {
class MainWindow;
}

class MainWindow : public QMainWindow
{
    Q_OBJECT

public:
    explicit MainWindow(QWidget *parent = 0);
    ~MainWindow();

private slots:
    void on_highscores_button_clicked();

    void on_playgame_button_clicked();

    void on_quit_button_clicked();

private:
    Ui::MainWindow *ui;
    static const int font_size = 15;
    static const int font_size_2 = 8;
    const QString font_family = "Joystix";

    void loadUI();
};

#endif // MAINWINDOW_H
