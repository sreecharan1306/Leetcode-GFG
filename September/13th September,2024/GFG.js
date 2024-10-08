

// User function Template for javascript

/**
 * @param {Node} node
*/

/*
class Node{
    constructor(data){
        this.data = data;
        this.left = null;
        this.right = null;
    }
}
*/

class Solution {
    // Function to convert a binary tree into its mirror tree.
    mirror(node) {
        // your code here
        if(!node) return;
        
        let temp=node.left;
        node.left=node.right;
        node.right=temp;
        this.mirror(node.left);
        this.mirror(node.right);
    }
}