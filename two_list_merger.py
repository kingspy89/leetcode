list1=[1,3,5,7]
list2=[2,4,6,8]

listmerged=list1+list2
print(sorted(listmerged))




# LINK LIST MERGER USING FUNCTION
#Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        # Step 1: Create a dummy node to start the merged list
        dummy = ListNode()
        tail = dummy   # tail always points to the last node in the merged list

        # Step 2: Traverse both lists until one ends
        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1   # attach list1’s smaller node
                list1 = list1.next  # move list1 ahead
            else:
                tail.next = list2   # attach list2’s smaller node
                list2 = list2.next  # move list2 ahead
            tail = tail.next        # move tail forward

        # Step 3: Attach whichever list still has nodes left
        if list1:
            tail.next = list1
        else:
            tail.next = list2

        # Step 4: Return the merged list (skip dummy node)
        return dummy.next
