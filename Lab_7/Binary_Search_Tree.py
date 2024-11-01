class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    # Insertion method
    def insert(self, value):
        if not self.root:
            self.root = Node(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = Node(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = Node(value)
            else:
                self._insert_recursive(node.right, value)

    # Search method
    def search(self, value):
        return self._search_recursive(self.root, value) is not None

    def _search_recursive(self, node, value):
        if node is None or node.value == value:
            return node
        if value < node.value:
            return self._search_recursive(node.left, value)
        return self._search_recursive(node.right, value)

    # In-order traversal
    def inorder_traversal(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.value)
            self._inorder_recursive(node.right, result)

    # Pre-order traversal
    def preorder_traversal(self):
        result = []
        self._preorder_recursive(self.root, result)
        return result

    def _preorder_recursive(self, node, result):
        if node:
            result.append(node.value)
            self._preorder_recursive(node.left, result)
            self._preorder_recursive(node.right, result)

    # Post-order traversal
    def postorder_traversal(self):
        result = []
        self._postorder_recursive(self.root, result)
        return result

    def _postorder_recursive(self, node, result):
        if node:
            self._postorder_recursive(node.left, result)
            self._postorder_recursive(node.right, result)
            result.append(node.value)

    # Deletion method
    def delete(self, value):
        self.root = self._delete_recursive(self.root, value)

    def _delete_recursive(self, node, value):
        if node is None:
            return node

        if value < node.value:
            node.left = self._delete_recursive(node.left, value)
        elif value > node.value:
            node.right = self._delete_recursive(node.right, value)
        else:
            # Node with only one child or no child
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # Node with two children
            node.value = self._min_value(node.right)
            node.right = self._delete_recursive(node.right, node.value)

        return node

    def _min_value(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current.value

    def find_max(self):
        if self.root is None:
            return None  # Tree is empty
        current = self.root
        while current.right:  # Traverse to the rightmost node
            current = current.right
        return current.value  # Return the value of the rightmost node

    def count_nodes(self):
        return self._count_nodes_recursive(self.root)

    def _count_nodes_recursive(self, node):
        if node is None:
            return 0
        return 1 + self._count_nodes_recursive(node.left) + self._count_nodes_recursive(node.right)

    def height(self):
        return self._height_recursive(self.root)

    def _height_recursive(self, node):
        if node is None:
            return -1
        left_height = self._height_recursive(node.left)
        right_height = self._height_recursive(node.right)
        return 1 + max(left_height, right_height)

    def is_valid_bst(self):
        return self._is_valid_bst_recursive(self.root, float('-inf'), float('inf'))

    def _is_valid_bst_recursive(self, node, min_value, max_value):
        if node is None:
            return True
        if not (min_value < node.value < max_value):
            return False
        return (self._is_valid_bst_recursive(node.left, min_value, node.value) and
                self._is_valid_bst_recursive(node.right, node.value, max_value))

# Example usage:
bst = BinarySearchTree()
for value in [5, 3, 7, 2, 4, 6, 8]:
    bst.insert(value)

# Test search
print(bst.search(4))  # Should return True
print(bst.search(9))  # Should return False

# Test traversals
print("In-order:", bst.inorder_traversal())   # Output: [2, 3, 4, 5, 6, 7, 8]
print("Pre-order:", bst.preorder_traversal()) # Output: [5, 3, 2, 4, 7, 6, 8]
print("Post-order:", bst.postorder_traversal()) # Output: [2, 4, 3, 6, 8, 7, 5]

# Test deletion
bst.delete(3)
print("After deleting 3:", bst.inorder_traversal())  # Output should not include 3

# Find the maximum value
print("Maximum value in BST:", bst.find_max())  # Output: 8

# Count the total number of nodes
print("Total number of nodes in BST:", bst.count_nodes())  # Output: 6

# Find the height of the BST
print("Height of BST:", bst.height())  # Output: 2

# Check if the tree is a valid BST
print("Is the tree a valid BST?", bst.is_valid_bst())  # Output: True

# Create an invalid BST example
invalid_bst = BinarySearchTree()
invalid_bst.insert(5)
invalid_bst.root.left = Node(7)  # Incorrectly placing a larger value on the left
invalid_bst.root.right = Node(6)

print("Is the tree a valid BST?", invalid_bst.is_valid_bst())  # Output: False
