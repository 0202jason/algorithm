import java.util.Arrays;

class Solution {
    public String solution(String s) {
        // String을 배열로 바꾸는 메서드
        String[] arr = s.split(" ");
        // System.out.println(Arrays.toString(arr));
        
        // 문자열을 정수로 전환
        int min = Integer.parseInt(arr[0]);
        int max = Integer.parseInt(arr[0]);
        for (int i = 1; i < arr.length; i++){
            int num = Integer.parseInt(arr[i]);
            if (num < min){
                min = num;
            }
            if (num > max){
                max = num;
            }
        }
        // 정수 + 문자열 => 문자열로 바뀜
        String answer = min + " " + max;
        return answer;
    }
}