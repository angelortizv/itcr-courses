package ce.itcr.dataStructures.graphs;

public class GraphInterface {
    public void interfaceRUn(){
        Graph gr = new Graph();
        gr.addVertex("bob","arun");
        gr.addVertex("kiran","arun");
        gr.addVertex("bob","kiran");
        gr.addVertex("bob","anie");
        gr.addVertex("bob","kunju");
    }
}
