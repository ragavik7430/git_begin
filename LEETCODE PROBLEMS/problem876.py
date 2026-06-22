class Solution:
    def middleNode(self, head):
        count = 0
        curr = head

        while curr:
            count += 1
            curr = curr.next

        mid = count // 2

        curr = head
        for _ in range(mid):
            curr = curr.next

        return curr
#Example 1:
#Input: head = [1,2,3,4,5]
#Output: [3,4,5]