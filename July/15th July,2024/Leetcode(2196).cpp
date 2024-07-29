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
    TreeNode* createBinaryTree(vector<vector<int>>& descriptions) {
        unordered_map<int, TreeNode*> mp;
        map<int, int> child, parent;

        for (auto i : descriptions) {
            child[i[1]]++;
            parent[i[0]]++;
            TreeNode *p, *c;
            if (mp.find(i[0]) == mp.end())
                p = new TreeNode(i[0]);
            else {
                p = mp[i[0]];
            }
            if (mp.find(i[1]) == mp.end())
                c = new TreeNode(i[1]);
            else {
                c = mp[i[1]];
            }
            if (i[2] == 1) {
                p->left = c;
            } else {
                p->right = c;
            }
            mp[i[0]] = p;
            mp[i[1]] = c;
        }
        for (auto i : parent) {
            if (child[i.first] == 0) {
                return mp[i.first];
            }
        }
        return nullptr;
    }
};