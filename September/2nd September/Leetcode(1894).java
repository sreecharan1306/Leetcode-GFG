class Solution {
    public int chalkReplacer(int[] chalk, int k) {
        int n=chalk.length;
        int i=0;
        long sum=0;
        for(int j=0;j<n;j++){
            sum+=chalk[j];
        }
        k%=sum;
        while(n>0){
            int ind=i%n;
            if(k<chalk[ind]) return ind;
            else k-=chalk[ind];
            i++;
        }
        return -1;
    }
}