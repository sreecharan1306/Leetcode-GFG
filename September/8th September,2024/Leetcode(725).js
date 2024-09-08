/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} k
 * @return {ListNode[]}
 */
var splitListToParts = function(head, k) {
    let ans=[]
    let temp=head;
    let len=0;
    while(temp){
        len+=1;
        temp=temp.next;
    }
    let div=Math.floor(len/k);
    let mod=len%k;
    let cnt=[];
    for(let i=0;i<mod;i++){
        cnt.push(Math.floor(div+1))
    }
    for(let i=0;i<k-mod;i++){
        cnt.push(div)
    }
    console.log(cnt)
    temp=head;
    let bs=temp;
    let loc=0;
    for(let i=0;i<k;i++){
        while(loc!=cnt[i]){
            temp=bs;
            bs=bs.next;
            loc+=1;
        }
        if(temp) temp.next=null;
        if(head){
            ans.push(head);
            head=bs;
            temp=bs;
        }
        else{
            ans.push(null)
        }
        loc=0;
    }
    return ans;
};