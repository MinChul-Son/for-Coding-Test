package codingtest;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.List;
import java.util.Map;
import java.util.Scanner;

public class CodingTest1 {
    public static final Scanner scanner = new Scanner(System.in);
    public static void main(String[] args) throws Exception {
//        int n = scanner.nextInt(); // 송수신 기록의 수
//        String[] logs = new String[n]; // 송수신 기록
//        for(int i = 0 ; i < n ; i ++)
//        {
//            logs[i] = scanner.nextLine().trim();
//        }
//
//        List<String> record = new ArrayList<>();
//        record.add(logs[0]);
//
//        for (int i = 1; i < n; i++) {
//            System.out.println(i);
//            if (logs[i - 1].equals(logs[i])){
//                String s = record.get(record.size() - 1);
//                if (s.substring(s.length() - 1).equals(")")) {
//                    int time = Integer.parseInt(s.substring(s.length() - 2, s.length() - 1));
//                    record.set(i - 1, logs[i] + " (" + String.valueOf(time) + ")");
//                } else {
//                    record.set(i - 1, logs[i] + " (2)");
//                }
//                continue;
//            }
//            record.add(logs[i]);
//        }

        Map<Integer, String> phoneNumbers = new HashMap<>();


    }
}
