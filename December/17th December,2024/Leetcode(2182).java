class Solution {
    public:
        string repeatLimitedString(string s, int l) {
            priority_queue<char>pq;
            unordered_map<char,int>mp;
            set<char>st(s.begin(),s.end());
            for(char c:s){
                mp[c]++;
            }
            for(char c:st)pq.push(c);
            string ans="";
            int temp=0;
            while(!pq.empty()){
                char c=pq.top();
                int f=mp[c];
                if(f<=l){
                    // ans+=(c*f);
                    for(int i=0;i<f;i++) ans+=c;
                    mp[c]=0;
                    pq.pop();
                    continue;
                }
                else{
                    // ans+=(c*l);
                    for(int i=0;i<l;i++) ans+=c;
                    mp[c]-=l;
                    //another character
                    pq.pop();
                    if(!pq.empty()){
                        char d=pq.top();
                        pq.pop();
                        ans+=d;
                        mp[d]-=1;
                        if(mp[d]>0) pq.push(d);
                    }
                    else{
                        return ans;
                    }
                    if(mp[c]>0) pq.push(c);
                    continue;
                }
            }
            return ans;
        }
    };