class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return (3*sum(set(nums))-sum(nums))//2
#Example 1:
#Input: nums = [2,2,1]
#Output: 1