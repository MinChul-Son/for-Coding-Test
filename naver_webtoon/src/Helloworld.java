import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class Helloworld {
    public static void main(String[] args) throws IOException {

    }

}
//class Solution {
//    public int solution(int[] prices, int[] discounts) {
//        int answer = 0;
//        Integer[] prices_sort = Arrays.stream(prices).boxed().toArray(Integer[]::new);
//        Arrays.sort(prices_sort, Collections.reverseOrder());
//        Integer[] discounts_sort = Arrays.stream(discounts).boxed().toArray(Integer[]::new);
//        Arrays.sort(discounts_sort, Collections.reverseOrder());
//        if (prices_sort.length > discounts_sort.length) {
//            for (int i = 0; i < discounts_sort.length; i++) {
//                answer += prices_sort[i] * (100-discounts_sort[i]) / 100;
//            }
//            for (int i = prices_sort.length - discounts_sort.length + 1; i < prices_sort.length; i++) {
//                answer += prices_sort[i];
//            }
//        } else {
//            for (int i = 0; i < prices_sort.length; i++) {
//                answer += prices_sort[i] * (100-discounts_sort[i]) / 100;
//            }
//        }
//        return answer;
//    }
//}

//class Solution {
//    public String[] solution(String s) {
//        String[] answer = {};
//        List<String> splitListHead = new ArrayList<>();
//        List<String> splitListTail = new ArrayList<>();
//        List<String> joinedList = new ArrayList<>();
//        int first = 0;
//        int last = s.length();
//        int mid = 1;
//        String temp_split = "";
//        while (first+mid <= s.length()/2) {
//            temp_split = s.substring(first, first + mid);
//            if (temp_split.equals(s.substring(last - mid, last))) {
//                splitListHead.add(temp_split);
//                splitListTail.add(temp_split);
//                first += mid;
//                last -= mid;
//                mid = 1;
//            } else {
//                mid++;
//            }
//        }
//        if (splitListHead.isEmpty()) { // 공통부분 존재 x
//            splitListHead.add(s);
//        }
//        if (s.length() > String.join("", splitListHead).length() + String.join("", splitListTail).length()) {
//            splitListHead.add(s.substring(String.join("", splitListHead).length(),
//                    s.length() - String.join("", splitListTail).length()));
//        }
//        Collections.reverse(splitListTail); // 뒷부분 뒤집고
//        joinedList.addAll(splitListHead); // 합치기
//        joinedList.addAll(splitListTail);
//        System.out.println(temp_split);
//        answer = new String[joinedList.size()];
//        joinedList.toArray(answer); // 리스트 배열로 변환
//        return answer;
//    }
//}
