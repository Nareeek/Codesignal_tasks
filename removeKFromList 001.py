'''import json
import math
import string
import re
import random
import sys
import traceback
import functools
from collections import OrderedDict
import numpy
import pandas

# silence pyflakes
assert json
assert math
assert string
assert re
assert random
assert sys
assert traceback
assert functools
assert OrderedDict
assert numpy
assert pandas
'''


class ListNode(object):
    _slots_ = ('value', 'next')

    def __init__(self, x):
        self.value = x
        self.next = None


class Tree(object):
    _slots_ = ('value', 'left', 'right')

    def __init__(self, x):
        self.value = x
        self.left = None
        self.right = None


# Singly-linked lists are already defined with this interface:
# class ListNode(object):
#   def __init__(self, x):
#     self.value = x
#     self.next = None
#
def removeKFromList(l, k):
    c = l
    while c:
        if c.next and c.next.value == k:
            c.next = c.next.next
        else:
            c = c.next
    return l.next if l and l.value == k else l


print(removeKFromList([1, 2, 3, 4, 5, 6, 7], 10))
