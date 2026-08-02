import java.util.Stack;

class Solution {
    boolean solution(String s) {
        // 필요 없는 변수. 없애고 써도 될듯.
        boolean answer = true;
        
        // Stack 선언. 메서드로는 push, pop, peak, size, isEmpty 등이 있다.
        // 기본 자료구조는 vector
        // 요즘은 Deque를 많이 쓴다네??
        Stack<Character> stack = new Stack<>();
        for (int i = 0; i < s.length(); i++){
            char c = s.charAt(i);
            if (c == '('){
                stack.push(c);
            }
            else if(c == ')'){
                // stack.isEmpth() 메서드를 사용하면 편함
                if (stack.size() == 0){
                    return false;
                }
                else stack.pop();
            }
        }
        // stack.isEmpty()로 줄여도 괜찮음.
        if (stack.size() == 0){
            return answer;
        }
        else{
            answer = false;
            return answer;
        }
    }
}