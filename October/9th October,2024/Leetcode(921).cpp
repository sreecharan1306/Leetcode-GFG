class Solution {
public:
    int minAddToMakeValid(string s) {
        int l=0,r=0;
        for(char c:s){
            if(c=='(') l+=1;
            else if(l>0) l-=1;
            else r++;
        }
        return l+r;
    }
};