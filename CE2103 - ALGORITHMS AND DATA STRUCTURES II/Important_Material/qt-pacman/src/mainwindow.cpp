#include "mainwindow.h"
#include "ui_mainwindow.h"
#include "winner.h"

MainWindow::MainWindow(QWidget *parent) :
    QMainWindow(parent),
    ui(new Ui::MainWindow)
{
    ui->setupUi(this);
    loadUI();
}

MainWindow::~MainWindow()
{
    delete ui;
}

void MainWindow::loadUI(){
    QMovie *movie=new QMovie(":/img/initial_gif.gif");
    ui->initial_gif_label->setMovie(movie);
    movie->start();

    QFontDatabase::addApplicationFont(":/font/pixel.ttf");
    ui->playgame_button->setFont(QFont(font_family, font_size));
    ui->highscores_button->setFont(QFont(font_family, font_size));
    ui->quit_button->setFont(QFont(font_family, font_size));
    ui->developer_label->setFont(QFont(font_family, font_size_2));

}

void MainWindow::on_highscores_button_clicked()
{
    close();
    HighScores highscores;
    highscores.setModal(true);
    highscores.exec();
}

void MainWindow::on_playgame_button_clicked()
{
    close();
    Game *game = new Game();
    game->afterGameStart();
    game->show();
}

void MainWindow::on_quit_button_clicked()
{
    this->close();
}
