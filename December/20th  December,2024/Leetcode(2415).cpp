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
    TreeNode* reverseOddLevels(TreeNode* root) {
        queue<TreeNode*> q;
        q.push(root);
        int lvl = 0;
        vector<int> temp;
        while (!q.empty()) {
            int n = q.size();
            if (lvl & 1) {
                for (int i = 0; i < n; i++) {
                    TreeNode* t = q.front();
                    q.pop();
                    t->val=temp[i];
                    if (t->left) {
                        q.push(t->left);
                    }
                    if (t->right) {
                        q.push(t->right);
                    }
                }
                temp.clear();
            } else {

                for (int i = 0; i < n; i++) {
                    TreeNode* t = q.front();
                    q.pop();
                    if (t->left) {
                        q.push(t->left);
                        temp.push_back(t->left->val);
                    }
                    if (t->right) {
                        q.push(t->right);
                        temp.push_back(t->right->val);
                    }
                }
                reverse(temp.begin(),temp.end());
            }
            lvl++;
        }
        return root;
    }
};