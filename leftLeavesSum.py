#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def leftLeavesSum(t):
    s = 0
    if t is None:
        return s
    
    if t.left and t.left.left is None and t.left.right is None:
        s = t.left.value
    
    return s + leftLeavesSum(t.left) + leftLeavesSum(t.right)