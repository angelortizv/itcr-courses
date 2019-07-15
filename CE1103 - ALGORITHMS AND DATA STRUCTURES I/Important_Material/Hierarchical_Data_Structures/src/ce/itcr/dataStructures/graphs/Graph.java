package ce.itcr.dataStructures.graphs;

import java.util.ArrayList;
import java.util.Iterator;
import java.util.LinkedList;
import java.util.List;
class Graph{
    ArrayList<Vertex> graphDS;
    public Graph() {

        graphDS=new ArrayList<Vertex>();

    }
    public void addVertex(String key, String value) {
        Vertex keyVertex;
        Vertex valueVertex;
        keyVertex=getNode(key);
        if(keyVertex!=null) {
            keyVertex.adjList.add(new Vertex(value));
        }
        else {
            keyVertex=new Vertex(key);
            keyVertex.adjList.add(new Vertex(value));
            graphDS.add(keyVertex);
        }
        valueVertex=getNode(value);
        if(valueVertex!=null) {
            valueVertex.adjList.add(new Vertex(key));//check if already the entry is there
        }else {
            valueVertex=new Vertex(key);
            valueVertex.adjList.add(new Vertex(value));
            graphDS.add(valueVertex);
        }


    }
    private Vertex getNode(String value) {
        Iterator<Vertex> it = graphDS.iterator();
        while(it.hasNext()) {
            Vertex v = it.next();
            if(v.word.equalsIgnoreCase(value)) {
                return v;
            }
        }
        return null;
    }

}

class Vertex{
    String word;
    LinkedList<Vertex> adjList;
    public Vertex(String word) {
        this.word = word;
        adjList=new LinkedList<Vertex>();
    }

}