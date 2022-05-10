# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        list1 = head
        list2 = self.reverse(self.findMiddle(head))
        
        while list1 and list2:
            temp = list1.next
            list1.next = list2
            list1 = temp
            
            temp = list2.next
            list2.next = list1
            list2 = temp
            
        if list1:
            list1.next = None
            
    def findMiddle(self, head):
        if not head:
            return
        
        fast, slow = head, head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow 
    
    
    def reverse(self, head):
        prev, curr = None, head
        
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            
        return prev