"""from functools import reduce"""

#tarda muchisimo, se hace el O(1) en espacio de la segunda parte del ejercicio
# pero el tiempo es O(2n) por lo que tarda un cristo en comparacion con las otras soluciones
class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        """ Primera aproximacion: exceed time
        rtr = []
        for i, x in enumerate(nums):
            nums.remove(x)
            math no esta instalado en esta maquina, usamos version antigua math.prod(nums) 
            rtr.append(reduce(lambda x, y: x * y, nums, 1))
            nums.insert(i, x)

        return rtr"""
        n = len(nums)
        rtr = [1] * n
        
        # rtr[i] = product of all elements to the left of i starting from 1 to avoid the i
        for i in range(1, n):
            #product of all elements to the left of i avoiding i
            rtr[i] = rtr[i - 1] * nums[i - 1]
        
        # rtr[i] = product of all elements to the right of i starting from n - 1 to avoid the i
        suffix_prod = 1
        for i in range(n - 1, -1, -1):
            rtr[i] = rtr[i] * suffix_prod
            suffix_prod *= nums[i]
        
        return rtr
        