class BinaryTree:
    def __init__(self):
        self.root = None

    def pre_order(self):
        output = []

        def walk(node):
            if not node:
                return
            # deal with root
            output.append(node.value)
            # check the left sub-tree
            walk(node.left)
            # check the right sub-tree
            walk(node.right)
        walk(self.root)

        return output


class BST(BinaryTree):
    def add(self, value):

        def walk(node, node_to_add):

            if not node:
                return

            if node_to_add.value < node.value:
                # go to the left
                if not node.left:
                    node.left = node_to_add
                else:
                    walk(node.left, node_to_add)
            else:
                # got to the right
                if not node.right:
                    node.right = node_to_add
                else:
                    walk(node.right, node_to_add)

        n = Node(value)

        if not self.root:
            self.root = n
            return

        walk(self.root, n)


class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


bst = BST()
bst.add(4)
bst.add(7)
bst.add(5)
bst.add(9)
bst.add(2)
bst.add(30)
bst.add(-1)
print(bst.pre_order())


#         4
#     2       7
#  -1       5    9
#                    30
