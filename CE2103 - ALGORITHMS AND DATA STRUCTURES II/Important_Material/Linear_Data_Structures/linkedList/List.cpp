#include "List.h"

LinkedList::LinkedList(){
    cout << "\nEntering Constructor ..." << endl;
    head = new node;
    head -> song = "head (contains no song data)";
    head -> artist = "head (contains no artist data)";
    head -> next = NULL;
    listLength = 0;
    cout << "Success: head node created. listLength set to 0." << endl;
}

LinkedList::~LinkedList(){
    cout << "\nEntering Destructor..." << endl;
    node * p = head;
    node * q = head;
    while (q){
        p = q;
        q = p -> next;
        delete p;
    }
    cout << "Success: list is deleted." << endl;
}


bool LinkedList::insertNode( node * newNode, int position ){
    cout << "\nEntering insertNode ..." << endl;
    if ( (position <= 0) || (position > listLength + 1) ){
        cout << "Error: the given position is out of range." << endl;
        return false;
    }
    if (!head -> next){
        head -> next = newNode;
        listLength++;
        cout << "Success: added '" << newNode -> song << "' to position " << position << ".\n";
        cout << "listLength = " << listLength << endl;
        return true;
    }
    int count = 0;
    node * p = head;
    node * q = head;
    while (q){
        if (count == position){
            p -> next = newNode;
            newNode -> next = q;
            listLength++;
            cout << "Success: added '" << newNode -> song << "' to position " << position << ".\n";
            cout << "listLength = " << listLength << endl;
            return true;
        }
        p = q;
        q = p -> next;
        count++;
    }
    if (count == position){
        p -> next = newNode;
        newNode -> next = q;
        listLength++;
        cout << "Success: added '" << newNode -> song << "' to position " << position << ".\n";
        cout << "listLength = " << listLength << endl;
        return true;
    }
    cout << "Error: song node was not added to list." << endl;
    return false;
}

bool LinkedList::removeNode( int position ){
    cout << "\nEntering removeNode..." << endl;
    if ( (position <= 0) || (position > listLength + 1) ){
        cout << "Error: the given position is out of range." << endl;
        return false;
    }
    if (!head -> next){
        cout << "Error: there is nothing to remove." << endl;
        return false;
    }

    int count = 0;
    node * p = head;
    node * q = head;
    while (q){
        if (count == position){
            p -> next = q -> next;
            delete q;
            listLength--;
            cout << "Success: node at position " << position << " was deleted." << endl;
            cout << "listLength = " << listLength << endl;
            return true;
        }
        p = q;
        q = p -> next;
        count++;
    }
    cout << "Error: nothing was removed from the list." << endl;
    return false;
}

void LinkedList::printList(){
    cout << "\nEntered printList..." << endl;
    int count = 0;
    node * p = head;
    node * q = head;
    cout << "\n---------------------\n";
    cout << " Song Playlist\n";
    while (q){
        p = q;
        cout << "---------------------\n";
        cout << "\t position: " << count << "\n";
        cout << "\t song: " << p -> song << "\n";
        cout << "\t artist: " << p -> artist << "\n";
        q = p -> next;
        count++;
    }
}
