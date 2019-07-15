package ce.itcr.dataStructures.heap;

import org.jetbrains.annotations.NotNull;
import org.jetbrains.annotations.Nullable;

import java.lang.reflect.Array;

/**
 * Created by Prakash on 01-11-2018.
 */
public class Heap<T extends Comparable> {
    private int capacity;
    private int firstFreeIndex;
    private boolean isMaxHeap;
    private Class<T> classType;

    @NotNull
    private T[] array;
    Heap() {}
    Heap(boolean isMaxHeap, int initialCapacity, Class<T> classType) {
        this.capacity = initialCapacity;
        this.isMaxHeap = isMaxHeap;
        this.classType = classType;
        this.array = (T[]) Array.newInstance(classType, this.capacity);
    }

    Heap(boolean isMaxHeap, T[] array) {
        if (array == null || array.length == 0) throw new RuntimeException("Array is empty");
        this.capacity = array.length;
        this.isMaxHeap = isMaxHeap;
        this.classType = (Class<T>) array[0].getClass();
        this.array = (T[]) Array.newInstance(classType, this.capacity);
        for (int i = 0; i < array.length; i++)
            this.array[i] = array[i];

        for (int parentIndex = this.parentIndex(array.length-1); parentIndex >=0; parentIndex--)
            this.percolateDown(parentIndex);
    }

    public int parentIndex(int childIndex) {
        if (childIndex < 1 || childIndex >= firstFreeIndex) return -1;
        return (childIndex -1)/2;
    }

    public int leftChildIndex(int parentIndex) {
        if (parentIndex < 0 || parentIndex >= firstFreeIndex) return -1;
        return parentIndex*2 +1;
    }

    public int rightChildIndex(int parentIndex) {
        if (parentIndex < 0 || parentIndex >= firstFreeIndex) return -1;
        return parentIndex*2 + 2;
    }

    // Time complexity - O(log n)
    public void offer(T element) {
        if (firstFreeIndex == this.capacity) resize();
        array[firstFreeIndex++] = element;

        int childIndex = firstFreeIndex-1;
        int parentIndex = this.parentIndex(childIndex);
        while (parentIndex >= 0 && (array[childIndex].compareTo(array[parentIndex]) > 0) == isMaxHeap) {
            swap(childIndex, parentIndex);
            parentIndex = this.parentIndex(childIndex = parentIndex);
        }
    }

    private void swap(int a, int b) {
        T temp = array[a];
        array[a] = array[b];
        array[b] = temp;
    }

    @Nullable
    public T poll() {
        if (firstFreeIndex == 0) return null;
        T element = array[0];
        swap(0, this.firstFreeIndex-1);
        firstFreeIndex--;
        percolateDown(0);
        return element;
    }

    @Nullable
    public T peek() {
        if (firstFreeIndex == 0) return null;
        return array[0];
    }

    // Time Complexity -- O(log n)
    private void percolateDown(int parentIndex){
        if (parentIndex < 0 || parentIndex > this.parentIndex(firstFreeIndex-1)) return;
        int indexToSwap = (array[leftChildIndex(parentIndex)].compareTo(array[rightChildIndex(parentIndex)]) > 0) == isMaxHeap ?
                leftChildIndex(parentIndex) : rightChildIndex(parentIndex);
        if ((array[indexToSwap].compareTo(array[parentIndex]) < 0) == isMaxHeap) return;
        swap(parentIndex, indexToSwap);
        percolateDown(indexToSwap);
    }

    // Time Complexity - O(n)
    private void resize(){
        T[] arr = (T[]) Array.newInstance(classType, this.capacity *= 2);
        System.arraycopy(array, 0, arr, 0, array.length);
        this.array = arr;
    }

    public int size(){
        return this.firstFreeIndex;
    }

    public boolean isEmpty(){
        return this.firstFreeIndex == 0;
    }


}
