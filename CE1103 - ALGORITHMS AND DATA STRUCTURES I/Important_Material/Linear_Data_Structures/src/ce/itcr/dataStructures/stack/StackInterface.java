package ce.itcr.dataStructures.stack;

public class StackInterface {
    public void StackRunner(){
        Stack stackTest = new Stack();
        stackTest.push(10);
        stackTest.push(230);
        stackTest.print();
        stackTest.pop();
        stackTest.print();
    }
}
