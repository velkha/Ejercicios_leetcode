class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        Tengo que aprender a usar mejor los sets, se me ha complicado mas de lo que deberia
        """
        num_set = set(nums)
        maxstr=0
        for num in num_set:
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1
                maxstr = max(maxstr, current_streak)

        return maxstr
