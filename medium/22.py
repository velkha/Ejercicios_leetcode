class Solution(object):
    def generateParenthesis(self, n):
        self.result = []
        self.backtrack("", 0, 0, n)
        return self.result
    
    def backtrack(self, s, left, right, n):
        if len(s) == 2 * n:
            self.result.append(s)
            return
        if left < n:
            self.backtrack(s + "(", left + 1, right, n)
        if right < left:
            self.backtrack(s + ")", left, right + 1, n)