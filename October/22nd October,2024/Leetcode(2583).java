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
    public long kthLargestLevelSum(TreeNode root, int k) {
        ArrayList<Long>res=new ArrayList<>();
        LinkedList<TreeNode>q=new LinkedList<TreeNode>();
        q.add(root);
        while(!q.isEmpty()){
            int n=q.size();
            long s=0;
            for(int i=0;i<n;i++){
                TreeNode temp=q.poll();
                s+=temp.val;
                if(temp.left!=null) q.add(temp.left);
                if(temp.right!=null) q.add(temp.right);
            }
            res.add(s);
        }
        res.sort(Collections.reverseOrder());
        if(res.size()<k) return -1;
        return res.get(k-1);
    }
}