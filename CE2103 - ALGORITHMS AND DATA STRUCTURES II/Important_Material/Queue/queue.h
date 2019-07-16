/**
 * @file queue.h
 * @version 1.0
 * @date 01/04/2019
 * @autor angelortizv
 * @title Métodos de Cola para Jugadores
 * @brief Incluye métodos básicos de cola como: enqueue, dequeue, print, removeItems
 */

#ifndef PROYECTO1_SCRABBLE_queue_H
#define PROYECTO1_SCRABBLE_queue_H


class queueItem;

class queue{
private:
    queueItem *_pHead;
    queueItem *_pTail;
    int _itemCounter;
public:
    queue();
    ~queue();
    void addItem(char *pData);
    void removeItem();
    void print();
    void erase();

};



#endif //PROYECTO1_SCRABBLE_queue_H
