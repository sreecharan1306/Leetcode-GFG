/**
 * Definition for a binary tree node.
 * public class TreeNode {
 * int val;
 * TreeNode left;
 * TreeNode right;
 * TreeNode() {}
 * TreeNode(int val) { this.val = val; }
 * TreeNode(int val, TreeNode left, TreeNode right) {
 * this.val = val;
 * this.left = left;
 * this.right = right;
 * }
 * }
 */
class Solution {
    public TreeNode reverseOddLevels(TreeNode root) {
        Queue<TreeNode> q=new LinkedList<>();
        q.offer(root);
        int lvl = 0;
        ArrayList<Integer> temp=new ArrayList<>();
        while (!q.isEmpty()) {
            int n = q.size();
            if (lvl %2 ==1 ) {
                for (int i = 0; i < n; i++) {
                    TreeNode t = q.peek();
                    q.poll();
                    t.val=temp.get(i);
                    if (t.left!=null) q.add(t.left);
                    if (t.right!=null) q.add(t.right);
                }
                temp.clear();
            } else {
                for (int i = 0; i < n; i++) {
                    TreeNode t = q.peek();
                    q.poll();
                    if (t.left!=null) {
                        q.add(t.left);
                        temp.add(t.left.val);
                    }
                    if (t.right!=null) {
                        q.add(t.right);
                        temp.add(t.right.val);
                    }
                }
                Collections.reverse(temp);
            }
            lvl++;
        }
        return root;
    }
}