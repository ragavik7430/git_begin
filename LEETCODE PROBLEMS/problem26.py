class Solution:
    def removeDuplicates(self, nums):
        k = 1

        for i in range(1, len(nums)):
            if nums[i] != nums[k - 1]:
                nums[k] = nums[i]
                k += 1

        return k
#Example 1:
#Input: nums = [1,1,2]
#Output: 2