public class Solution {
    public String convert(String s, int numRows) {
        if (s == null || numRows <= 1) {
            return s;
        }
        StringBuilder sb = new StringBuilder();
        int nPerLevel = numRows * 2 - 2;
        int level = s.length() / nPerLevel;
        if (s.length() % nPerLevel != 0) {
            level += 1;
        }
        for (int i = 0; i < numRows; i++) {
            for (int j = 0; j < level; j++) {
                int j1 = nPerLevel * j + i;
                if (j1 < s.length()) {
                    sb.append(s.charAt(j1));
                }
                int j2 = (j + 1) * nPerLevel - i;
                if (i > 0 && i < numRows - 1 && j2 < s.length()) {
                    sb.append(s.charAt(j2));
                }
            }
        }
        return sb.toString();
    }
}
