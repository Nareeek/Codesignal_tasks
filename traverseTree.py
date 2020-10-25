#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def traverseTree(t):
    stack = []
    stack.append(t)
    res = []
    if not t:
        return []
    while len(stack):
        new_n = stack.pop(0)
        res.append(new_n.value)
        if new_n.left:
            stack.append(new_n.left)
        if new_n.right:
            stack.append(new_n.right)       
    return res