/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left),
 * right(right) {}
 * };
 */
class Solution {
public:


    vector<char> path(TreeNode* root,vector<char>&temp,int tv){
        if(root==NULL) return {};
        if(root->val==tv) return temp;
        temp.push_back('L');
        vector<char>res=path(root->left,temp,tv);
        if(res.size()>0) return res;
        temp.pop_back();
        temp.push_back('R');
        res=path(root->right,temp,tv);
        if(res.size()>0) return res;
        temp.pop_back();
        return {};
    }
    string getDirections(TreeNode* root, int startValue, int destValue) {
        vector<char> sp,ep;
        path(root,sp,startValue);
        path(root,ep,destValue);
        int i=0;
        string ans="";
        while(i<min(sp.size(),ep.size())){
            if(sp[i]!=ep[i]){
                break;
            }
            i++;
        }
        for(int j=i;j<sp.size();j++){
            ans+="U";
        }
        for(int j=i;j<ep.size();j++){
            ans+=ep[j];
        }
        return ans;
    }
};