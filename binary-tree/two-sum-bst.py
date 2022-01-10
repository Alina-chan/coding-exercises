"""
Given the root of a Binary Search Tree and a target number k, return true if 
there exist two elements in the BST such that their sum is equal to the given target.

Time complexity   | O(N)
Space complexity  | O(N)
"""

def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
    # Initialize a list for the inorder traversal of the BST
    node_list = list()
    
    # Inorder: left subtree -> root -> right subtree
    def inorder(root, node_list):
        if root is None:
            return 

        inorder(root.left, node_list)
        node_list.append(root.val)
        inorder(root.right, node_list)

    inorder(root, node_list)
    
    # Create two pointers pointing to the beginning and the end of the inorder list
    left = 0
    right = len(node_list) - 1

    while left < right:
        # Calculate the sum of the nodes at pointers
        s = node_list[left] + node_list[right]
        
        if s == k:
            return True
        # Increase the sum of current elements
        if s < k:
            left += 1
        # Decrease the sum of current elements
        else:
            right -= 1
            
    # Pointers crossed each other - no result found
    return False
