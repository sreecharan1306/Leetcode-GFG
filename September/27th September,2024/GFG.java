//{ Driver Code Starts
// Initial template for JAVA

import java.io.*;
import java.lang.*;
import java.util.*;

public class Main {
    public static void main(String args[]) throws IOException {
        // taking input using class Scanner
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int t = Integer.parseInt(br.readLine());

        while (t-- > 0) {
            // taking total number of elements
            int k = Integer.parseInt(br.readLine());
            String line = br.readLine();
            String[] tokens = line.split(" ");

            // Create an ArrayList to store the integers
            ArrayList<Integer> array = new ArrayList<>();

            // Parse the tokens into integers and add to the array
            for (String token : tokens) {
                array.add(Integer.parseInt(token));
            }

            int[] arr = new int[array.size()];
            int idx = 0;
            for (int i : array) arr[idx++] = i;
            ArrayList<Integer> res = new Solution().max_of_subarrays(k, arr);

            // printing the elements of the ArrayList
            for (int i = 0; i < res.size(); i++) System.out.print(res.get(i) + " ");
            System.out.println();
        }
    }
}
// } Driver Code Ends


// User function template for JAVA

class Solution {
    // Function to find maximum of each subarray of size k.
    public ArrayList<Integer> max_of_subarrays(int k, int arr[]) {
        // Your code here
        int n=arr.length,ri=0;
        int ans[]=new int[n-k+1];
        ArrayList<Integer> sol=new ArrayList<>();
        Deque<Integer>dq=new ArrayDeque<>();
        for(int i=0;i<n;i++){
            while(!dq.isEmpty() && dq.peek()<i-k+1){
                dq.poll();
            }
            while(!dq.isEmpty() && arr[dq.peekLast()]<arr[i]){
                dq.pollLast();
                
            }
            dq.offer(i);
            if(i>=k-1) sol.add(arr[dq.peek()]);
        }
        return sol;
        
    }
}