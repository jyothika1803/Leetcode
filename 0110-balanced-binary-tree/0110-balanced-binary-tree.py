# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.flag=True
        self.height(root)
        return self.flag      
    def height(self,root):
        if root is None:
            return -1
        leftheight=self.height(root.left)  
        rightheight=self.height(root.right)  
        if abs(leftheight-rightheight)>1:
            self.flag=False
        return max(leftheight,rightheight)+1