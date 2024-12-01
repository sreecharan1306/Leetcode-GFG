class Solution {
public:
    int solve(int n, vector<vector<int>> adj) {
        queue<pair<int, int>> q;
        q.push(make_pair(0, 0));
        set<int> s;
        s.insert(0);
        while (!q.empty()) {
            auto i = q.front();
            q.pop();
            int c = i.first;
            int dist = i.second;
            if (c == n - 1)
                return dist;
            for (int o : adj[c]) {
                pair<int,int>p=make_pair(o,dist+1);
                if (find(s.begin(), s.end(), o) == s.end()) {
                    q.push(p);
                    s.insert(o);
                }
            }
        }
        return 0;
    }
    vector<int> shortestDistanceAfterQueries(int n,
                                             vector<vector<int>>& queries) {
        vector<vector<int>> adj(n);
        vector<int> sol;
        for (int i = 0; i < n - 1; i++) {
            adj[i].push_back(i + 1);
        }
        for (auto i : queries) {
            adj[i[0]].push_back(i[1]);
            int ans = solve(n, adj);
            sol.push_back(ans);
        }

        return sol;
    }
};