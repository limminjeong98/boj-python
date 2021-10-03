s = input()
stack = []
answer = ''
for i in s:
    if i.isalpha():
        answer += i
    else:
        if i == '(':
            stack.append(i)
        elif i == ')':
            while stack and stack[-1] != '(':
                answer += stack.pop()
            stack.pop()
        elif i == '*' or i == '/':
            while stack and (stack[-1] == '*' or stack[-1] == '/'):
                answer += stack.pop()
            stack.append(i)
        elif i == '+' or i == '-':
            while stack and stack[-1] != '(':
                answer += stack.pop()
            stack.append(i)
        # print('stack ', stack)
while stack:
    answer += stack.pop()
print(answer)