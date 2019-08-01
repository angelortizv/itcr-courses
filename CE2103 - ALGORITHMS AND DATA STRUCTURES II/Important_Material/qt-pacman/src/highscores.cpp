#include "highscores.h"
#include "ui_highscores.h"

HighScores::HighScores(QWidget *parent) :
    QDialog(parent),
    ui(new Ui::HighScores)
{
    ui->setupUi(this);
    loadUI();
    addHighScoresToTable("angelortizv", 2000);
    addHighScoresToTable("test", 100);
}

HighScores::~HighScores()
{
    delete ui;
}

void HighScores::loadUI(){
    QFontDatabase::addApplicationFont(":/font/pixel.ttf");
    ui->goback_button->setFont(QFont(font_family, font_size));
    ui->hs_label->setFont(QFont(font_family, font_size));
}

void HighScores::on_goback_button_clicked()
{
    close();
    MainWindow *w = new MainWindow();
    w->show();
}

void HighScores::addHighScoresToTable(QString name, int score){
    QTableWidget *table = ui->tableWidget;
    QTableWidgetItem *nameItem = new QTableWidgetItem(name);
    QTableWidgetItem *scoreItem = new QTableWidgetItem();
    nameItem->setTextAlignment(Qt::AlignCenter);
    scoreItem->setData(Qt::EditRole, score);
    scoreItem->setTextAlignment(Qt::AlignCenter);

    nameItem->setFont(QFont(font_family, font_size));
    scoreItem->setFont(QFont(font_family, font_size));

    int index = table->rowCount();
    table->insertRow(index);
    table->setItem(index, 0, nameItem);
    table->setItem(index, 1, scoreItem);
    table->sortItems(1, Qt::DescendingOrder);

}

void HighScores::cleanTable(){
    QTableWidget *table = ui->tableWidget;
    table->clear();
    for (int i = 0; i < table->rowCount(); i ++){
        table->removeRow(i);
    }
}
