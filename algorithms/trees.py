from typing import Self


class Node:
    value: int


class Tree:
    root = Node


# Binary
class BinaryNode(Node):
    left: Self | None
    right: Self | None

    def __init__(self, value: int, left: Self | None = None, right: Self | None = None) -> None:
        self.value = value
        self.left = left
        self.right = right


class BinaryTree(Tree):
    root = BinaryNode | None

    def __init__(self, root: BinaryNode | None) -> None:
        self.root = root

        # if not self.is_binary:
        #     self.balance()

    def build_tree_by_list_recursive(self, _l: list, index: int) -> BinaryNode:
        return BinaryNode(
            _l[index],
            self.build_tree_by_list_recursive(_l, 2 * index + 1),
            self.build_tree_by_list_recursive(_l, 2 * index + 2)
        )

    @classmethod
    def build_tree_by_list(cls, _l: list) -> Self:
        root = None
        current_parent = None

        temp = []

        for index, value in enumerate(_l):
            if index == 0:
                root = BinaryNode(_l[0])
                current_parent = root
                temp.append(root)
                continue

            if (index - 1) % 2 == 0:
                current_parent.left = BinaryNode(value)  # type: ignore
                temp.append(current_parent.left)

            if index % 2 == 0:
                current_parent.right = BinaryNode(value)  # type: ignore
                temp.append(current_parent.right)
                current_parent = temp[int(index / 2)]

        return cls(root)

    def is_binary_search(self) -> bool:
        temp = [(self.root, float('-inf'), float('inf'))]

        index = 0

        while index < len(temp):
            if not temp[index][1] < temp[index][0].value < temp[index][2]:
                return False

            if temp[index][0].left: temp.append((temp[index][0].left, temp[index][1], temp[index][0].value))
            if temp[index][0].right: temp.append((temp[index][0].right, temp[index][0].value, temp[index][2]))

            index += 1

        return True

    def balance(self) -> None:
        ...


class BinaryTreeTest:

    def run(self) -> None:
        print(self.is_binary_search())

    def building(self) -> BinaryTree:
        _l = [5, 3, 8, 2, 4, 7, 9]

        return BinaryTree.build_tree_by_list(_l)

    def is_binary_search(self) -> None:
        true = [5, 3, 8, 2, 4, 7, 9]
        false = [5, 3, 8, 2, 4, 1, 10]

        true_tree = BinaryTree.build_tree_by_list(true)
        false_tree = BinaryTree.build_tree_by_list(false)

        assert true_tree.is_binary_search()
        assert not false_tree.is_binary_search()


if __name__ == '__main__':
    test = BinaryTreeTest()
    test.run()
