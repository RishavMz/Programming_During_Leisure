package DSA;

import java.util.*;

class Node<T>                   	    // declare Node array class
{
    T data;
    Node<T> next;

    Node()
    {
        data = null;
        next = null;
    }
}
public class linkedlist<T>              // Declare linkedlist class
{
    Node<T> head;

    linkedlist()
    {
        head = null;
    }
    public String traverse()            // Traverse the linked list
    {
        Node<T> temp = new Node<T>();
        temp = head;
        if(temp == null)
        {
            return "Empty list";
        }
        String s = "";
        while(true)
        {
            s = s + temp.data;
            if(temp.next != null)
            {
                temp = temp.next;
            }            
            else
            {
                break;
            }
        }
        return s;
    }

    public void addBeginning(T value)       // Add a node to beginning of the linked list
    {
        Node<T> newnode = new Node<T>();
        newnode.data = value;
        if (head == null)
        {
            head = newnode;
        }
        else
        {
            newnode.next = head;
        }
        head = newnode;
    }

    public void addEnd(T value)                 // Add a node to end of the linked list
    {
        Node<T> newnode = new Node<T>();
        newnode.data = value;
        if(head == null)
        {
            head = newnode;
        }
        else
        {
            Node<T> temp = new Node<T>();
            temp = head;
            while(temp.next != null)
            {
                temp = temp.next;
            }
            temp.next = newnode;
        }
    }

    public void deleteBeginning()                   // Delete the node at beginning of the linked list
    {
        if(head == null)
        {
            System.out.println("Cannot delete: list already empty");
        }
        else
        {
            Node<T> temp = new Node<T>();
            temp = head;
            head = head.next;
            temp.data = null;
            temp.next = null;
            temp = null;
        }
    }

    public void deleteEnd()                         // Delete a node at end of he linked list
    {
        if (head == null)
        {
            System.out.println("Cannot delete: list already empty");
        }
        else
        {
            if(head.next == null)
            {
                head.data = null;
                head = null;
            }
            else
            {
                Node<T> temp = new Node<T>();
                temp = head;
                while(temp.next.next != null)
                {
                    temp = temp.next;
                }
                temp.next.data = null;
                temp.next = null;
            }  
        }
    }

    public int count()                              // Count the number of nodes in linked list
    {
        int count = 0;
        Node<T> temp = new Node<T>();
        temp = head;
        while(temp != null)
        {
            count++;
            temp = temp.next;
        }
        return count;
    }

    public void reverse()                           // Reverse the linked list
    {
        if (this.count() == 0)
        {
            System.out.println("Error: Cannot reverse empty list");
        }
        else if(this.count() == 1)
        {
            return;
        }
        else if(this.count() == 2)
        {
            head.next.next = head;
            head = head.next;
            head.next.next = null;
        }
        else 
        {
            Node<T> pointer1 = new Node<T>();
            Node<T> pointer2 = new Node<T>();
            Node<T> pointer3 = new Node<T>();
            pointer1 = head;
            pointer2 = head.next;
            pointer3 = pointer2.next;
            pointer1.next = null;
            while(pointer3 != null)
            {
                pointer2.next = pointer1;
                pointer1 = pointer2;
                pointer2 = pointer3;
                pointer3 = pointer3.next;
            }
            pointer2.next = pointer1;
            head = pointer2;
        }
    }


    public static void main(String args[])
    {
        Scanner sc = new Scanner(System.in);
        linkedlist<Integer> ll = new linkedlist<Integer>();
        int ch , val;
        boolean run = true;
        while(run)
        {
            System.out.println("Enter your choice: ");
            System.out.println("0: Traverse through the linked list");
            System.out.println("1: Add element at beginning of the linked list");
            System.out.println("2. Add element at the end of the linked list");
            System.out.println("3. Remove element at beginning of the linked list");
            System.out.println("4. Remove element at end of the linked list");
            System.out.println("5. Count number of nodes in the linked list");
            System.out.println("6. Reverse the linked list");
            System.out.println("7. Exit");

            ch = sc.nextInt();
            switch (ch)
            {
                case 0:
                    System.out.println(ll.traverse());
                    break;
                case 1:
                    System.out.print("Enter value: ");
                    val = sc.nextInt();
                    ll.addBeginning(val);
                    break;
                case 2:
                    System.out.print("Enter value: ");
                    val = sc.nextInt();
                    ll.addEnd(val);
                    break;
                case 3:
                    ll.deleteBeginning();
                    break;
                case 4:
                    ll.deleteEnd();
                    break;
                case 5:
                    System.out.println(ll.count());
                    break;
                case 6:
                    ll.reverse();
                    break;
                case 7:
                    run = false;
                    break;
                default:
                    System.out.println("Wrong choice!!!!!!!");
            }
        }
        sc.close();
    }
}
