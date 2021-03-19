from typing import List, Optional


class SearchNotFoundError(Exception):
    """BinarySearchTreeで検索した結果見つからなかった場合に返すエラー"""
    pass


Index = int


def calculate_left_child_index(parent_index: Index) -> Index:
    if not isinstance(parent_index, Index):
        raise TypeError('Unexpected type data was supplied.')

    return 2 * parent_index + 1


def calculate_right_child_index(parent_index: Index) -> Index:
    if not isinstance(parent_index, Index):
        raise TypeError('Unexpected type data was supplied.')

    return 2 * parent_index + 2


class BinarySearchTree(object):

    def __init__(self):
        self.tree: List[Optional[int]] = []

    def _insert_internal(self, node: int, index: Index) -> None:
        try:
            parent = self.tree[index]
        except IndexError:
            size = len(self.tree)
            nones: List[Optional[int]] = [None] * (index - size)
            self.tree.extend(nones + [node])
            return
        except Exception as e:
            raise e

        if parent is None:
            self.tree[index] = node
            return

        if node < parent:
            self._insert_internal(node, calculate_left_child_index(index))
        else:
            self._insert_internal(node, calculate_right_child_index(index))

    def insert(self, node: int) -> None:
        self._insert_internal(node, 0)

    def _search_internal(self, value: int, index: Index) -> Index:
        try:
            parent = self.tree[index]
        except IndexError:
            raise SearchNotFoundError
        except Exception as e:
            raise e

        if parent is None:
            raise SearchNotFoundError

        if value == parent:
            return index
        elif value < parent:
            return self._search_internal(value, calculate_left_child_index(index))
        else:
            return self._search_internal(value, calculate_right_child_index(index))

    def search(self, value: int) -> Index:
        return self._search_internal(value, 0)

    def search_max_child_index(self, parent_index: Index) -> Index:
        right_child_index = calculate_right_child_index(parent_index)

        try:
            right_child = self.tree[right_child_index]
        except IndexError:
            return parent_index
        except Exception as e:
            raise e

        if right_child is None:
            return parent_index

        return self.search_max_child_index(right_child_index)

    def delete(self, value: int):
        try:
            target_index = self.search(value)
        except SearchNotFoundError as e:
            raise e
        except Exception as e:
            raise e

        try:
            left_child_index = calculate_left_child_index(target_index)
            left_child = self.tree[left_child_index]
        except IndexError:
            left_child = None
        except Exception as e:
            raise e

        try:
            right_child_index = calculate_right_child_index(target_index)
            right_child = self.tree[right_child_index]
        except IndexError:
            right_child = None
        except Exception as e:
            raise e

        if (left_child is None) and (right_child is None):
            self.tree[target_index] = None
            return

        if (left_child is not None) and (right_child is not None):
            left_child_index = calculate_left_child_index(target_index)
            child_index = self.search_max_child_index(left_child_index)
        elif (left_child is not None) and (right_child is None):
            child_index = left_child_index
        else:
            child_index = right_child_index

        self.tree[target_index] = self.tree[child_index]
        self.tree[child_index] = None
