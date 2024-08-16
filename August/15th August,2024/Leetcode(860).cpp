class Solution {
public:
    bool lemonadeChange(vector<int>& bills) {
        int total=0;
        map<int,int>mp;
        for(int i:bills){
            // mp[i]+=1;
            total+=i;
            if(i==5){
                mp[i]+=1;
                continue;
            }
            else if(i==10){
                mp[i]+=1;
                if(mp[5]==0){
                    return false;
                }
                else{
                    total-=(i-5);
                    mp[5]-=1;
                }
            }
            else if(i==20){
                mp[i]+=1;
                if(mp[10]>0 && mp[5]>0){
                    mp[10]-=1;
                    mp[5]-=1;
                }
                else if(mp[10]==0 && mp[5]>=3){
                    mp[5]-=3;
                }
                else{
                    return false;
                }
                total-=15;
                // if(mp[10]==0){
                //     if(mp[5]<3){
                //         return false;
                //     }
                //     else{
                //         mp[5]-=3;
                //     }
                // }
                // total-=(i-15);
            }
            // if(total<0) return false;
        }
        return true;
    }
};