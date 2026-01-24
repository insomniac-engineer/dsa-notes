class Solution {
    public int lengthOfLastWord(String s) {
        if (s.isEmpty()) return 0;
        s = s.toLowerCase();
        int counter = 0;

        for (int i = s.length() - 1; i >= 0; --i) {
            if (counter != 0 && s.charAt(i) == ' ') return counter;
            if (s.charAt(i) >= 'a' && s.charAt(i) <= 'z') {
                counter++;
            }
        }
        return counter;
    }
}