class Solution {
    public long findScore(int[] nums) {
        PriorityQueue<Pair<Integer, Integer>> pq = new PriorityQueue<>(new Comparator<Pair<Integer, Integer>>() {
            @Override
            public int compare(Pair<Integer, Integer> a, Pair<Integer, Integer> b) {
                if (a.getKey().equals(b.getKey())) {
                    return a.getValue() - b.getValue();
                }
                return a.getKey() - b.getKey();
            }
        });
        int n = nums.length;
        if (n == 1)
            return nums[0];
        boolean visited[] = new boolean[n];
        long score = 0;
        for (int i = 0; i < n; i++) {
            pq.add(new Pair<Integer, Integer>(nums[i], i));
        }
        while (!pq.isEmpty()) {
            Pair<Integer, Integer> p = pq.peek();
            // System.out.println(p);
            int ele = p.getKey();
            int ind = p.getValue();
            if (visited[ind] == true) {
                pq.poll();
                continue;
            }
            int prev = ind - 1, next = ind + 1;
            if (ind == 0)
                prev = ind;
            else if (ind == n - 1)
                next = ind;
            score += ele;
            visited[ind] = true;
            visited[prev] = true;
            visited[next] = true;
            pq.poll();
        }
        return score;
    }
}