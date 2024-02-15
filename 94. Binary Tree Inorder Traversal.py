from typing import List


class Solution:
  def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        
        result = []
        stack = []
        
        while root or stack:
              while root:
                    stack.append(root)
                    root = root.left
              root = stack.pop()
              result.append(root.val)
              root = root.right
              
        return result