def mid2pos(midexpression):
    out_put = []
    op_stack = []
    op_priority = {'*': 2, '/': 2, '%': 2, '+': 1, '-': 1, '(': 0, ')': 0}

    for exp in midexpression:
        if exp == '(':
            op_stack.append(exp)
        elif exp == ')':
            while op_stack[-1] != '(':
                out_put.append(op_stack.pop())
            op_stack.pop()
        elif exp.isdigit():
            out_put.append(exp)
        else:
            while len(op_stack) != 0 and op_priority[op_stack[-1]] >= op_priority[exp]:
                out_put.append(op_stack.pop())
            op_stack.append(exp)

    while len(op_stack) != 0:
        out_put.append(op_stack.pop())
    return "".join(out_put)

def postfix_eval(expression):
    num_stack = []

    for exp in expression:
        if exp.isdigit():
            num_stack.append(exp)
        else:
            num1 = num_stack.pop()
            num2 = num_stack.pop()
            res = eval(num1 + exp + num2)
            num_stack.append(str(res))
    return num_stack.pop()

if __name__ == "__main__":
    print(mid2pos('2+(3+5)*(6+4)*(8+3)'))
    print(postfix_eval('235+64+*83+*+'))
