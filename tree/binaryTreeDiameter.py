#
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def binaryTreeDiameter(t):
    d = btDiameter(t)
    return d[1]

def btDiameter(t):
    if not t:
        return [0, 0]
    
    # left and right children
    L = btDiameter(t.left)
    R = btDiameter(t.right)
    
    # merge
    
    # at each recursion we (re-)calculate the MAX linear length
    # and keep track of max diameter we've seen so far vs the diameter that can be constructed
    # using left and right lengths - as this is the maximum "reach" (or diameter)
    ML = 1 + max(L[0], R[0])   # max length
    MD = max(1 + L[0] + R[0], max(L[1], R[1]))
    
    return [ML, MD]