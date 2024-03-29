from collections import namedtuple

def count(node):
    if not node:
        return 0
    if not node.left and not node.right:
        return 1
    return count(node.left)+count(node.right)


if __name__ == "__main__":
    Node = namedtuple("Node",["left","right"])
    tree = Node(left=Node(left=None, right=None), right=Node(left=None, right=None))
    print(count(tree)) # 2