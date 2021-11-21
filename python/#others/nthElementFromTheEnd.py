# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def nthElementFromTheEnd(l, n):
    s = []
    while l:
        s.append(l.value)
        l=l.next
    if n > len(s):
        return -1
    return s[-n]