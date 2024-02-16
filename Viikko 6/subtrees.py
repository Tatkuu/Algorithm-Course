from collections import namedtuple
val = 0
def diff(node, dif = -1):
    global val
    if dif == -1:
        val = 0
    if not node:
        return 0
    if dif == 0 or dif == -1:
        res = abs(diff(node.left, dif = 1) - diff(node.right, dif = 1))
        if val < res:
            val = res
        print(res)
        return val
    if dif == 1:
        diff(node, dif = 0)
        return diff(node.right, dif) + diff(node.left, dif) + 1

if __name__ == "__main__":
    Node = namedtuple("Node", ["left", "right"])
    tree = Node(left=Node(left=Node(left=Node(left=Node(left=None, right=None), right=None), right=None), right=None), right=Node(left=Node(left=Node(left=Node(left=Node(left=None, right=None), right=None), right=None), right=None), right=None))
    print(diff(tree)) # 3