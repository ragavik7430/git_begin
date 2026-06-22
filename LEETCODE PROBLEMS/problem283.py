class Solution:
    def moveZeroes(self, nums) :
        """
        Do not return anything, modify nums in-place instead.
        """
        last=0
        for i in range(len(nums)):
            if nums[i]!=0:
               nums[i],nums[last]=nums[last],nums[i]
               last+=1
#Example 1:
#Input: nums = [0,1,0,3,12]
#Output: [1,3,12,0,0]
