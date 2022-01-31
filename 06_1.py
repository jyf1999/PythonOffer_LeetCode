# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def reversePrint(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        """
        self.stack=[]
        l=head
        while l:
            self.stack.append(l.val)
            l=l.next
        self.stack.reverse()
        return self.stack
