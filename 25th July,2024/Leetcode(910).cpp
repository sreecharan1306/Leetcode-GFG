class Solution {
public:
    void swap(int &a,int &b){
        a=a^b;
        b=a^b;
        a=a^b;
    }
    vector<int> sortArray(vector<int>& nums) {
        sort(nums.begin(),nums.end());
        // int n=nums.size();
        // for(int i=0;i<n;i++){
        //     for(int j=0;j<n-i-1;j++){
        //         if(nums[j]>nums[j+1]){
        //             swap(nums[j],nums[j+1]);
        //         }
        //     }
        // }
        return nums;
    }
};