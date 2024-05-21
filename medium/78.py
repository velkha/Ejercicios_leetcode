class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        self.backtrack(nums, 0, [], result)
        return result

    def backtrack(self, nums, start, path, result):
        # Append a copy of path to result
        result.append(path[:])
        
        # Iterate through the remaining elements
        for i in range(start, len(nums)):
            # Include nums[i] in the current subset
            path.append(nums[i])
            # Recur with the next element in the list
            self.backtrack(nums, i + 1, path, result)
            # Backtrack by removing the last element
            path.pop()   