# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class Solution(object):
    def isBalanced(self, root):
        def check(node):
            if node is None:
                return 0, True

            left_tree, left_balanced = check(node.left)
            right_tree, right_balanced = check(node.right)
            
            current_height = 1 + max(left_tree, right_tree)
            

            is_balanced = left_balanced and right_balanced and abs(left_tree - right_tree) <= 1
            
            return current_height, is_balanced
            
        return check(root)[1]
        


        