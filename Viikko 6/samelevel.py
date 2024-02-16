from collections import namedtuple

def count(node, level, curlevel = 1):
    if not node:
        return 0
    if curlevel == level:
        return 1
    return count(node.left, level, curlevel + 1) + count(node.right, level, curlevel + 1)

if __name__ == "__main__":
    Node = namedtuple("Node", ["left", "right"])
    tree = Node(None,Node(Node(None,None),Node(None,None)))
    print(count(tree,1)) # 1
    print(count(tree,2)) # 1
    print(count(tree,3)) # 2
    print(count(tree,4)) # 0