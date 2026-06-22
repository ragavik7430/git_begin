class Solution:
    def deleteDuplicates(self, head):
        if not head:
            return head

        arr = []
        curr = head

        while curr:
            if curr.val not in arr:
                arr.append(curr.val)
            curr = curr.next

        dummy = ListNode(0)
        curr = dummy

        for num in arr:
            curr.next = ListNode(num)
            curr = curr.next

        return dummy.next
#Example 1:
#Input: head = [1,1,2]
#Output: [1,2]