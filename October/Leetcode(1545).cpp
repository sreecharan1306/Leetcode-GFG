class Solution {
public:
    string invert(string s){
        string temp="";
        for(int i=0;i<s.size();i++){
            if(s[i]=='0'){
                temp+='1';
            }
            else{
                temp+='0';
            }
        }
        reverse(temp.begin(),temp.end());
        return temp;
    }
    char findKthBit(int n, int k) {
        string s="0";
        // string prev="0";
        while(true){
            if(k<=s.size()) return s[k-1];
            auto prev=s;
            reverse(prev.begin(),prev.end());
            for(auto &ch:prev){
                ch= ch=='0'?'1':'0';
            }
            s+='1'+prev;
        }
        return '0';
    }
};