class Solution {

    public int maxDifference(String s, int k) {
        int n = s.length();
        int ans = Integer.MIN_VALUE;        
        for (char a = '0'; a <= '4'; ++a) {
            for (char b = '0'; b <= '4'; ++b) {
                if (a == b) {
                    continue;
                }
                int[] best = new int[4];
                Arrays.fill(best, Integer.MAX_VALUE);
                int cnt_a = 0, cnt_b = 0;
                int prev_a = 0, prev_b = 0;
                int left = -1;
                for (int right = 0; right < n; ++right) {
                    cnt_a += (s.charAt(right) == a) ? 1 : 0;
                    cnt_b += (s.charAt(right) == b) ? 1 : 0;
                    while (right - left >= k && cnt_b - prev_b >= 2) {
                        int left_status = getStatus(prev_a, prev_b);
                        best[left_status] = Math.min(
                                best[left_status],
                                prev_a - prev_b
                        );                        ++left;
                        prev_a += (s.charAt(left) == a) ? 1 : 0;
                        prev_b += (s.charAt(left) == b) ? 1 : 0;
                    }
                    int right_status = getStatus(cnt_a, cnt_b);
                    int required_status = right_status ^ 0b10;
                    if (best[required_status] != Integer.MAX_VALUE) {
                        ans = Math.max(
                                ans,
                                cnt_a - cnt_b - best[required_status]
                        );
                    }
                }
            }
        }
        return ans;
    }

    /**
     * Helper function to calculate the 2-bit parity state.
     * Bit 1: parity of cnt_a. Bit 0: parity of cnt_b.
     */
    private int getStatus(int cnt_a, int cnt_b) {
        // (cnt_a & 1) is 1 if cnt_a is odd, 0 if even.
        // << 1 shifts it to the second bit position.
        // | (cnt_b & 1) puts the parity of cnt_b in the first bit position.
        return ((cnt_a & 1) << 1) | (cnt_b & 1);
    }
}