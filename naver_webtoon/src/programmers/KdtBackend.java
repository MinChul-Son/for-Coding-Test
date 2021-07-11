package programmers;

import java.util.*;

public class KdtBackend {
    public int solution(int[] d, int m) {
        int answer = 0;
        int currentBox = 1;
        for (int maxWeight : d) {
            if (maxWeight >= currentBox) { // 보트에 상자를 적재 가능
                answer++;
                m -= currentBox;
                currentBox *=2;
            } else { // 보트에 상자를 적재 불가
                currentBox = 1;
                continue;
            }
            if (m <= 0) { // 목표 상자 다 보낸 경우
                return answer;
            }
        }
        return -1;
    }

    public int[] solution(int[] deposit) {
        Stack<Integer> stack = new Stack<>();
        for (int transaction : deposit) { // 스택에 입출금 내역 넣기
            if (transaction > 0) { // 입금
                stack.push(transaction);
                continue;
            }

            //출금
            int withdraw = transaction;
            while (withdraw < 0) {
                withdraw += stack.pop();
            }
            if (withdraw > 0) {
                stack.push(withdraw);
            }
        }

        return stack.stream().mapToInt(Integer::intValue).toArray(); // 배열로 변환해서 반환
    }

    public int solution(int n, int[][] wires) { // 모든 전선을 하나씩 자르면서 bfs or dfs
        List<Integer> answerList = new ArrayList<>();
        boolean[] check = new boolean[n+1];

        int[][] arr = arr = new int[n+1][n+1];;
        for (int[] wire : wires) { // 전체 그래프 배열 생성
            arr[wire[0]][wire[1]] = 1;
            arr[wire[1]][wire[0]] = 1;
        }

        for (int[] wire : wires) {
            arr[wire[0]][wire[1]] = 0;
            arr[wire[1]][wire[0]] = 0;
            int bfsResult = bfs(1, check, arr);
            answerList.add(Math.abs(bfsResult - (n-bfsResult)));
            arr[wire[0]][wire[1]] = 1;
            arr[wire[1]][wire[0]] = 1;
        }
        System.out.println("answerList = " + answerList);
        return Collections.min(answerList);
    }

    public static void initCheck(boolean[] check){
        for(int i = 0 ; i < check.length; i++) check[i] = false;
    }

    public static int bfs(int start, boolean[] check, int[][] arr){
        // check배열 초기화
        initCheck(check);
        Queue<Integer> queue = new LinkedList<>();
        int count = 1;
        // 처음 시작노드 추가
        queue.add(start);
        // 처음 시작노드 방문처리
        check[start] = true;

        while(!queue.isEmpty()){
            int num = queue.poll();

            for(int i = 1; i < check.length; i++){
                // 현재 노드와 다른 노드 중 && 미방문 && 간선이 존재
                if(i != num && check[i] == false && arr[num][i] == 1) {
                    // 노드 추가
                    queue.add(i);
                    check[i] = true;
                    count++;
                }
            }
        }
        return count;
    }
}
