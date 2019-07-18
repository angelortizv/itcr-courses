#include "Queue.h"

queue::queue(){
    queueItem* _pNext = _pHead = _pTail = 0;
    _itemCounter = 0;
}

queue::~queue(){

}

void queue::addItem(char *pData){
    queueItem *pItem = new queueItem(pData, ++_itemCounter);

    if ( 0 == _pHead )
        _pHead = _pTail = pItem;
    else{
        _pTail->setNext(pItem);
        _pTail = pItem;
    }
    queueItem* _pNext = 0;
}


void queue::removeItem(){
    if ( _pTail == 0 && _pHead == 0 ){
        // empty body
    }
    else{
        queueItem* _pItem = _pHead->getNext();
        delete _pHead;
        _pHead = _pItem;
    }

}

void queue::print(){
    queueItem* _pItem = _pHead;
    while ( _pItem != NULL ){
        cout << _pItem->getId() << endl;
        cout << _pItem->getData() << endl;
        _pItem = _pItem->getNext();
    }
}

void queue::erase(){
    while ( _pHead != NULL ){
        queueItem* _pItem = _pHead->getNext();
        delete _pHead;
        _pHead = _pItem;
    }
}