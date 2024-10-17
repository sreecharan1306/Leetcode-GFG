//{ Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

struct Node {
    int data;
    struct Node* next;

    Node(int x) {
        data = x;
        next = NULL;
    }
};


// } Driver Code Ends
/*
struct Node
{
    int data;
    struct Node* next;

    Node(int x){
        data = x;
        next = NULL;
    }

};
*/

class Solution {
  public:
    // Function to split a linked list into two lists alternately
    vector<Node*> alternatingSplitList(struct Node* head) {
        // Your code here
        vector<Node*>sol;
        // Node* temp=head;
        // Node* bs=new Node(-1);
        // Node* d1=bs;
        // while(temp && temp->next){
        //     d1->next=temp;
        //     d1=d1->next;
        //     temp=temp->next->next;
        // }
        // sol.push_back(bs->next);
        // Node* bs2=new Node(-1);
        // Node* d2=bs2;
        // temp=head->next;
        // while(temp && temp->next){
        //     d2->next=temp;
        //     d2=d2->next;
        //     temp=temp->next->next;
        // }
        // sol.push_back(bs2->next);
        Node* d1=new Node(-1);
        Node* l1=d1;
        
        Node* d2=new Node(-1);
        Node* l2=d2;
        Node* temp=head;
        while(temp){
            if(!temp) break;
            Node* bs=temp;
            l1->next=bs;
            l1=l1->next;
            temp=temp->next;
            if(!temp) break;
            Node* bs2=temp;
            l2->next=bs2;
            l2=l2->next;
            temp=temp->next;
        }
        l1->next=nullptr;
        l2->next=nullptr;
        sol.push_back(d1->next);
        sol.push_back(d2->next);
        return sol;
    }
};


//{ Driver Code Starts.

void printList(struct Node* node) {
    while (node != NULL) {
        cout << node->data << " ";
        node = node->next;
    }
    cout << endl;
}

int main() {
    int t;
    cin >> t;
    cin.ignore();

    while (t--) {
        vector<int> arr;
        string input;
        getline(cin, input);
        stringstream ss(input);
        int number;

        while (ss >> number) {
            arr.push_back(number);
        }

        struct Node* head = new Node(arr[0]);
        struct Node* tail = head;

        for (int i = 1; i < arr.size(); ++i) {
            tail->next = new Node(arr[i]);
            tail = tail->next;
        }

        Solution ob;
        vector<Node*> result = ob.alternatingSplitList(head);
        printList(result[0]);
        printList(result[1]);
    }

    return 0;
}

// } Driver Code Ends