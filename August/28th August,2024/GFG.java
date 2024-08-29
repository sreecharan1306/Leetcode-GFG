//{ Driver Code Starts
// Initial Template for Java

import java.io.*;
import java.lang.*;
import java.util.*;
import java.util.Map.Entry;


// } Driver Code Ends
// User function Template for Java

class Solution {
    // Function to sort the array according to frequency of elements.
    public ArrayList<Integer> sortByFreq(int arr[]) {
        // add your code here
        HashMap<Integer,Integer>freq=new HashMap<>();
        for(int num:arr){
            int x=freq.getOrDefault(num,0);
            freq.put(num,x+1);
        }
        
        List<Map.Entry<Integer, Integer>> entryList = new ArrayList<>(freq.entrySet());
        Collections.sort(entryList, new Comparator<Map.Entry<Integer,Integer>>() {
            public int compare(Map.Entry<Integer, Integer> m1,Map.Entry<Integer, Integer> m2) {
                if(m1.getValue()==m2.getValue()){
                    return m1.getKey()-m2.getKey();
                }
                return m2.getValue()-m1.getValue();
            }
        });
        ArrayList<Integer> ans=new ArrayList<>();
        
        for(Map.Entry<Integer, Integer> m1: entryList){
            for(int i=0;i<m1.getValue();i++){
                ans.add(m1.getKey());
            }
        }
        return ans;
    }
    
}

//{ Driver Code Starts.

class Driverclass {
    public static void main(String[] args) throws NumberFormatException, IOException {
        BufferedReader sc = new BufferedReader(new InputStreamReader(System.in));
        int n = Integer.parseInt(sc.readLine());
        while (n != 0) {
            String input = sc.readLine();
            String[] inputs = input.split(" ");
            int[] arr = new int[inputs.length];

            for (int i = 0; i < inputs.length; i++) {
                arr[i] = Integer.parseInt(inputs[i]);
            }

            ArrayList<Integer> ans = new ArrayList<Integer>();
            ans = new Solution().sortByFreq(arr);
            for (int i = 0; i < ans.size(); i++) System.out.print(ans.get(i) + " ");
            System.out.println();
            n--;
        }
    }
}

// } Driver Code Ends