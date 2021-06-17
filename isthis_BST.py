def check(node, max_val = float('inf'), min_val = float('-inf')):
    if not node:
        return True
    if node.data <= min_val or node.data >= max_val:
        return False
    return check(node.left, node.data, min_val) and check(node.right, max_val, node.data)

def check_binary_search_tree_(root):
    return check(root) 