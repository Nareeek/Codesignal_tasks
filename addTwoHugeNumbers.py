# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
# Definition for singly-linked list:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def addTwoHugeNumbers(a, b):
    new_a = reverse_linked_list(a)
    new_b = reverse_linked_list(b)
    curr_a, curr_b = new_a, new_b
    carry = 0
    new_head = None
    prev = None
    while curr_a is not None or curr_b is not None:
        curr, carry = add_list_elem(curr_a, curr_b, carry)
        if prev:
            prev.next = curr
            prev = curr
        if new_head is None:
            new_head = curr
            prev = curr
        if curr_a:
            curr_a = curr_a.next
        if curr_b:
            curr_b = curr_b.next
    if carry:
        curr = ListNode(carry)
        prev.next = curr
    new_head = reverse_linked_list(new_head)
    # reverse the inputed lists back, try to avoid side effects
    reverse_linked_list(new_a)
    reverse_linked_list(new_b)
    return new_head


def reverse_linked_list(head):
    """reverse linked list, tail becomes head and new head is returned
    """
    if head is None:
        return None
    curr, prev = head, None
    while curr is not None:
        tmp = curr
        curr = curr.next
        tmp.next = prev
        prev = tmp
    return prev

def add_list_elem(in1, in2, carry):
    """addition of two nodes with carry_in and carry_out
    """
    in1_val = in1.value if in1 else 0
    in2_val = in2.value if in2 else 0
    tmp = in1_val + in2_val + carry
    return ListNode(tmp % 10000), tmp // 10000