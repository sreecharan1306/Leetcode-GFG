/**
 * Definition for a binary tree node.
 * function TreeNode(val, left, right) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.left = (left===undefined ? null : left)
 *     this.right = (right===undefined ? null : right)
 * }
 */
/**
 * @param {TreeNode} root
 * @param {number} k
 * @return {number}
 */
var kthLargestLevelSum = function(root, k) {
    let res=[];
    let q=[];
    q.push(root);
    while(q.length>0){
        let n=q.length;
        let s=0;
        for(let i=0;i<n;i++){
            let temp=q.shift();
            s+=temp.val;
            if(temp.left) q.push(temp.left);
            if(temp.right) q.push(temp.right);
        }
        res.push(s);
    }
    res.sort((a,b)=>(b-a));
    // sort(res.rbegin(),res.rend());
    if(res.length<k) return -1;
    return res[k-1];
};