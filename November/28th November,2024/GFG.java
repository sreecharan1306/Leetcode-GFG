//{ Driver Code Starts
// Initial template for JAVA

import java.util.Scanner;

class Main {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int t = sc.nextInt();
        sc.nextLine();
        while (t > 0) {
            String str = sc.nextLine();

            Solution obj = new Solution();
            int num = obj.myAtoi(str);
            System.out.println(num);
            System.out.println("~");
            t--;
        }
    }
}
// } Driver Code Ends


class Solution {
    public int myAtoi(String s) {
        // Your code here
        s=s.trim();
        int i=0,res=0,sign=1;
        if(i<s.length() && s.charAt(i)=='-'){
            sign =-1;
            i++;
        }
        while(i<s.length() && s.charAt(i)>='0' && s.charAt(i)<='9'){
            int temp=s.charAt(i)-'0';
            if(res>Integer.MAX_VALUE/10){
                return sign==-1?Integer.MIN_VALUE:Integer.MAX_VALUE;
            }
            res=res*10+temp;
            i++;
        }
        
        return res*sign;
    }
}