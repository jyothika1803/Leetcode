# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue=deque([root])
        result=[]
        level=0
        if root is None:
            return []
        while queue:
            size=len(queue)
            level_nodes=[]
            for _ in range(size):
                node=queue.popleft()
                level_nodes.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            result.append(level_nodes)
            level+=1
        return result
