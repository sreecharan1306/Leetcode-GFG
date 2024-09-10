/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {ListNode}
 */
function gcd(a, b) {
    let smaller = Math.min(a, b);
    let hcf = 1;
 
    for (let i = 1; i <= smaller; i++) {
        if (a % i === 0 && b % i === 0) {
            hcf = i;
        }
    }
 
    return hcf;
}
var insertGreatestCommonDivisors = function(head) {
    let temp=head.next;
    let curr=head;
    if(!head || !head.next) return head;
    while(temp){
        let x=gcd(temp.val,curr.val);
        let nn=new ListNode(x,temp);
        curr.next=nn
        curr=temp
        temp=temp.next
    }
    return head;
};