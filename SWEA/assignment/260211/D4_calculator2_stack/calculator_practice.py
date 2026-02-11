import sys

sys.stdin = open("input (3).txt", "r")

T = 10

# 우선순위 표 (스택 밖:icp), (스택 안:isp)
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


for tc in range(1, T + 1):
    str_len = int(input())
    str = input()

    str_post = get_postfix(str, str_len)
    print(f"#{tc} {cal_postfix(str_post)}")
