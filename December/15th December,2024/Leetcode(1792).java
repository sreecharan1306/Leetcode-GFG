class Solution {
    public double inc(double p, double t){
        return ((double)(p+1)/(t+1)) - ((double)p/t);
    }
    public double maxAverageRatio(int[][] classes, int extraStudents) {
        PriorityQueue<double []> pq = new PriorityQueue<>((a,b)->{
                return Double.compare(b[0],a[0]);
        });

        for(int i=0;i<classes.length;i++){
            double p=classes[i][0],t=classes[i][1];
            pq.add(new double[]{inc(p,t),p,t});
        }
        double ans=0;
        for(int i=0;i<extraStudents;i++){
            double d[]=pq.poll();
            pq.add(new double[]{inc(d[1]+1,d[2]+1),d[1]+1,d[2]+1});
        }
        while(!pq.isEmpty()){
            double d[]=pq.poll();
            // System.out.println(Arrays.toString(pq.poll()));
            ans+=(double) d[1]/d[2];
        }
        return ans/classes.length;
    }
}