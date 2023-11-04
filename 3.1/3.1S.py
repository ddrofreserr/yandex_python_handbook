def RPN(stack):
    stack_unmod = tuple(stack.split(' '))
    ans = stack.split(' ')
    for val in stack_unmod:
        i = ans.index(val)
        if val == '+':
            ans[i - 2] = int(ans[i - 2]) + int(ans[i - 1])
            ans.pop(i)
            ans.pop(i - 1)
        elif val == '*':
            ans[i - 2] = int(ans[i - 2]) * int(ans[i - 1])
            ans.pop(i)
            ans.pop(i - 1)
        elif val == '-':
            ans[i - 2] = int(ans[i - 2]) - int(ans[i - 1])
            ans.pop(i)
            ans.pop(i - 1)
    return ans


print(*RPN(input()))
