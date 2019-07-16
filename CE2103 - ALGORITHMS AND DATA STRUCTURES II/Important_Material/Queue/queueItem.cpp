#include <iostream>
#include "queueItem.h"
#include <cstring>

using namespace std;

queueItem::queueItem( char *pData, int id) : _itemId(id) {
    strncpy( _data, pData, strlen( pData ) +1 );
    _pNext = NULL;
}

void queueItem::setNext( queueItem *pItem ){
    _pNext = pItem;
}

queueItem* queueItem::getNext() const{
    return _pNext;
}

int queueItem::getId() const{
    return _itemId;
}

const char* queueItem::getData() const{
    return _data;
}