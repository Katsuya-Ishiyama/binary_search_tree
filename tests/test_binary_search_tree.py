import pytest

from binary_search_tree import (BinarySearchTree,
                                SearchNotFoundError,
                                calculate_left_child_index,
                                calculate_right_child_index)


class TestCalculateLeftChildIndex:

    current_indices = [
        (0, 1),
        (3, 7),
        (10, 21)
    ]

    unexpected_types = [
        -1.1,
        '1'
    ]

    @pytest.mark.parametrize('current_index, expected', current_indices)
    def test_calculate_correctly(self, current_index, expected):
        actual = calculate_left_child_index(current_index)
        assert actual == expected

    @pytest.mark.parametrize('unexpected_index', unexpected_types)
    def test_raise_typeerror_if_unexpected_type_was_supplied(self, unexpected_index):
        with pytest.raises(TypeError):
            calculate_left_child_index(unexpected_index)


class TestCalculateRightChildIndex:

    current_indices = [
        (0, 2),
        (3, 8),
        (10, 22)
    ]

    unexpected_types = [
        -1.1,
        '1'
    ]

    @pytest.mark.parametrize('current_index, expected', current_indices)
    def test_calculate_correctly(self, current_index, expected):
        actual = calculate_right_child_index(current_index)
        assert actual == expected

    @pytest.mark.parametrize('unexpected_index', unexpected_types)
    def test_raise_typeerror_if_unexpected_type_was_supplied(self, unexpected_index):
        with pytest.raises(TypeError):
            calculate_right_child_index(unexpected_index)


class TestBinarySearchTreeInstantiate:

    def test_instantiate(self):
        binary_tree = BinarySearchTree()
        expected = []
        assert binary_tree.tree == expected


class TestBinarySearchTreeInsert:

    def test_insert_1(self):
        binary_tree = BinarySearchTree()
        binary_tree.insert(6)
        binary_tree.insert(4)
        binary_tree.insert(8)

        expected = [6, 4, 8]

        assert binary_tree.tree == expected

    def test_insert_2(self):
        binary_tree = BinarySearchTree()
        binary_tree.insert(6)
        binary_tree.insert(8)
        binary_tree.insert(7)

        expected = [6, None, 8, None, None, 7]

        assert binary_tree.tree == expected

    def test_insert_3(self):
        binary_tree = BinarySearchTree()
        binary_tree.insert(6)
        binary_tree.insert(8)
        binary_tree.insert(9)

        expected = [6, None, 8, None, None, None, 9]

        assert binary_tree.tree == expected

    def test_insert_4(self):
        binary_tree = BinarySearchTree()
        binary_tree.insert(6)
        binary_tree.insert(4)
        binary_tree.insert(5)

        expected = [6, 4, None, None, 5]

        assert binary_tree.tree == expected

    def test_insert_5(self):
        binary_tree = BinarySearchTree()
        binary_tree.insert(6)
        binary_tree.insert(4)
        binary_tree.insert(3)

        expected = [6, 4, None, 3]

        assert binary_tree.tree == expected

    def test_insert_6(self):
        binary_tree = BinarySearchTree()
        binary_tree.insert(6)
        binary_tree.insert(2)
        binary_tree.insert(1)
        binary_tree.insert(3)
        binary_tree.insert(4)

        expected = [6, 2, None, 1, 3, None, None, None, None, None, 4]

        assert binary_tree.tree == expected

    def test_insert_7(self):
        binary_tree = BinarySearchTree()
        binary_tree.insert(6)
        binary_tree.insert(2)
        binary_tree.insert(8)
        binary_tree.insert(1)
        binary_tree.insert(3)
        binary_tree.insert(7)
        binary_tree.insert(4)

        expected = [6, 2, 8, 1, 3, 7, None, None, None, None, 4]

        assert binary_tree.tree == expected


class TestBinarySearchTreeSearch:

    @pytest.fixture(scope='function')
    def binary_search_tree(self):
        """
              6
            /  ¥
           2    8
          /¥   /
         1  3 7
             ¥
              4

        Returns
        -------
        BinarySearchTree:
            上図の2分探索木
        """
        _binary_tree = BinarySearchTree()
        _binary_tree.insert(6)
        _binary_tree.insert(2)
        _binary_tree.insert(8)
        _binary_tree.insert(1)
        _binary_tree.insert(3)
        _binary_tree.insert(7)
        _binary_tree.insert(4)

        return _binary_tree

    def test_search_success_root(self, binary_search_tree):
        tree = binary_search_tree
        found_index = tree.search(6)
        expected = 0

        assert found_index == expected

    def test_search_success_left_child(self, binary_search_tree):
        tree = binary_search_tree
        found_index = tree.search(2)
        expected = 1

        assert found_index == expected

    def test_search_success_left_right_right_child(self, binary_search_tree):
        tree = binary_search_tree
        found_index = tree.search(4)
        expected = 10

        assert found_index == expected

    def test_search_success_right_child(self, binary_search_tree):
        tree = binary_search_tree
        found_index = tree.search(8)
        expected = 2

        assert found_index == expected

    def test_search_success_right_left_child(self, binary_search_tree):
        tree = binary_search_tree
        found_index = tree.search(7)
        expected = 5

        assert found_index == expected

    def test_search_fail_1(self, binary_search_tree):
        tree = binary_search_tree
        with pytest.raises(SearchNotFoundError):
            tree.search(5)

    def test_search_fail_2(self, binary_search_tree):
        tree = binary_search_tree
        with pytest.raises(SearchNotFoundError):
            tree.search(9)


class TestBinarySearchTreeDelete:

    success_value_list = [
        (8, [6, 2, 7, 1, 3, None, None, None, None, None, 4]),
        (4, [6, 2, 8, 1, 3, 7, None, None, None, None, None]),
        (1, [6, 2, 8, None, 3, 7, None, None, None, None, 4]),
        (2, [6, 1, 8, None, 3, 7, None, None, None, None, 4]),
        (6, [4, 2, 8, 1, 3, 7, None, None, None, None, None])
    ]

    fail_value_list = [5, 9, 10]

    @pytest.fixture(scope='function')
    def binary_search_tree(self):
        """
              6
            /  ¥
           2    8
          /¥   /
         1  3 7
             ¥
              4

        Returns
        -------
        BinarySearchTree:
            上図の2分探索木
        """
        _binary_tree = BinarySearchTree()
        _binary_tree.insert(6)
        _binary_tree.insert(2)
        _binary_tree.insert(8)
        _binary_tree.insert(1)
        _binary_tree.insert(3)
        _binary_tree.insert(7)
        _binary_tree.insert(4)

        return _binary_tree

    @pytest.mark.parametrize('value, expected_tree', success_value_list)
    def test_delete_success(self, binary_search_tree, value, expected_tree):
        tree = binary_search_tree
        tree.delete(value)
        assert tree.tree == expected_tree

    @pytest.mark.parametrize('value', fail_value_list)
    def test_delete_fail(self, binary_search_tree, value):
        tree = binary_search_tree
        with pytest.raises(SearchNotFoundError):
            tree.delete(value)
