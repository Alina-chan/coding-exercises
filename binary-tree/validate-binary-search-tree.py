"""
Given the root of a binary tree, determine if it is a valid binary search tree (BST).

A valid BST is defined as follows:

- The left subtree of a node contains only nodes with keys less than the node's key.
- The right subtree of a node contains only nodes with keys greater than the node's key.
- Both the left and right subtrees must also be binary search trees.

Time complexity   | O(N)
Space complexity  | O(N)
"""

def isValidBST(root: Optional[TreeNode]) -> bool:
  
  def validate(node, low = -math.inf, high = math.inf):
    # An empty tree is a valid BST
    if node is None:
      return True
    
    # Current node's value must be between low and high
    if node.val <= low or node.val >= high:
      return False
    
    # Check the validity for left and right subtree
    return validate(node.left, low, node.val) and validate(node.right, node.val, high)
  
  return validate(root)
