## 1. 후위표기법 변환 로직 (Infix → Postfix)

핵심은 이거야: **"숫자는 그냥 지나가고, 연산자는 스택이라는 대기실에서 서열 싸움을 한다."**  
[예시문제](SWEA/assignment/260211/D4_calculator2_stack)

### 💡 icp와 isp의 정체

* **icp (in-coming priority):** 대기실로 **들어가려고 하는** 연산자의 서열.
* **isp (in-stack priority):** 이미 대기실 **안에 앉아있는** 연산자의 서열.

> **특이점 (괄호):** `(`는 밖에서는 서열 1위(`icp=3`)라 무조건 들어가지만, 일단 대기실 안에 들어가면 꼴찌(`isp=0`)가 돼. 그래야 그 뒤에 오는 어떤 연산자든 자기 위에 쌓일 수 있거든.

### 🏃 동작 시나리오 (Step-by-Step)

1. **숫자:** 고민 안 해. 그냥 결과(`postfix`)에 바로 적어.
2. **연산자 (서열 싸움):**
* 내가 지금 들어가려는데(`icp`), 안에 있는 놈(`isp`)이 나보다 서열이 높거나 같네?
* 그럼 안에 있는 놈을 **"야, 너 먼저 나가서 일해!"** 하고 `pop`해서 결과에 적어줘.
* 이걸 나보다 서열 낮은 놈이 나올 때까지 반복하다가, 드디어 내가 스택에 들어가.


3. **닫는 괄호 `)`:**
* 얘는 폭군이야. 여는 괄호 `(`를 만날 때까지 스택에 있는 모든 연산자를 다 끄집어내서 결과에 적어버려.



---

## 2. 후위표기법 계산 로직 (Get Result)

변환된 수식(예: `6528-*2/+`)을 계산할 때는 훨씬 쉬워. **"연산자를 만나면 숫자 두 개를 꺼내서 요리한다"**만 기억해.

1. **숫자:** 스택에 차곡차곡 쌓아. (나중에 연산자 만나면 쓰려고 장전하는 거야)
2. **연산자:**
* 스택에서 숫자 2개를 `pop` 해.
* **주의:** 먼저 뽑은 놈(`right`)이 오른쪽, 나중에 뽑은 놈(`left`)이 왼쪽이야. (뺄셈, 나눗셈에서 순서 바뀌면 망한다!)
* 계산하고 그 결과를 다시 스택에 `push` 해. (다음 연산의 재료가 됨)



---

## 🛠 재현이를 위한 디버깅 포인트 (이해 안 될 때 봐)

코드에서 `infix = "(6+5*(2-8)/2)"` 이걸 돌릴 때, **`5*(2-8)`** 구간을 잘 봐봐.

1. `*` 가 들어오려는데 스택에 `+`가 있어. `*`(`icp=2`) > `+`(`isp=1`)니까 `*`가 위에 쌓여.
2. 그러다 `(` 가 들어오면 서열 3위라 `*` 위에 또 쌓여.
3. `-` 가 들어오면, 안쪽에 있는 `(`가 서열 0위(`isp=0`)라 `-`(`icp=1`)가 그 위에 쌓여.
4. 마지막에 `)`를 만나는 순간, 여는 괄호 위에 있던 `-`가 `pop` 되면서 계산기로 달려가는 거야.

---

## 코드 구현

```python
icp = {"+": 1, "-": 1, "*": 2, "/": 2, "(": 3}
isp = {"+": 1, "-": 1, "*": 2, "/": 2, "(": 0}


def get_postfix(infix, n):
    postfix = ""
    stack = []

    for i in range(n):
        if infix[i] not in "()+-*/":
            postfix += infix[i]
        else:
            if infix[i] == ")":
                while stack:
                    op = stack.pop()
                    if op == "(":
                        break

                    postfix += op
            else:
                while stack and icp[infix[i]] <= isp[stack[-1]]:
                    postfix += stack.pop()

                stack.append(infix[i])

    while stack:
        postfix += stack.pop()

    return postfix


def cal_postfix(postfix):

    stack = []

    for c in postfix:
        if c not in "+-/*":
            stack.append(int(c))
        else:
            right = stack.pop()
            left = stack.pop()

            result = 0

            if c == "+":
                result = left + right
            elif c == "-":
                result = left - right
            elif c == "*":
                result = left * right
            elif c == "/":
                result = left / right

            stack.append(result)
    return stack.pop()
```