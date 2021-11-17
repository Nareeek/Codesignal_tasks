# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def findMiddleElement(l):
    a = []
    while l:
        a.append(l.value)
        l = l.next
    mid = len(a) // 2
    
    return a[mid]

