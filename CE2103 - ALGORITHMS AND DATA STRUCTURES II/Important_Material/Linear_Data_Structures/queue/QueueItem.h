#ifndef PROYECTO1_SCRABBLE_queueItem_H
#define PROYECTO1_SCRABBLE_queueItem_H

#include <iostream>
#include <cstring>

using  namespace std;

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
