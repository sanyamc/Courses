# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

def getLength(node):
    l=1
   
    if node==None:
        return 0
    while(node.next!=None):
        node=node.next
        l+=1
    return (l,node)

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        l,tail=getLength(head)
        tail.next=head
        j=0
        if k>l:
            k=k%l
        node=head
        while(j<(l-k)):
            j+=1
            node=node.next
        head=node.next
        node.next=None
        return head



        