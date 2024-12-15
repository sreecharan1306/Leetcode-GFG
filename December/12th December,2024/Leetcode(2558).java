class Solution {
    public long pickGifts(int[] gifts, int k) {
        PriorityQueue<Integer>pq=new PriorityQueue<>((a,b)-> b-a);
        for(int i:gifts) pq.add(i);
        while(k>0){
            int x=pq.peek();
            if(x==1) break;
            pq.poll();
            pq.add((int) Math.sqrt(x));
            k-=1;
        }
        long ans=0;
        while(!pq.isEmpty()) ans+=pq.poll();
        return ans;
    }
}