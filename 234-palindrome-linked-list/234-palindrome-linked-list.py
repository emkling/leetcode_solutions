# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        curr = self.findMiddle(head)
        list1 = head
        
        curr = self.reverse(curr)
        
        while curr and list1:
            if curr.val != list1.val:
                return False
            curr = curr.next
            list1 = list1.next
    
        return True
        
        
    def findMiddle(self, head):
        slow, fast = head, head
        
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            
        return slow
    
    
    def reverse(self, head):
        if not head: 
            return
        
        prev, curr = None, head
        
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
            
        return prev
            