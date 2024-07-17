
class Solution {
public:
    vector<TreeNode*>sol;
    unordered_map<int,bool>todel;
    void solve(TreeNode* &root){
        if(root->left){
            solve(root->left);
        }
        if(root->right){
            solve(root->right);
        }
        if(todel[root->val]){
            if(root->left) sol.push_back(root->left);
            if(root->right) sol.push_back(root->right);
            root=nullptr;
            delete root;
            return;
        }
        else{
            return;
        }
    }
    vector<TreeNode*> delNodes(TreeNode* root, vector<int>& to_delete) {
        // vector<TreeNode*>sol;
        
        // unordered_map<int,bool>todel;
        for(int i:to_delete){
            todel[i]=true;
        }
        solve(root);
        if(root)
        sol.push_back(root);
        return sol;
        
    }
};