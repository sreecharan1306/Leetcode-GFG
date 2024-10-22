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
    long long kthLargestLevelSum(TreeNode* root, int k) {
        // int ans=root->val;
        vector<long long int>res;
        priority_queue<long long int>pq;
        queue<TreeNode*>q;
        q.push(root);
        while(!q.empty()){
            int n=q.size();
            long long int s=0;
            for(int i=0;i<n;i++){
                TreeNode* temp=q.front();
                s+=temp->val;
                if(temp->left) q.push(temp->left);
                if(temp->right) q.push(temp->right);
                q.pop();
            }
            // ans=max(ans,s);
            pq.push(s);
            // res.push_back(s);
        }
        // for(int i:res) cout<<i<<"  ";
        // sort(res.rbegin(),res.rend());
        if(pq.size()<k) return -1;
        
        while(--k) pq.pop();
        return pq.top();
        return res[k-1];
        // return ans;
    }
};