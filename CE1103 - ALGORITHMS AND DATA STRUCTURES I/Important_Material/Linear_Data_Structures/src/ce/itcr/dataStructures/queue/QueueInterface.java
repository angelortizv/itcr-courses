package ce.itcr.dataStructures.queue;

public class QueueInterface {
    public void QueueRunner(){
        Queue queueTest = new Queue();
        queueTest.enqueue(10);
        queueTest.enqueue(20);
        queueTest.print();
//        queueTest.peek();
        queueTest.dequeue();
        queueTest.print();
    }
}
