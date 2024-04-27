class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) <= 1:
            return False
            
        stack = Stack()
        parentesis = ['(','[','{']
        for x in s:
            if x in parentesis:
                stack.push(x)
            else:
                if x == ')' and stack.peek() != '(':
                    return False
                elif x == ']' and stack.peek() != '[':
                    return False
                elif x == '}' and stack.peek() != '{':
                    return False
                stack.pop()
        return stack.size() == 0

            

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