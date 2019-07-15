package ce.itcr.dataStructures.trees;

public class Node
{
    String name;
    int height;
    Node left;
    Node right;

    public Node()
    {
        this.name = new String("Value");
        this.height = 1;
        this.left = null;
        this.right = null;
    }

    public Node(String name)
    {
        this.name = new String(name);
        this.height = 1;
        this.left = null;
        this.right = null;
    }
}
