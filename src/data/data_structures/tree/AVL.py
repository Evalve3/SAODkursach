from typing import Optional, Any

from src.core.repo.data_structures.tree.tree_repo import Node, TreeABC


class AvlTree(TreeABC):

    def find(self, key: str) -> Optional[Node]:
        return self.__find(self.root, key)

    def insert(self, key: str, data: Any) -> None:
        self.root = self.__insert(self.root, key, data)

    def remove(self, key: str) -> None:
        self.root = self.__remove(self.root, key)

    def remove_all(self) -> None:
        self.root = None

    def clear_data(self, key: str) -> None:
        self.__clear_data(self.root, key)

    def __clear_data(self, node: Node, key: str) -> None:
        self.__find(node, key).data = None

    def print(self) -> None:
        return self.__print_tree(self.root, False, '')

    def get_all(self) -> list[Node]:
        return self._preorder_traversal()

    def _preorder_traversal(self, root='0', ans: list = None) -> list[Node]:
        if ans is None:
            ans = []
        if root == '0':
            root = self.root
        if root:
            ans.append(root)
            self._preorder_traversal(root.left, ans)
            self._preorder_traversal(root.right, ans)
        return ans

    def __find(self, node: Node, key: str) -> Optional[Node]:
        if not node:
            return None
        if key < node.key:
            return self.__find(node.left, key)
        if key > node.key:
            return self.__find(node.right, key)
        return node

    def __height(self, node: Node) -> int:
        return node.height if node else 0

    def __b_factor(self, node: Node) -> int:
        return self.__height(node.right) - self.__height(node.left)

    def __fix_height(self, node: Node) -> None:
        hl = self.__height(node.left)
        hr = self.__height(node.right)
        node.height = (hl if hl > hr else hr) + 1

    def __right_rotate(self, node: Node) -> Node:

        temp = node.left
        node.left = temp.right
        temp.right = node
        self.__fix_height(node)
        self.__fix_height(temp)
        return temp

    def __left_rotate(self, node: Node) -> Node:
        temp = node.right
        node.right = temp.left
        temp.left = node
        self.__fix_height(node)
        self.__fix_height(temp)
        return temp

    def __balance(self, node: Node) -> Node:
        self.__fix_height(node)
        if self.__b_factor(node) == 2:
            if self.__b_factor(node.right) < 0:
                node.right = self.__right_rotate(node.right)
            return self.__left_rotate(node)
        if self.__b_factor(node) == -2:
            if self.__b_factor(node.left) > 0:
                node.left = self.__left_rotate(node.left)
            return self.__right_rotate(node)
        return node

    def __insert(self, node: Node, key: str, data: Any) -> Node:
        if not node:
            return Node(key=key, height=1, data=data)
        if key < node.key:
            node.left = self.__insert(node.left, key, data)
        if key > node.key:
            node.right = self.__insert(node.right, key, data)
        return self.__balance(node)

    def __find_min(self, node: Node) -> Node:
        return self.__find_min(node.left) if node.left else node

    def __remove_min(self, node: Node) -> Node:
        if node.left is None:
            return node.right
        node.left = self.__remove_min(node.left)
        return self.__balance(node)

    def __remove(self, node: Node, key: str) -> Optional[Node]:
        if not node:
            return None
        if key < node.key:
            node.left = self.__remove(node.left, key)
        elif key > node.key:
            node.right = self.__remove(node.right, key)
        else:
            left = node.left
            right = node.right
            del node
            if not right:
                return left
            mn = self.__find_min(right)
            mn.right = self.__remove_min(right)
            mn.left = left
            return self.__balance(mn)

        return self.__balance(node)

    def __print_tree(self, node: Node, is_left: bool, prefix: str):
        if node:
            self.__print_tree(node.right, False, prefix + ('│   ' if is_left else '    '))
            print(prefix + ('└── ' if is_left else '┌── ') + str(node.key))
            self.__print_tree(node.left, True, prefix + ('    ' if is_left else '│   '))




