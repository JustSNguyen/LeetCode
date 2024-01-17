# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

import json
from collections import deque
class Codec:

    def serialize(self, root):
        if not root:
            return ""

        if not root.left and not root.right:
            return str(root.val)

        result_in_list = [str(root.val)]

        left_tree = ""
        if root.left:
            left_tree = self.serialize(root.left)
        result_in_list.extend(["(", left_tree, ")"])

        if root.right:
            right_tree = self.serialize(root.right)
            result_in_list.extend(["(", right_tree, ")"])

        return "".join(result_in_list)

    def deserialize(self, data):
        q = deque()

        for char in data:
            if "0" <= char <= "9":
                new_num = int(char)

                while q and (q[-1] == "-" or isinstance(q[-1], int)):
                    last_val = q.pop()
                    if isinstance(last_val, int):
                        is_negative = last_val < 0
                        new_num = abs(last_val) * 10 + new_num
                        if is_negative:
                            new_num = -new_num
                    else:
                        new_num = -new_num

                q.append(new_num)
            if char == "(" or char == "-":
                q.append(char)
            if char == ")":
                tree_stack = []
                while q[-1] != "(":
                    tree_stack.append(q.pop())

                q.pop()
                root = None
                assigned_root_left = False

                while tree_stack:
                    val = tree_stack.pop()
                    if not root:
                        root = TreeNode(val)
                    elif not assigned_root_left:
                        root.left = val
                        assigned_root_left = True
                    else:
                        root.right = val

                q.append(root)

        root = None
        assigned_root_left = False
        while q:
            val = q.popleft()
            if not root:
                root = TreeNode(val)
            elif not assigned_root_left:
                root.left = val
                assigned_root_left = True
            else:
                root.right = val

        return root



if __name__ == '__main__':
    codec = Codec()
    tree_string = "1()(2)"
    tree = codec.deserialize(tree_string)

    q = deque()

    if tree:
        q.append((tree, 0))
    else:
        print(None)

    while q:
        cur, level = q.popleft()

        if cur.left:
            q.append((cur.left, level + 1))
        if cur.right:
            q.append((cur.right, level + 1))

    print(tree.left, tree.right)

    string = codec.serialize(tree)
    print(string)


