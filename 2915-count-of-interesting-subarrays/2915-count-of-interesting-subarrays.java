class Solution {
    public long countInterestingSubarrays(List<Integer> nums, int modulo, int k) {
        long count = 0;
        Map<Integer, Long> map = new HashMap<>();
        int curr = 0;
        map.put(0, 1L); // base case

        for (int num : nums) {
            if (num % modulo == k) {
                curr++;
            }

            int need = (curr - k + modulo) % modulo;
            count += map.getOrDefault(need, 0L);

            int key = curr % modulo;
            map.put(key, map.getOrDefault(key, 0L) + 1);
        }

        return count;
    }
}
