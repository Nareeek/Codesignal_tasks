# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def reverseLinkedList(l):
    res = []
    while l:
        res.append(l.value)
        l = l.next
    res.reverse()
    return res
