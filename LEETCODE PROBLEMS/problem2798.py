class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        c=0
        for i in hours:
            if i>=target:
                c+=1
        return c
#Example 1:
#Input: hours = [0,1,2,3,4], target = 2
#Output: 3
