package ce.itcr.dataStructures.stack;

import java.util.NoSuchElementException;

public class Stack {

    private Node top = null;

    public void push(Object item) {
        top = new Node(item, top);
    }

    public Object pop() {
        if (top == null) {
            throw new IllegalStateException("Cannot pop from a empty stack");
        }
        Object result = peek();
        top = top.next;
        return result;
    }

    public Object peek() {
        if (top == null) {
            throw new NoSuchElementException("Cannot peek from a empty stack");
        }
        return top.item;
    }

    public int size() {
        int size = 0;
        for (Node node = top; node != null; node = node.next) {
            size++;
        }
        return size;
    }

    public boolean isEmpty() {
        return top == null;
    }

    public void print(){
        Node node = top;
        while(node.next != null){
            System.out.println(node.item);
            node = node.next;
        }
        System.out.println(node.item);
    }

}
