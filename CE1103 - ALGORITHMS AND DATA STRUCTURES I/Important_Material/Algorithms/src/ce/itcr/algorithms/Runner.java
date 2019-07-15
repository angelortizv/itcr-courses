package ce.itcr.algorithms;

import java.util.Scanner;

public class Runner {
    public static void main(String[] args){
        boolean running = true;
        while (running){
            System.out.println("Insert: \n" +
                    "1. To execute Sorting Algorithms,\n" +
                    "2. To execute Searching Algorithms,\n" +
                    "3. To exit the loop.");
            Scanner scanner = new Scanner(System.in);
            int opt = scanner.nextInt();
            if(opt == 1){

            } else if(opt == 2){

            } else if(opt == 3){
                running = false;
            } else{
                System.out.println("Insert valid option.");
            }


        }
    }
}
