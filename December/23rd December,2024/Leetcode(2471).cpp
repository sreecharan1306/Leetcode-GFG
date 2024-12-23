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
    int minswaps(vector<int> v) {
        vector<int> sv = v;
        sort(sv.begin(), sv.end());
        map<int, int> mp;
        int cnt = 0;
        for (int i = 0; i < sv.size(); i++)
            mp[sv[i]] = i;
        vector<bool> visited(v.size(), false);
        for (int i = 0; i < v.size(); i++) {
            if (mp[v[i]] == i)
                continue;
            else {
                int ind = mp[v[i]];
                int temp = v[ind];
                v[ind] = v[i];
                v[i] = temp;
                i--;
                cnt++;
            }
        }
        return cnt;
    }
    int minimumOperations(TreeNode* root) {
        int ans = 0;
        queue<TreeNode*> q;
        q.push(root);
        while (!q.empty()) {
            int n = q.size();
            vector<int> temp;
            for (int i = 0; i < n; i++) {
                TreeNode* t = q.front();
                q.pop();
                temp.push_back(t->val);
                if (t->left) {
                    q.push(t->left);
                }
                if (t->right) {
                    q.push(t->right);
                }
            }
            ans += minswaps(temp);
            cout << ans << "     ";
            for (int ele : temp)
                cout << ele << "  ";
            cout << endl;
        }
        return ans;
    }
};