/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    int length(ListNode head){
        int l=0;
        while(head!=null){
            l+=1;
            head=head.next;
        }
        return l;
    }
    public ListNode[] splitListToParts(ListNode head, int k) {
        
        ArrayList<ListNode>sol=new ArrayList<ListNode>();
        int len=length(head);
        ArrayList<Integer>cnt=new ArrayList<>();
        int div=len/k;
        int mod=len%k;
        for(int i=0;i<mod;i++){
            cnt.add(div+1);
        }
        for(int i=0;i<k-mod;i++){
            cnt.add(div);
        }

        ListNode temp=head;
        int loc=0;
        ListNode bs=temp;
        for(int i:cnt){
            while(loc!=i){
                temp=bs;
                bs=bs.next;
                loc+=1;
            }
            if(temp!=null)
            temp.next=null;
            if(head!=null){
                sol.add(head);
                head=bs;
                temp=bs;
            }
            else{
                sol.add(null);
            }
            loc=0;
        }
        while(sol.size()<k){
            sol.add(null);
        }
        return sol.toArray(new ListNode[0]);

    }
}