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
    public void dfs(TreeNode root, int sval, ArrayList<Integer> arrsum, int lvl) {
        if (root == null)
            return;
        root.val=arrsum.get(lvl)-sval;
        int p=0;
        if(root.left!=null) p+=root.left.val;
        if(root.right!=null) p+=root.right.val;
        if(root.left!=null){
            dfs(root.left,p,arrsum,lvl+1);
        }
        if(root.right!=null) {
            dfs(root.right,p,arrsum,lvl+1);
        }
    }

    public TreeNode replaceValueInTree(TreeNode root) {
        LinkedList<TreeNode> q = new LinkedList<>();
        ArrayList<Integer> arrsum = new ArrayList<>();
        q.push(root);
        while (!q.isEmpty()) {
            int n = q.size();
            int s = 0;
            for (int i = 0; i < n; i++) {
                TreeNode temp = q.poll();
                s += temp.val;
                if (temp.left != null)
                    q.add(temp.left);
                if (temp.right != null)
                    q.add(temp.right);
            }
            arrsum.add(s);
        }
        for (int i : arrsum)
            System.out.println(i);

        dfs(root, arrsum.get(0), arrsum, 0);

        return root;
    }
}