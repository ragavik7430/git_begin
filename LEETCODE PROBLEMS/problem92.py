class Solution:
    def reverseBetween(self, head, left, right):
        arr = []

        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next

        arr[left-1:right] = arr[left-1:right][::-1]

        dummy = ListNode(0)
        curr = dummy

        for num in arr:
            curr.next = ListNode(num)
            curr = curr.next

        return dummy.next
#Example 1:
#Input: head = [1,2,3,4,5], left =
#       2, right = 4
#Output: [1,4,3,2,5]