class Solution {
    public long maxKelements(int[] nums, int k) {
        PriorityQueue<Integer>pq=new PriorityQueue<>((a,b)->(b-a));
        for(int i:nums) pq.add(i);
        long ans=0;
        while(k-->0){
            int x=pq.peek();
            ans+=x;
            pq.poll();
            pq.add((int)Math.ceil(x/3.0));
        }
        return ans;
    }
}