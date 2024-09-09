/**
 * Definition for singly-linked list.
 * public class ListNode {
 * int val;
 * ListNode next;
 * ListNode() {}
 * ListNode(int val) { this.val = val; }
 * ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public int[][] spiralMatrix(int m, int n, ListNode head) {
        int[][] mat = new int[m][n];
        int rb = 0, cb = 0, re = m - 1, ce = n - 1;
        int data;
        while (rb <= re && cb <= ce) {
            for (int i = cb; i <= ce; i++) {
                if (head != null) {
                    mat[rb][i] = head.val;
                    head = head.next;

                } else
                    mat[rb][i] = -1;
            }
            rb++;
            for (int i = rb; i <= re; i++) {
                if (head != null) {
                    mat[i][ce] = head.val;

                    head = head.next;
                } else
                    mat[i][ce] = -1;
            }
            ce--;
            if (rb <= re) {

                for (int i = ce; i >= cb; i--) {
                    if (head != null) {
                        mat[re][i] = head.val;
                        head = head.next;
                    } else
                        mat[re][i] = -1;
                }
                re--;
            }
            if (cb <= ce) {

                for (int i = re; i >= rb; i--) {
                    if (head != null) {
                        mat[i][cb] = head.val;
                        head = head.next;
                    } else
                        mat[i][cb] = -1;
                }
                cb++;
            }
        }
        return mat;
    }
}