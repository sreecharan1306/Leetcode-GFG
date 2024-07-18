/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    int ans=0;
    int dist;
    vector<int> dfs(TreeNode* root){
        if(!root) return {};
        if(root->left ==nullptr && root->right==nullptr) return {1};
        vector<int> ll=dfs(root->left);
        vector<int>rl=dfs(root->right);

        for(int i:ll){
            for(int j:rl){
                if((i+j)<=dist){
                    ans+=1;
                }
            }
        }
        vector<int>al;
        al.reserve(ll.size() + rl.size());
        merge(ll.begin(),ll.end(),rl.begin(),rl.end(),back_inserter(al));
        for(int i=0;i<al.size();i++){
            al[i]+=1;
        }
        return al;
    }
    int countPairs(TreeNode* root, int distance) {
        dist=distance;
        dfs(root);

        return ans;
    }
};