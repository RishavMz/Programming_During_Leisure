package DSA;

class BNode
{
    protected int data;
    protected BNode left;
    protected BNode right;

    BNode()
    {
        data = 0;
        left = null;
        right = null;
    }
}

class BinarySearchTree extends BNode
{
    BNode root;
    BinarySearchTree()
    {
        root = null;
    }

    public void insert(int value)
    {
        BNode newnode = new BNode();
        newnode.data = value;
        if(root == null)
        {
            root = newnode;

        }
        else
        {
            BNode temp = new BNode();
            temp = root;
            while(true)
            {
                if(value <= temp.data)
                {
                    if(temp.left == null)
                    {   
                        temp.left = newnode;
                        break;
                    }
                    else
                    {
                        temp = temp.left;
                        continue;
                    }    
                }
                else
                {
                    if(temp.right == null)
                    {
                        temp.right = newnode;
                        break;
                    }
                    else
                    {
                        temp = temp.right;
                        continue;
                    }
                }
            }
        }
    }

    void preorder(BNode n)
    {
        System.out.print(n.data + " ");
        if(n.left != null)
        {
            preorder(n.left);
        }
        if(n.right != null)
        {
            preorder(n.right);
        }
    }

    void inorder(BNode n)
    {
        if(n.left != null)
        {
            inorder(n.left);
        }
        System.out.print(n.data + " ");
        if(n.right != null)
        {
            inorder(n.right);
        }
    }

    void postorder(BNode n)
    {
        if(n.left != null)
        {
            postorder(n.left);
        }
        if(n.right != null)
        {
            postorder(n.right);
        }
        System.out.print(n.data + " ");
    }

    void reverse(BNode n)
    {
        BNode temp = new BNode();
        if(n.left != null && n.right != null)
        {
            temp = n.left;
            n.left = n.right;
            n.right = temp;
            reverse(n.left);
            reverse(n.right);
        }
        else if(temp.left == null && temp.right != null)
        {
            temp.left = temp.right;
            temp.right = null;
            reverse(n.left);
        }
        else if(temp.right == null && temp.left != null)
        {
            temp.right = temp.left;
            temp.left = null;
            reverse(n.left);
        }
        
    }


    public static void main(String args[])
    {
        BinarySearchTree btree = new BinarySearchTree();
        
        btree.insert(5);
        btree.insert(3);
        btree.insert(7);
        btree.insert(2);
        btree.insert(6);
        btree.insert(4);
        btree.insert(8);
        btree.preorder(btree.root);
        System.out.println("Pre Order");
        btree.inorder(btree.root);
        System.out.println("In order");
        btree.postorder(btree.root);
        System.out.println("Post order");
        System.out.println("Reversed inorder");
        btree.reverse(btree.root);
        btree.inorder(btree.root);
    }
}