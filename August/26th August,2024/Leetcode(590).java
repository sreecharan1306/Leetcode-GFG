/*
// Definition for a Node.
class Node {
    public int val;
    public List<Node> children;

    public Node() {}

    public Node(int _val) {
        val = _val;
    }

    public Node(int _val, List<Node> _children) {
        val = _val;
        children = _children;
    }
};
*/

class Solution {
    void postorder(Node root,List<Integer>arr){
        if(root==null) return;
        for(Node c:root.children){
            postorder(c,arr);
        }
        arr.add(root.val);
    }
    public List<Integer> postorder(Node root) {
        List<Integer>arr=new ArrayList<Integer>();
        postorder(root,arr);
        return arr;
    }
}