//{ Driver Code Starts
import java.io.*;
import java.util.*;

class Node {
    int data;
    Node next;

    Node(int x) {
        data = x;
        next = null;
    }
}

class LinkedList {
    // Function to print nodes in a given circular linked list
    static void printList(Node head) {
        if (head == null) {
            System.out.println("empty");
            return;
        }
        Node temp = head;
        do {
            System.out.print(temp.data + " ");
            temp = temp.next;
        } while (temp != head);
        System.out.println();
    }

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());

        while (t-- > 0) {
            List<Integer> arr = new ArrayList<>();
            String input = br.readLine();
            StringTokenizer st = new StringTokenizer(input);
            while (st.hasMoreTokens()) {
                arr.add(Integer.parseInt(st.nextToken()));
            }
            int key = Integer.parseInt(br.readLine());
            Node head = new Node(arr.get(0));
            Node tail = head;
            for (int i = 1; i < arr.size(); ++i) {
                tail.next = new Node(arr.get(i));
                tail = tail.next;
            }
            tail.next = head; // Make the list circular
            Solution ob = new Solution();
            Node current = ob.deleteNode(head, key);
            Node rev = ob.reverse(current);
            printList(rev);
        }
    }
}

// } Driver Code Ends


/*class Node
{
    int data;
    Node next;
    Node(int d)
    {
        data=d;next=null;
    }
}*/

class Solution {
    // Function to reverse a circular linked list
    Node reverse(Node head) {
        // code here
         if(head==null) return null;
        Node curr=head,next=null,pre=null;
        do{
            next=curr.next;
            curr.next=pre;
            pre=curr;
            curr=next;
        }while(curr!=head);
        
        head.next=pre;
        return pre;       
        
    }

    // Function to delete a node from the circular linked list
    Node deleteNode(Node head, int key) {
        // code here
        if(head.data==key){ 
            if(head.next==head) return null;
            else{
                Node temp=head;
                while(temp.next!=head){
                    temp=temp.next;
                }
                temp.next=head.next;
                return head.next;
            }
        }
        Node temp=head.next;
        Node bs=temp;
        while (temp!=head){
            if(temp.data==key){
                bs.next=temp.next;
                if(temp==head.next) head.next=temp.next;
                return head;
            }
            bs=temp;
            temp=temp.next;
        }
        // if(temp.next==head){
        //     bs.next=head;
        // }
        // else{
        //     bs.next=temp.next;
        // }
        return head;
    }
    
}