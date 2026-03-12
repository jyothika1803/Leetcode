# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        res=[]
        # i represents the current level in the tree, and tree is the current node.
        def add(i,tree):
            if len(res)<=i:
                res.append([tree.val]) # Create a new level if needed
            else:
                res[i].append(tree.val) # Append value to the existing level
            i+=1 # Move to the next level
            if tree.left: add(i,tree.left)
            if tree.right: add(i,tree.right)
        if root:   # Start recursion if root is not None
            add(0,root)
        # Reverse values at every other level to achieve zigzag order
        for i in range(len(res)):
            if i%2==1:
                res[i].reverse()
        return res