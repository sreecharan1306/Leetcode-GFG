package November.25th November,2024;

public class Solution {
    String swap(String str, int i, int j) {
        char[] chars = str.toCharArray();
        char temp = chars[i];
        chars[i] = chars[j];
        chars[j] = temp;
        return new String(chars);
    }

    public int slidingPuzzle(int[][] board) {
        int[][] directions = { {1, 3}, {0, 2, 4}, {1, 5}, {0, 4}, {1, 3, 5}, {2, 4} };

        String target = "123450";
        String startState = Arrays.stream(board)
                                  .flatMapToInt(Arrays::stream)
                                  .collect(StringBuilder::new, StringBuilder::append, StringBuilder::append)
                                  .toString();

        Set<String> visited = new HashSet<>();
        Queue<String> queue = new LinkedList<>();
        queue.add(startState);
        visited.add(startState);

        int moves = 0;
        while (!queue.isEmpty()) {
            int size = queue.size();
            while (size-- > 0) {
                String current = queue.poll();
                if (current.equals(target)) return moves;

                int zeroPos = current.indexOf('0');
                for (int newZeroPos : directions[zeroPos]) {
                    String nextState = swap(current, zeroPos, newZeroPos);

                    if (visited.contains(nextState)) continue;
                    visited.add(nextState);
                    queue.add(nextState);
                }
            }
            moves++;
        }
        return -1;
    }
} {
    
}
