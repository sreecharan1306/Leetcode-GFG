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
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    boolean check(ListNode n,TreeNode t){
        // bool a=false,b=false;
        if(n==null) return true;
        if(t==null || t.val!=n.val) return false;
        // check(n.next,t.left);
        
        return (check(n.next,t.right) || check(n.next,t.left));
    }
    public boolean isSubPath(ListNode head, TreeNode root) {
        if(head==null) return true;
        if(root==null) return false;
        // if(head.val!=root.val) return false;
        return check(head,root)||isSubPath(head,root.left) || isSubPath(head,root.right);
    }
}