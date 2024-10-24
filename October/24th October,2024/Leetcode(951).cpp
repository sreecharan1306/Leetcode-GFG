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

    void dfs(TreeNode* root,map<int,int>&mp){
        if(root==nullptr) return;
        int s=0;
        if(root->left) s+=(root->left->val);
        if(root->right) s+=(root->right->val);
        mp[root->val]=s;
        if(root->left) dfs(root->left,mp);
        if(root->right) dfs(root->right,mp);
    }
    bool flipEquiv(TreeNode* root1, TreeNode* root2) {
        if((root1==nullptr) || (root2==nullptr)){
            return root1==root2;
        }
        map<int,int>mp1;
        map<int,int>mp2;
        dfs(root1,mp1);
        dfs(root2,mp2);
        for(auto i:mp1){
            cout<<i.first<<"  "<<i.second<<endl;
        }
        cout<<endl;
        for(auto i:mp2){
            cout<<i.first<<"  "<<i.second<<endl;
        }
        if(mp1.size()!=mp2.size()) return false;
        queue<TreeNode*>q;
        q.push(root1);
        while(!q.empty()){
            int n=q.size();
            for(int i=0;i<n;i++){
                TreeNode* temp=q.front();
                q.pop();
                int v=temp->val;
                if(mp1[v]!=mp2[v]) return false;
                if(temp->left) q.push(temp->left);
                if(temp->right) q.push(temp->right);
            }
        }
        return true;
    }
};