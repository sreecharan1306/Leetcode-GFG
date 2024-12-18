class Solution {
public:
    vector<int> finalPrices(vector<int>& prices) {
        stack<int>st;
        int n=prices.size();
        vector<int>sm;
        reverse(prices.begin(),prices.end());
        for(int i:prices){
            if(st.empty()){
                sm.push_back(0);
                st.push(i);
                continue;
            }
            if(i>=st.top()){
                sm.push_back(st.top());
                st.push(i);
                continue;
            }
            else{
                while(!st.empty() && i<st.top()){
                    st.pop();
                }
                if(st.empty()){
                    sm.push_back(0);
                    st.push(i);
                }
                else{
                    sm.push_back(st.top());
                    st.push(i);
                }
            }
            // sm.push_back(i);
        }
        // reverse(sm.begin(),sm.end());
        // reverse(prices)
        // for(int i:sm) cout<<i;
        vector<int>ans;
        for(int i=0;i<n;i++){
            ans.push_back(prices[i]-sm[i]);
        }
        reverse(ans.begin(),ans.end());
        return ans;
    }
};