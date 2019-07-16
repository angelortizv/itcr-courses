#ifndef LINKEDLIST_LIST_H
#define LINKEDLIST_LIST_H

#include <fstream>
#include <iostream>
#include <stdlib.h>


#include "Node.h"

using namespace std;

template <class T>

class List
{
public:
    List();
    ~List();

    void add_head(T);
    void add_end(T);
    void add_sort(T);
    void concat(List);
    void del_all();
    void del_by_data(T);
    void del_by_position(int);
    void fill_by_user(int);
    void fill_random(int);
    void intersection(List);
    void invert();
    void load_file(string);
    void print();
    int size();
    T getbyposicion(int);
    void save_file(string);
    bool search(T);
    void sort();

private:
    Node<T> *m_head;
    int m_num_nodes;
};


#endif //LINKEDLIST_LIST_H
