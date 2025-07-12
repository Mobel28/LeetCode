class Solution {
    public int[] earliestAndLatest(int n, int f, int s) {
        int p1 = Math.min(f, s), p2 = Math.max(f, s);
        if (p1 + p2 == n + 1) return new int[]{1, 1};

        int m = (n + 1) / 2, minR = Integer.MAX_VALUE, maxR = Integer.MIN_VALUE;
        if (p1 - 1 > n - p2) {
            int t = n + 1 - p1;
            p1 = n + 1 - p2;
            p2 = t;
        }

        if (p2 * 2 <= n + 1) {
            int a = p1 - 1, b = p2 - p1 - 1;
            for (int i = 0; i <= a; i++) {
                for (int j = 0; j <= b; j++) {
                    int[] next = earliestAndLatest(m, i + 1, i + j + 2);
                    minR = Math.min(minR, next[0] + 1);
                    maxR = Math.max(maxR, next[1] + 1);
                }
            }
        } else {
            int p4 = n + 1 - p2, a = p1 - 1, b = p4 - p1 - 1, c = p2 - p4 - 1;
            for (int i = 0; i <= a; i++) {
                for (int j = 0; j <= b; j++) {
                    int offset = i + j + 1 + (c + 1) / 2 + 1;
                    int[] next = earliestAndLatest(m, i + 1, offset);
                    minR = Math.min(minR, next[0] + 1);
                    maxR = Math.max(maxR, next[1] + 1);
                }
            }
        }
        return new int[]{minR, maxR};
    }
}