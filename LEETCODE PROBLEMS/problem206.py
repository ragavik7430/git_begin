class Solution:
    def reverseList(self, head):
        prev = None
        curr = head

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        return prev
#Example 1:
#Input: head = [1,2,3,4,5]
#Output: [5,4,3,2,1]