from ArrayStack import ArrayStack


def precedence(op):  # priority of operator
    if op == '(' or op == ')':
        return 0  # brackets must be pushed right away
    elif op == '+' or op == '-':
        return 1  # addition and subtraction is the least important operators
    elif op == '*' or op == '/':
        return 2  # multiplication and division is the second least important operators
    else:
        return -1  # error

def infixToPostfix(expr):
    stack = ArrayStack()  # stack to save numbers and operators in order
    postfix = []  # result list

    for term in expr:  # categorize operators and numbers
        if term in '(':
            stack.push(term)  # push left bracket right away
        elif term in ')':
            while not stack.isEmpty():
                op = stack.pop()  # all the operators inside the bracket
                if op == '(':
                    break  # stop the loop until the bracket is closed
                else:
                    postfix.append(op)   # the operators inside the brackets goes into res list right away

        elif term in "+-*/":  # if the term is an operator
            while not stack.isEmpty():
                op = stack.peek()
                if precedence(term) <= precedence(op):  # if the last operator has less importance than the operator
                    postfix.append(op)  # make the peeked operator appended to res list
                    stack.pop()  # delete the operator
                else:
                    break
            stack.push(term)  # push the operator to the stack
        else:
            postfix.append(term)  # put numbers into res list right away

    while not stack.isEmpty():
        postfix.append(stack.pop())  # put the rest operators into the res list in reversed order

    return postfix  # return res list


if __name__ == '__main__':
    print(infixToPostfix('8*(15-7)/4+3'))
