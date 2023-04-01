from typing import Optional

from src.core.tree.tree_repo import Node, TreeABC


class AvlTree(TreeABC):

    def find(self, key: int) -> bool:
        return self.__find(self.root, key)

    def insert(self, key: int) -> None:
        self.root = self.__insert(self.root, key)

    def remove(self, key: int) -> None:
        self.root = self.__remove(self.root, key)

    def print(self) -> None:
        return self.__print_tree(self.root, False, '')

    def preorder_traversal(self, root='0') -> None:
        if root == '0':
            root = self.root
        if root:
            print(root.key, end=' ')
            self.preorder_traversal(root.left)
            self.preorder_traversal(root.right)

    def __find(self, node: Node, key: int) -> bool:
        if not node:
            return False
        if key < node.key:
            return self.__find(node.left, key)
        if key > node.key:
            return self.__find(node.right, key)
        return True

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

    def __insert(self, node: Node, key: int):
        if not node:
            return Node(key=key, height=1)
        if key < node.key:
            node.left = self.__insert(node.left, key)
        if key > node.key:
            node.right = self.__insert(node.right, key)
        return self.__balance(node)

    def __find_min(self, node: Node) -> Node:
        return self.__find_min(node.left) if node.left else node

    def __remove_min(self, node: Node) -> Node:
        if node.left is None:
            return node.right
        node.left = self.__remove_min(node.left)
        return self.__balance(node)

    def __remove(self, node: Node, key: int) -> Optional[Node]:
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
        if node is not None:
            print(prefix, end="")
            if is_left:
                print("╠══", end="")
            else:
                print('╚══', end="")
            print(f"{node.key: 2}")
            self.__print_tree(node.right, True, prefix + ("║   " if is_left else "   "))
            self.__print_tree(node.left, False, prefix + ("║   " if is_left else "   "))


if __name__ == "__main__":
    tree = AvlTree()
    tree.insert(9)
    tree.insert(3)
    tree.insert(5)
    tree.insert(15)
    tree.insert(11)
    tree.insert(21)
    tree.insert(9)
    tree.insert(13)
    tree.insert(10)
    tree.print()
    tree.remove(15)
    tree.print()
    tree.remove(13)
    tree.print()
    tree.insert(23)
    tree.print()
    print(tree.find(23))
    print(tree.find(24))
