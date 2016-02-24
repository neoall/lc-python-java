    public class Solution {
        public int lengthOfLongestSubstring(String s) {
            if (s == null) {
                return 0;
            }
            int max = 0;
            int[] map = new int[256];
            int beg = 0;
            int end = 0;
            while (end < s.length()) {
                char c = s.charAt(end);
                map[c]++;
                while (map[c] > 1) {
                    map[s.charAt(beg)]--;
                    beg++;
                }
                max = Math.max(max, end - beg + 1);
                end++;
            }
            return max;
        }
    }
