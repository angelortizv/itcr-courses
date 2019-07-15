package ce.itcr.dataStructures.heap;

public class HeapInterface {
    public void heapRun(){
        Heap<Integer> heap = new Heap<Integer>(false, 2, Integer.class);
        heap.offer(2);
        heap.offer(1);
        heap.offer(3);
        System.out.println(heap.poll());
        System.out.println(heap.size());
    }
}
