class Solution:
    def sortedSquares(self, nums):
        result = []

        for num in nums:
            result.append(num * num)

        result.sort()

        return result
#Example 1:
#Input: nums = [-4,-1,0,3,10]
#Output: [0,1,9,16,100]