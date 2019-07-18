#include <iostream>
#include <linkedList/LinkedListInterface.h>
#include <queue/QueueInterface.h>

using namespace std;

int main() {
    bool running = true;
    int validation;
    while(running){
        cout << "Insert: \n"
                "1. To execute Linked List Test,\n"
                "2. To execute Queue Test,\n"
                "3. To exit the loop." << endl;
        cin >> validation;
        if(validation == 1){
            LinkedListInterface *linkedListInterface = new LinkedListInterface();
            linkedListInterface->linkedListRunner();
        } else if(validation == 2){
            QueueInterface *queueInterface = new QueueInterface();
            queueInterface->queueRunner();
        } else if(validation == 3){
            running = false;
        } else{
            cout << "Insert valid option." << endl;
        }
    }
}