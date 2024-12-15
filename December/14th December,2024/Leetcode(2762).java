class Solution {
    public long continuousSubarrays(int[] nums) {
        int n=nums.length;
        long ans=0;
        int l=0,r=0;
        HashMap<Integer,Integer>mp=new HashMap<>();
        while(r<n){
            mp.put(nums[r],mp.getOrDefault(nums[r],0)+1);
            while((r-l+1) > getc(nums[r],mp)){
                mp.put(nums[l],mp.getOrDefault(nums[l],0)-1);
                l++;
            }
            ans+=(r-l+1);
            r++;
        }
        return ans;
    }
    private int getc(int num,HashMap<Integer,Integer>mp){
        return mp.getOrDefault(num,0)+mp.getOrDefault(num-2,0)+mp.getOrDefault(num-1,0)+mp.getOrDefault(num+1,0)+mp.getOrDefault(num+2,0);
    }
}