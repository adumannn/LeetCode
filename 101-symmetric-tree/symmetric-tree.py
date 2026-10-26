# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode | None) -> bool:
        
        if root is None:
            return True

        def Mirror(t1, t2):
            if t1 and not t2:
                return False
            if not t1 and t2:
                return False
            if not t1 and not t2:
                return True
            if t1.val == t2.val:

                return Mirror(t1.left, t2.right) and Mirror(t1.right, t2.left)
            return False

        return Mirror(root.left, root.right)