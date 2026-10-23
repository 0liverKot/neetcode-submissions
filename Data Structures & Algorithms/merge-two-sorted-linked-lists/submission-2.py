# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if list1 is None:
            return list2
        if list2 is None: 
            return list1

        if list1.val <= list2.val:
            head = list1
            other = list2
        else:
            head = list2
            other = list1

        l = head   

        while l:
            if l.next is None:
                l.next = other
                break

            elif other is None or l.next.val <= other.val:
                l = l.next

            elif l.next.val > other.val:
                temp = l.next
                l.next = other
                other = other.next
                l.next.next = temp
                l = l.next
        
        return head