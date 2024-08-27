//{ Driver Code Starts
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Stack;

public class Main {
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));

        int t = Integer.parseInt(br.readLine());

        while (t-- > 0) {
            String input = br.readLine();
            String[] inputs = input.split(" ");
            int[] arr = new int[inputs.length];

            for (int i = 0; i < inputs.length; i++) {
                arr[i] = Integer.parseInt(inputs[i]);
            }

            Solution ob = new Solution();
            System.out.println(ob.findMaxDiff(arr));
        }
    }
}

// } Driver Code Ends


class Solution {
    public int findMaxDiff(int[] arr) {
        // code here
        int n=arr.length;
        
        int[] nse=new int[n];
        Stack<Integer>st1=new Stack<>();
        st1.push(arr[n-1]);
        nse[n-1]=0;
        for(int i=n-2;i>=0;i--){
            while(!st1.empty() && arr[i]<=st1.peek()) st1.pop();
            if(st1.empty()) nse[i]=0;
            else nse[i]=st1.peek();
            st1.push(arr[i]);
        }
        
        
        int[] lse=new int[n];
        Stack<Integer>st=new Stack<>();
        lse[0]=0;
        st.push(arr[0]);
        for(int i=1;i<n;i++){
            while(!st.empty() && arr[i]<=st.peek()) st.pop();
            if(st.empty()) lse[i]=0;
            else lse[i]=st.peek();
            st.push(arr[i]);
        }
        
        int m=Integer.MIN_VALUE;
        for(int i=0;i<n;i++){
            m=Math.max(Math.abs(nse[i]-lse[i]),m);
        }
        return m;
    }
}
