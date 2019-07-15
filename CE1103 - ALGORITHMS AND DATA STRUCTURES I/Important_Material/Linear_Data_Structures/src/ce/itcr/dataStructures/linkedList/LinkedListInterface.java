package ce.itcr.dataStructures.linkedList;

public class LinkedListInterface {
    public void linkedListRunner(){
        LinkedList listTest = new LinkedList();
        listTest.insert(20);
        listTest.insert(40);
        listTest.insert(60);
        listTest.print();
        listTest.insertAtStart(10);
        listTest.print();
        listTest.insertAt(2, 45);
        listTest.print();
        listTest.deleteAt(0);
        listTest.print();
    }
}
