class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        caboom
        if len(strs) <= 1:
            return [strs]
        rtrArr = []
        auxArr = []
        auxStrs = strs[:]
        i = 0
        for x in strs:
            for y in auxStrs:
                if self.isAnagram(x, y):
                    auxArr.append(y)
            auxStrs = [item for item in auxStrs if item not in  auxArr]
            if len(auxArr)>0:
                rtrArr.append(auxArr)
            auxArr=[]
        
        return rtrArr"""
        if len(strs) <= 1:
            return [strs]
        map = {}
        for s in strs:
            akey = ''.join(sorted(s))
            if akey not in map:
                map[akey] = []
            map[akey].append(s)
        return list(map.values())

    def isAnagram(self, s, t):
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