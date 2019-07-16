/**
 * @file queueItem.h
 * @version 1.0
 * @date 01/04/2019
 * @autor angelortizv
 * @title Item en Cola
 * @brief Adquiere atributos como el elemento de análisis y el siguiente en cola.
 */

#ifndef PROYECTO1_SCRABBLE_queueItem_H
#define PROYECTO1_SCRABBLE_queueItem_H


class Queue;

class queueItem{
private:
    char _data[30];
    const int _itemId;
    queueItem* _pNext;
public:
    queueItem( char *pData, int id);
    void setNext(queueItem *pItem);
    queueItem* getNext() const;
    int getId() const;
    const char* getData() const;
};


#endif //PROYECTO1_SCRABBLE_queueItem_H
