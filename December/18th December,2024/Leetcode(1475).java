import java.util.Arrays;
class Solution {
    public int[] finalPrices(int[] prices) {
        Stack<Integer>st=new Stack<>();
        int n=prices.length;
        int sm[]=new int[n];
        // Arrays.reverse(prices);
        int left = 0, right = n - 1;  
        while (left < right) {  
            int temp = prices[left];  
            prices[left] = prices[right];  
            prices[right] = temp;  
            left++;  
            right--;  
        }  

        for (int i = 0; i < n; i++) {  
            if (st.empty()) {  
                sm[i] = 0;  
                st.push(prices[i]);  
                continue;  
            }  
            if (prices[i] >= st.peek()) {  
                sm[i] = st.peek();  
                st.push(prices[i]);  
                continue;  
            } else {  
                while (!st.empty() && prices[i] < st.peek()) {  
                    st.pop();  
                }  
                if (st.empty()) {  
                    sm[i] = 0;  
                    st.push(prices[i]);  
                } else {  
                    sm[i] = st.peek();  
                    st.push(prices[i]);  
                }  
            }  
        }  

        int[] ans = new int[n];  
        for (int i = 0; i < n; i++) {  
            ans[i] = prices[i] - sm[i];  
        }  

        left = 0;  
        right = n - 1;  
        while (left < right) {  
            int temp = ans[left];  
            ans[left] = ans[right];  
            ans[right] = temp;  
            left++;  
            right--;  
        }  

        return ans; 
    }
}