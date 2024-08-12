class KthLargest {
public:
    int kl;
    priority_queue<int,vector<int>,greater<int>>pq;
    KthLargest(int k, vector<int>& nums) {
        kl=k;
        for(int i:nums){
            if(pq.size()<kl){
                pq.push(i);
            }
            else if(i>pq.top()){
                pq.push(i);
                if(pq.size()>kl){
                    pq.pop();
                }
            }
        }
    }
    
    int add(int val) {
        if(pq.size()<kl){
            pq.push(val);
        }
        else if(val>pq.top()){
            pq.push(val);
            pq.pop();
        }
        return pq.top();
    }
};

/**
 * Your KthLargest object will be instantiated and called as such:
 * KthLargest* obj = new KthLargest(k, nums);
 * int param_1 = obj->add(val);
 */