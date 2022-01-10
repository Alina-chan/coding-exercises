"""
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

Time complexity   | O(N)
Space complexity  | O(N)
"""

def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
    parent_val = root.val
    p_val = p.val
    q_val = q.val

    # If both p and q are greater than parent
    if p_val > parent_val and q_val > parent_val:    
        return self.lowestCommonAncestor(root.right, p, q)
      
    # If both p and q are lesser than parent
    elif p_val < parent_val and q_val < parent_val:    
        return self.lowestCommonAncestor(root.left, p, q)
      
    else:
        return root
