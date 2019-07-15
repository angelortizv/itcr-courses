package ce.itcr.algorithms.sorting;

import java.util.Scanner;

public class SortingAlgorithmsInterface {
    public void sortingAlgorithmsRunner() {
        boolean running = true;
        while (running) {
            System.out.println("\n Insert: \n" +
                    "1. To execute Bubble Sort,\n" +
                    "2. To execute Quick Sort,\n" +
                    "3. To exit the loop.");
            Scanner scanner = new Scanner(System.in);
            int opt = scanner.nextInt();
            if (opt == 1) {
                BubbleSort bs = new BubbleSort();
                int n = 5;
                int a[] = new int[]{2,5,1,4,5};
                bs.sort(a,5);
            } else if (opt == 2) {
                QuickSort qs = new QuickSort();
                int n = 6;
                int b[] = new int[]{24,55,61,4,5,7};
                int start = 0;
                int end = n-1;
                qs.qsort(b,start,end);
            } else if (opt == 3) {
                running = false;
            } else {
                System.out.println("Insert valid option.");
            }
        }
    }
}
