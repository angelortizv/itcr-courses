#ifndef PROYECTO1_SCRABBLE_queue_H
#define PROYECTO1_SCRABBLE_queue_H

#include <iostream>
#include "QueueItem.h"

using namespace std;

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
