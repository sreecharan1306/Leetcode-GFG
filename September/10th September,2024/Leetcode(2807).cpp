/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     ListNode *next;
 *     ListNode() : val(0), next(nullptr) {}
 *     ListNode(int x) : val(x), next(nullptr) {}
 *     ListNode(int x, ListNode *next) : val(x), next(next) {}
 * };
 */
class Solution {
public:

    ListNode* insertGreatestCommonDivisors(ListNode* head) {
        ListNode* curr=head;
        if(head->next==NULL){
            return head;
        }
        ListNode* temp=head->next;
        while(temp!=NULL){
            ListNode* x=new ListNode(__gcd(temp->val,curr->val),temp);
            curr->next=x;
            curr=temp;
            temp=temp->next;
        }        
        return head;
    }
};