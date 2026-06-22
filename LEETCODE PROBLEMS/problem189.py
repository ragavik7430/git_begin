class Solution:
    def rotate(self, nums, k):
        n = len(nums)
        k = k % n

        temp = nums[-k:] + nums[:-k]

        for i in range(n):
            nums[i] = temp[i]
#Example 1:
#Input: nums = [1,2,3,4,5,6,7], k = 3
#Output: [5,6,7,1,2,3,4]