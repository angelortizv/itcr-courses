package ce.itcr.dataStructures.queue;

import java.util.NoSuchElementException;

public class Queue {
    private Node head = null;
    private Node tail = null;

    public void enqueue(Object item){
        Node newNode = new Node(item, null);
        if (isEmpty()) {
            head = newNode;
        } else {
            tail.next = newNode;
        }
        tail = newNode;
    }

    public Object dequeue(){
        if (isEmpty()) {
            throw new NoSuchElementException("Cannot dequeue from empty Queue");
        }
        Object item = head.item;
        if (tail == head) {
            tail = null;
        }
        head = head.next;
        return item;
    }

    public Object peek(){
        if(head == null){
            throw new NoSuchElementException("Cannot peek from empty Queue");
        }
        System.out.println(head.item);
        return head.item;
    }

    public int size(){
        int count = 0;
        for(Node node = head; node != null; node = node.next){
            count++;
        }
        return count;
    }

    public boolean isEmpty(){
        return head == null;
    }

    public void print(){
        Node node = head;
        while(node.next != null){
            System.out.println(node.item);
            node = node.next;
        }
        System.out.println(node.item);
    }
}
