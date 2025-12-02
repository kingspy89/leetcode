# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        while head.next!=None:
            if head.val==head.next:
                 pass
            else:
                head=head.next
        return head
    

