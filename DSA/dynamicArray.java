package DSA;
import java.util.*;

@SuppressWarnings("unchecked")  //Prevent warnings due to generics
public class dynamicArray<T>    // Declare dynamic array class
{
    int capacity;
    int size;
    T arr[];
    
    dynamicArray()
    {
        capacity = 10;
        arr = (T[]) new Object[capacity];   // Declare arrray of generic type
        size = 0;
    }
    
    dynamicArray(int cap)
    {
        arr = (T[]) new Object[cap];    // Declare array of generic type
        size = 0;
        capacity = cap;
    }

    public void add(T value)                    // Add an element to the array
    {
        if (size == capacity)
        {
            T brr[] = (T[]) new Object[capacity*2];
            for(int i=0; i<capacity; i++)
            {
                brr[i] = arr[i];
            }
            brr[size++] = value;
            arr = brr;
            capacity = capacity*2;
        }
        else 
        {
            arr[size++] = value;
        }
    }

    public void replace(int position, T value)      // Replace array element at a position with another value
    {
        if (position < capacity)
        {
            arr[position] = value;
        }
        else
        {
            System.out.println("ERROR: Position exceeds current size of array");
            System.exit(0);
        }
    }

    public void insert(int position, T value)       // Insert value in array at a given position
    {
        if (size == capacity-1)
        {
            T brr[] = (T[]) new Object[capacity*2];
            for(int i=0; i<capacity; i++)
            {
                brr[i] = arr[i];
            }
            capacity = capacity*2;
            for(int i=size; i>=position; i--)
            {
                brr[i+1] = arr[i];
            }
            brr[position] = value;
            arr = brr;
            size++;
        }
        else if (position > capacity)
        {
            System.out.println("Error: position exceeds current size of array");
            System.exit(0);
        }
        else
        {
            for(int i=size; i>=position; i--)
            {
                arr[i+1] = arr[i];
            }
            arr[position] = value;
            size++;
        }
    }

    public void removeAt(int position)      // Remove array element at a given position
    {
        if (position < capacity)
        {
            for(int i = position; i<size-1; i++)
            {
                arr[i] = arr[i+1];
            }    
            arr[--size] = null;
        }
        else 
        {
            System.out.println("Error: Position exceeds current size of the array");
            System.exit(0);
        }
    }

    public void remove(T value)     // Removes the first occurance of element from the array
    {
        int found = 0 , i = 0;
        for(i=0; i<size; i++)
        {
            if(arr[i] == value)
            {
                found = 1;
                break;
            }
        }
        if(found == 1)
        {
            for(int j = i; j<size; j++)
            {
                arr[j] = arr[j+1];
            }
            arr[--size] = null;
        }
        if (found == 0)
        {
            System.out.println("Error: Item to be deleted not present in array");
            System.exit(0);
        }
    }

    public int count(T value)         // Count number of occurances of an element in array
    {
        int c = 0;
        for(int i=0; i<size; i++)
        {
            if(arr[i] == value)
                c++;
        }
        return c;
    }
    
    public int indexOf(T value)         // Returns the index of element from the array
    {
        for(int i=0; i<= size ; i++)
        {
            if(arr[i] == value)
            {
                return i;
            }   
        }
        return -1;
    }

    public void clear()                 // Removes all elements from the array
    {
        for(int i=0; i<size; i++)
        {
            arr[i] = null;
        }
    }

    public String display()
    {
        if (size == 0)
        {
            return "Empty array";
        }
        else
        {
            String s = "";
            for(int i=0; i<size; i++)
            {
                s = s + " "+ (arr[i] == null ? "" : arr[i]);
            }
            return s;
        }
    }


    // ===================== Testing Code ======================================= //
    public static void main(String args[])
    {
        dynamicArray<Integer> darr = new dynamicArray<Integer>();
        Scanner sc = new Scanner(System.in);

        int inp;
        int pos;
        int val;
        boolean run = true;
        while(run)
        {
            System.out.println("Enter your choice: ");
            System.out.println("0: Show elements of the array");
            System.out.println("1: Add element to end of the array");
            System.out.println("2. Replace element at a given position");
            System.out.println("3. Insert element at a given position");
            System.out.println("4. Remove value at a given position");
            System.out.println("5. Remove first occurance of a value from the array");
            System.out.println("6. count all occurances of a value from the array");
            System.out.println("7. Find index of an element in the array");
            System.out.println("8. Clear all elements from the array");
            System.out.println("9. Exit");

            inp = sc.nextInt();
            switch (inp) {
                case 0:
                    System.out.println(darr.display());
                    break;
                case 1:
                    System.out.print("Enter the value: ");
                    val = sc.nextInt();
                    darr.add(val);
                    break;
                case 2:
                    System.out.print("Enter the position: ");
                    pos = sc.nextInt();
                    System.out.println("Enter the value: ");
                    val = sc.nextInt();
                    darr.replace(pos, val);
                    break;
                case 3:
                    System.out.print("Enter the position: ");
                    pos = sc.nextInt();
                    System.out.print("Enter the value: ");
                    val = sc.nextInt();
                    darr.insert(pos, val);
                    break;
                case 4:
                    System.out.print("Ener the position: ");
                    pos = sc.nextInt();
                    darr.removeAt(pos);
                    break;
                case 5:
                    System.out.print("Ener the value: ");
                    val = sc.nextInt();
                    darr.remove(val);
                    break;
                case 6:
                    System.out.print("Ener the value: ");
                    val = sc.nextInt();
                    darr.count(val);
                    break;    
                case 7:
                    System.out.print("Enter the value: ");
                    val = sc.nextInt();
                    System.out.println(darr.indexOf(val));
                    break;
                case 8:
                    darr.clear();
                    break;
                case 9:
                    run = false;
                    break;            
                default:
                    System.out.println("Wrong choice!!!!!!");
            }
        }
        sc.close();
    }
}
