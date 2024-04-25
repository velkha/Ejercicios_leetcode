class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        auxDic = {}
        for x in nums:
            if x in auxDic:
                auxDic[x]+=1
            else:
                auxDic[x]=1
        
        sortedArr = sorted(auxDic, key=auxDic.get, reverse=True)
        return sortedArr[:k]


        """ Lo que pide es retornar los K elementos que mas veces aparecen en el array, no los que tengan mas de k
        newArr = []
        for key, value in auxDic.items():
            if value>=k:
                newArr.append(key)"""