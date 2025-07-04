class Solution {
    public char kthCharacter(long k, int[] operations) {
                int increase = 0;
        List<Long> lengths = new ArrayList<>();
        long length = 1;

        for (int op : operations) {
            length *= 2;
            lengths.add(length);
            if (length >= k) break;
        }

        int lastop = lengths.size() - 1;

        for (int i = lastop; i >= 0; i--) {
            long half = lengths.get(i) / 2;
            int op = operations[i];

            if (k > half) {
                k -= half;
                if (op == 1) {
                    increase++;
                }
            }
        }

        return (char) ('a' + (increase % 26));
    }
}