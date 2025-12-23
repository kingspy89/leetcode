# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        if head is None:
            return False
        visted ={}
        node= head
        while node.next :
           if node in visted:
            return True
           visted[node] = True
           node =node.next
        return False
        