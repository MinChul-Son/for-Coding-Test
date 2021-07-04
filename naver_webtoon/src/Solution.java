import java.util.*;

public class Solution {
    public int solution(String s, String t) {
        int result = 0;
        while (true)
            if (s.contains(t)) {
                s = s.replace(t, "");
                result += 1;
            } else {
                break;
            }
        return result;
    }
}