package ce.itcr.algorithms.searching;

import java.util.Scanner;

public class SearchingAlgorithmsInterface {
    public void searchingAlgorithmsRunner() {
        boolean running = true;
        while (running) {
            System.out.println("\n Insert: \n" +
                    "1. To execute Binary Search,\n" +
                    "2. To execute Linear Search,\n" +
                    "3. To exit the loop.");
            Scanner scanner = new Scanner(System.in);
            int opt = scanner.nextInt();
            if (opt == 1) {
                BinarySearch bs = new BinarySearch();
                int arr[] = {2, 3, 4, 10, 40};
                int n = arr.length;
                int x = 10;
                int result = bs.binarySearch(arr, 0, n - 1, x);
                if (result == -1) {
                    System.out.println("Element not present");
                } else{
                    System.out.println("Element found at index " + result);
                }
            } else if (opt == 2) {
                LinearSearch ls = new LinearSearch();
                int myList[] = {1,2,3,8,9,12};
                int key = 2;
                String output = ls.linearSearch(myList, key) ? "Successful Search" : "Unsuccessful Search";
                System.out.println(output);
            } else if (opt == 3) {
                running = false;
            } else {
                System.out.println("Insert valid option.");
            }
        }
    }
}
