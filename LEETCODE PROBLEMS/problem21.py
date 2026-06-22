class Solution:
    def mergeTwoLists(self, list1, list2):
        arr = []

        while list1:
            arr.append(list1.val)
            list1 = list1.next

        while list2:
            arr.append(list2.val)
            list2 = list2.next

        arr.sort()

        dummy = ListNode(0)
        curr = dummy

        for num in arr:
            curr.next = ListNode(num)
            curr = curr.next

        return dummy.next
#Example 1:
#Input: list1 = [1,2,4], list2 = [1,    3,4]
#Output: [1,1,2,3,4,4]