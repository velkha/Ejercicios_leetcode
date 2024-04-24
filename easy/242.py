class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        Too slow
        if len(s) != len(t):
            return False

        s = [ord(c) for c in s]
        t = [ord(c) for c in t]

        for x in s:
            aux = len(t)
            if x in t:
                t.remove(x)
            if aux == len(t):
                return False 
        return len(t) == 0"""
        if len(s) != len(t):
            return False
        
        dictS = {}
        dictT = {}

        for x in s:
            if x in dictS:
                dictS[x]+=1
            else:
                dictS[x] = 1
        for x in t:
            if x in dictT:
                dictT[x]+=1
            else:
                dictT[x] = 1

        return dictS == dictT