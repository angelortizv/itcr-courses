#include "winner.h"
#include "ui_winner.h"

Winner::Winner(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::Winner)
{
    ui->setupUi(this);
    loadUI();
}

Winner::~Winner()
{
    delete ui;
}

void Winner::loadUI(){
    QMovie *movie=new QMovie(":/img/winner_gif.gif");
    ui->gifwin_label->setMovie(movie);
    movie->start();

    QFontDatabase::addApplicationFont(":/font/pixel.ttf");
    ui->congrats_label->setFont(QFont(font_family, font_size));
    ui->amazing_label->setFont(QFont(font_family, font_size));
    ui->exit_button->setFont(QFont(font_family, font_size_2));
    ui->mainMenu_button->setFont(QFont(font_family, font_size_2));
    ui->moreInfo_button->setFont(QFont(font_family, font_size_2));
}

void Winner::on_exit_button_clicked()
{
    this->close();
}

void Winner::on_mainMenu_button_clicked()
{
    close();
    MainWindow *w = new MainWindow();
    w->show();
}

void Winner::on_moreInfo_button_clicked()
{
    QString link = "https://github.com/angelortizv/pacman";
    QDesktopServices::openUrl(QUrl(link));
}
