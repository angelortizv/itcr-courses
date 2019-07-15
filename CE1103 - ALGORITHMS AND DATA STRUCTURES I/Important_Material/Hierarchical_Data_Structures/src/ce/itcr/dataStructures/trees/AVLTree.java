package ce.itcr.dataStructures.trees;

import java.lang.StringBuilder;
import java.util.Stack;

public class AVLTree
{
    static Node Root;

    int getHeight(Node key)
    {
        if (key == null)
            return 0;

        else
            return key.height;
    }

    int getBalance(Node key)
    {
        if (key == null)
            return 0;

        else
            return (getHeight(key.right) - getHeight(key.left));
    }

    void updateHeight(Node key)
    {
        int leftSubtreeHeight = getHeight(key.left);
        int rightSubtreeHeight = getHeight(key.right);

        key.height = Math.max(leftSubtreeHeight , rightSubtreeHeight) + 1;
    }

    Node rotateLeft(Node oldRoot)
    {
        Node newRoot = oldRoot.right;
        Node temp = newRoot.left;

        newRoot.left = oldRoot;
        oldRoot.right = temp;

        updateHeight(oldRoot);
        updateHeight(newRoot);

        return newRoot;
    }

    Node rotateRight(Node oldRoot)
    {
        Node newRoot = oldRoot.left;
        Node temp = newRoot.right;

        newRoot.right = oldRoot;
        oldRoot.left = temp;

        updateHeight(oldRoot);
        updateHeight(newRoot);

        return newRoot;
    }

    Node balanceTree(Node root)
    {
        updateHeight(root);

        int balance = getBalance(root);

        if (balance == 2)
        {
            if (getBalance(root.right) < 0)
                root.right = rotateRight(root.right);

            return rotateLeft(root);
        }

        if (balance == -2)
        {
            if (getBalance(root.left) > 0)
                root.left = rotateLeft(root.left);

            return rotateRight(root);
        }

        return root;
    }

    Node insertNode(Node root, String key)
    {
        if (root == null)
            return new Node(key);

        else if (key.compareToIgnoreCase(root.name) < 0)
            root.left = insertNode(root.left, key);

        else
            root.right = insertNode(root.right, key);

        return balanceTree(root);
    }

    Node findSuccessor(Node root)
    {
        if (root.left != null)
            return findSuccessor(root.left);

        else
            return root;
    }

    Node removeNode(Node root, String key)
    {
        if (root == null)
            return root;

        else if (key.compareToIgnoreCase(root.name) < 0)
            root.left = removeNode(root.left, key);

        else if (key.compareToIgnoreCase(root.name) > 0)
            root.right = removeNode(root.right, key);

        else
        {
            if (root.right == null)
                root = root.left;

            else if (root.left == null)
                root = root.right;

            else
            {
                Node temp = findSuccessor(root.right);
                root.name = temp.name;
                root.right = removeNode(root.right, root.name);
            }
        }

        if (root == null)
            return root;

        else
            return balanceTree(root);
    }

    Node search(Node root, String key)
    {
        if (root == null || key.compareToIgnoreCase(root.name) == 0)
            return root;

        if (key.compareTo(root.name) < 0)
            return search(root.left, key);

        else
            return search(root.right, key);
    }

    void add(String key)
    {
        if (search(Root , key) == null)
        {
            Root = insertNode(Root , key);
            System.out.println("\n" + key + " added successfully :)");
        }

        else
            System.out.println("\n" + key + " has been added :(");
    }

    void delete(String key)
    {
        if (search(Root , key) != null)
        {
            Root = removeNode(Root , key);
            System.out.println("\n" + key + " deleted successfully :)");
        }

        else
            System.out.println("\n" + key + " not found in AVL Tree :(");
    }


    int depth(String key)
    {
        Node temp = search(Root, key);

        if (temp == null)
            return -1;

        else
        {
            System.out.println("\n" + "The depth of " + key + " is : " + (Root.height - temp.height));
            return (Root.height - temp.height);
        }
    }


    void showingPreOrder(Node key)
    {
        System.out.print("\nPre-Order : ");
        Stack <Node> stack = new Stack<Node>();

        if (key == null)
            return;

        else
        {
            stack.push(key);

            while (!stack.empty())
            {
                key = stack.pop();
                System.out.print(key.name + " ");

                if (key.right != null)
                    stack.push(key.right);

                if (key.left != null)
                    stack.push(key.left);
            }
        }

        System.out.println();
    }


    void showingInOrder(Node key)
    {
        System.out.print("\nIn-Order  : ");
        Stack <Node> stack = new Stack <Node>();

        while (!stack.empty() || key != null)
        {
            if (key != null)
            {
                stack.push(key);
                key = key.left;
            }

            else
            {
                key = stack.pop();
                System.out.print(key.name + " ");
                key = key.right;
            }
        }

        System.out.println();
    }
}
