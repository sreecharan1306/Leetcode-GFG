class Solution {
public:
    string countOfAtoms(string formula) {
        int n = formula.size(), i, j, k;
        stack<pair<string, int>> st;
        for (int i = 0; i < n; i++) {
            char ch = formula[i];
            if (isupper(ch)) {
                string ele = "";
                ele += ch;
                for (j = i + 1; j < n; j++) {
                    if (!islower(formula[j]))
                        break;
                    else
                        ele += formula[j];
                }

                string dig = "";
                for (k = j; k < n; k++) {
                    ch = formula[k];
                    if (!isdigit(ch))
                        break;
                    else
                        dig += ch;
                }
                if (dig == "")
                    dig = "1";
                int digit = stoi(dig);
                st.push({ele, digit});
                i = k - 1;
            } else if (ch == '(') {
                st.push({"(", -1});
            } else if (ch == ')') {
                string dig = "";
                for (j = i + 1; j < n; j++) {
                    ch = formula[j];
                    if (!isdigit(ch))
                        break;
                    else
                        dig += ch;
                }
                if (dig == "")
                    dig = "1";
                int digit = stoi(dig);

                vector<pair<string, int>> temp;
                while (!st.empty() && st.top().first != "(") {
                    pair<string, int> p = st.top();
                    st.pop();
                    temp.push_back({p.first, p.second * digit});
                }
                if (!st.empty() && st.top().first == "(") {
                    st.pop();
                }
                // st.pop();
                while (!temp.empty()) {
                    st.push(temp.back());
                    temp.pop_back();
                }
                i = j - 1;
            }
        }
        map<string, int> mp;
        while (!st.empty()) {
            pair<string, int> p1 = st.top();
            st.pop();
            mp[p1.first] += p1.second;
        }

        string ans = "";
        for (auto m : mp) {
            ans += m.first;
            if (m.second > 1)
                ans += to_string(m.second);
        }
        return ans;
    }
};