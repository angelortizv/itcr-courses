package ce.itcr.dataStructures.trees;

public class AVLInterface {
    public void AVLInterfaceRun(){
        AVLTree tree = new AVLTree();

        tree.add("Angelo");
        tree.add("Rossy");
        tree.add("Alex");
        tree.add("David");
        tree.add("Cristian");
        tree.add("Juanchin");

        tree.showingInOrder(tree.Root);
        tree.showingPreOrder(tree.Root);

        tree.delete("Juanchin");
        tree.search(tree.Root, "Angelo");
        tree.delete("Alex");

        tree.showingInOrder(tree.Root);
        tree.showingPreOrder(tree.Root);
    }
}
