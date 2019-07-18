#ifndef LINKEDLIST_LIST_H
#define LINKEDLIST_LIST_H

#include <iostream>
#include <string>

using namespace std;

struct node
{
    string song;
    string artist;
    node * next;
};

class LinkedList
{
private:
    node * head;
    int listLength;

public:
    LinkedList();
    ~LinkedList();
    bool insertNode( node * newNode, int position );
    bool removeNode( int position );
    void printList();

};

#endif //LINKEDLIST_LIST_H
