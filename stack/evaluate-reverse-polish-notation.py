# You are given an array of strings tokens that represents an arithmetic expression in a Reverse Polish Notation.

# Evaluate the expression. Return an integer that represents the value of the expression.

# Note that:

# The valid operators are '+', '-', '*', and '/'.
# Each operand may be an integer or another expression.
# The division between two integers always truncates toward zero.
# There will not be any division by zero.
# The input represents a valid arithmetic expression in a reverse polish notation.
# The answer and all the intermediate calculations can be represented in a 32-bit integer.

class Solution(object):
    def evalRPN(self, tokens):
        s = []

        for i in tokens:
            if i not in '+-*/':
                s.append(int(i))
            else:
                x, y = s.pop(), s.pop()
                if i == '+':
                    s.append(y+x)
                elif i == '-':
                    s.append(y-x)
                elif i == '*':
                    s.append(y*x)
                elif i == '/':
                    s.append(int(float(y)/x))
        
        return s[-1]