class Solution {
public:
    long long maxKelements(vector<int>& nums, int k) {
        priority_queue<long long>pq;
        for(int i:nums) pq.push(i);
        long long ans=0;
        while(k-->0){
            double x=pq.top();
            ans+=x;
            pq.pop();
            pq.push(ceil(x/3));
        }
        return ans;
    }
};