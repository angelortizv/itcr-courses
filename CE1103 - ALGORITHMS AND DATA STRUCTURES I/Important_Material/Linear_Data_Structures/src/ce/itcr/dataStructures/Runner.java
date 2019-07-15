package ce.itcr.dataStructures;

import java.util.Scanner;
import ce.itcr.dataStructures.linkedList.LinkedListInterface;

public class Runner {
    public static void main(String[] args){
        boolean running = true;
        while (running){
            System.out.println("Insert: \n" +
                               "1. To execute Linked List Test,\n" +
                               "2. To execute Queue Test,\n" +
                               "3. To execute Stack Test,\n" +
                               "4. To exit the loop.");
            Scanner scanner = new Scanner(System.in);
            int opt = scanner.nextInt();
            if(opt == 1){
                LinkedListInterface llinterface = new LinkedListInterface();
                llinterface.linkedListRunner();
            } else if(opt == 2){

            } else if(opt == 3){

            } else if(opt == 4){
                running = false;
            } else{
                System.out.println("Insert valid option.");
            }


        }
    }
}
