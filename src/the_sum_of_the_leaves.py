class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
    
def branchSumsHelper(node, is_right, total):
    if node is None:
        return 0
    if node.right is None and node.left is None and is_right:
        return node.value
    return branchSumsHelper(node.right, True, total) + branchSumsHelper(node.left, False, total) 

def branchSums(root): 
    return branchSumsHelper(root, False, 0)