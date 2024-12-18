//{ Driver Code Starts
// Initial Template for Java

import java.io.*;
import java.util.*;

class GFG {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int tc = Integer.parseInt(br.readLine().trim());

        while (tc-- > 0) {

            String[] str = br.readLine().trim().split(" ");
            int[] a = new int[str.length];
            for (int i = 0; i < str.length; i++) {
                a[i] = Integer.parseInt(str[i]);
            }
            String[] nk = br.readLine().trim().split(" ");
            int k = Integer.parseInt(nk[0]);
            Solution sln = new Solution();
            int ans = sln.findPages(a, k);

            System.out.println(ans);
            System.out.println("~");
        }
    }
}
// } Driver Code Ends



//Back-end complete function Template for Java

class Solution {
    static int help(int arr[],int m){
        int n=arr.length;
        int st=1;
        long pages=0;
        for(int i=0;i<n;i++){
            if(pages+arr[i]<=m){
                pages+=arr[i];
            }
            else{
                st++;
                pages=arr[i];
            }
        }
        return st;
    }
    public static int findPages(int[] arr, int k) {
        // code here
        int sol=-1;
        int n=arr.length;
        if(n<k) return -1;
        
        int l = Arrays.stream(arr).max().getAsInt();  
        int h = Arrays.stream(arr).sum(); 
        while(l<=h){
            int mid=(l+h)/2;
            int students = help(arr, mid);
            if (students > k) {
                l = mid + 1;
            }
            else {
                h = mid - 1;
            }
        }
        return l;
    }
}