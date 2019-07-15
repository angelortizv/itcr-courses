package ce.itcr.dataStructures;

import ce.itcr.dataStructures.graphs.GraphInterface;
import ce.itcr.dataStructures.trees.AVLInterface;

import java.util.Scanner;

public class Runner {
    public static void main(String[] args){
        boolean running = true;
        while (running){
            System.out.println("Insert: \n" +
                    "1. To execute Graph Test,\n" +
                    "2. To execute AVL Tree,\n" +
                    "3. To execute Heap Test,\n" +
                    "4. To exit the loop.");
            Scanner scanner = new Scanner(System.in);
            int opt = scanner.nextInt();
            if(opt == 1){
                GraphInterface graphInterface = new GraphInterface();
                graphInterface.interfaceRUn();
            } else if(opt == 2){
                AVLInterface avlInterface = new AVLInterface();
                avlInterface.AVLInterfaceRun();
            } else if(opt == 3){

            }else if(opt == 4){
                running = false;
            } else{
                System.out.println("Insert valid option.");
            }


        }
    }
}
