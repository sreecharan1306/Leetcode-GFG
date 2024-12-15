class Solution {
    public boolean[] isArraySpecial(int[] nums, int[][] queries) {
        int n=queries.length;
        boolean ans[]=new boolean[n];
        int n2=nums.length;
        int arr[]=new int[n2];
        arr[0]=nums[0];
        for(int i=1;i<nums.length;i++){
            if(nums[i]%2==nums[i-1]%2){
                arr[i]=arr[i-1];
            }
            else{
                arr[i]=arr[i-1]+1;
            }
        }
        for(int i=0;i<queries.length;i++){
            int x=queries[i][0];
            int y=queries[i][1];
            if((y-x)==(arr[y]-arr[x])){
                ans[i]=true;
            }
            else ans[i]=false;

        }
        return ans;
    }
}