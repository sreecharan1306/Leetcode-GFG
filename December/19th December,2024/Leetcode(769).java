class Solution {
    public int maxChunksToSorted(int[] arr) {
        int ans = 0, m = 0;
        for (int i = 0; i < arr.length; i++) {
            m = Math.max(arr[i], m);
            if (m <= i)
                ans++;
        }
        return ans;
    }
}