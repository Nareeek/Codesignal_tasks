# https://afteracademy.com/blog/check-if-a-binary-tree-is-BST-or-not
# Binary trees are already defined with this interface:
# class Tree(object):
#   def __init__(self, x):
#     self.value = x
#     self.left = None
#     self.right = None
def helper(root, range_min, range_max):
    if(root == None):
        return True
    
    if (root.value < range_min or root.value > range_max):
        return False
    
    if (helper(root.left, range_min, root.value - 1)):
        if (helper(root.right, root.value + 1, range_max)):
            return True
    return False

INT_MIN = -2147483648
INT_MAX = 2147483647

def isBST(root):
    if (helper(root, INT_MIN, INT_MAX)):
        return True
    return False
    
