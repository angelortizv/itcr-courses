#ifndef WINNER_H
#define WINNER_H

#include <QDialog>
#include <QDesktopServices>
#include "mainwindow.h"

namespace Ui {
class Winner;
}

class Winner : public QDialog
{
    Q_OBJECT

public:
    explicit Winner(QWidget *parent = 0);
    ~Winner();

private slots:
    void on_exit_button_clicked();

    void on_mainMenu_button_clicked();

    void on_moreInfo_button_clicked();

private:
    Ui::Winner *ui;
    void loadUI();
    static const int font_size = 10;
    static const int font_size_2 = 8;
    const QString font_family = "Joystix";
};

#endif // WINNER_H
