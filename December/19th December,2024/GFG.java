

class Solution {
    boolean bs(int []arr,int key){
        int l=0,h=arr.length-1;
        while(l<=h){
            int m=(l+h)/2;
            if(arr[m]==key) return true;
            else if(arr[m]>key){
                h=m-1;
            }
            else l=m+1;
        }
        return false;
    }
    public int kthMissing(int[] arr, int k) {
        // code here
        int cnt=0;
        for(int i=1;i<1000000;i++){
            if(bs(arr,i)==false){
                cnt+=1;
                // System.out.println(i);
            }
            if(cnt==k) return i;
        }
        return 0;
    }
}