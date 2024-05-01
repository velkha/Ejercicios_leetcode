import math
#visual and non-visual but optimized solution
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        Visual aproximation
       
        stack = Stack()
        for x in tokens:
            if(x == "+"):
                n = stack.pop()
                m = stack.pop()
                stack.push(m+n)
            elif(x == "-"):
                n = stack.pop()
                m = stack.pop()
                stack.push(m-n)
            elif(x == "/"):
                n = float(stack.pop())
                m = float(stack.pop())
                stack.push(math.trunc(m/n))
            elif(x == "*"):
                n = stack.pop()
                m = stack.pop()
                stack.push(m*n)
            else:
                stack.push(int(x))
        return stack.peek()

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        return 0

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return 0

    def size(self):
        return len(self.items)
    
    def show(self):
        return self.items """
        #Nonvisual but optimized
        stack = []
        operators = {
            '+': lambda y, x: x + y,
            '-': lambda y, x: x - y,
            '*': lambda y, x: x * y,
            '/': lambda y, x: (int(x / y) if x * y > 0 else -(-x // y)) 
        }

        for x in tokens:
            if x in operators:
                stack.append(operators[x](stack.pop(), stack.pop()))
            else:
                stack.append(int(x))

        return stack[-1] if stack else 0