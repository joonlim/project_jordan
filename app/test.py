import unittest
import utils as utils
from random import shuffle


class UtilsTests(unittest.TestCase):

    def test_group_into_pairs_even(self):
        test_items = [1, 2, 3, 4, 5, 6, 7]
        pairs_list = utils.group_into_pairs(test_items)
        result = [[1, 2], [3, 4], [5, 6], [7]]
        self.assertEqual(pairs_list, result)

    def test_group_into_pairs_odd(self):
        test_items = [1, 2, 3, 4, 5, 6, 7, 8]
        pairs_list = utils.group_into_pairs(test_items)
        result = [[1, 2], [3, 4], [5, 6], [7, 8]]
        self.assertEqual(pairs_list, result)

    def test_sort_list_by_attribute_basic(self):
        test_list = [
            {"attr": 1},
            {"attr": 2},
            {"attr": 3},
            {"attr": 4},
            {"attr": 5},
            {"attr": 6},
            {"attr": 7},
            {"attr": 8},
            {"attr": 9},
            {"attr": 10}
        ]
        shuffle(test_list)
        utils.sort_list_by_attribute(test_list, "attr", None, False)

        result = [
            {"attr": 1},
            {"attr": 2},
            {"attr": 3},
            {"attr": 4},
            {"attr": 5},
            {"attr": 6},
            {"attr": 7},
            {"attr": 8},
            {"attr": 9},
            {"attr": 10}
        ]

        self.assertEqual(test_list, result)

    def test_sort_list_by_attribute_reverse(self):
        test_list = [
            {"attr": 1},
            {"attr": 2},
            {"attr": 3},
            {"attr": 4},
            {"attr": 5},
            {"attr": 6},
            {"attr": 7},
            {"attr": 8},
            {"attr": 9},
            {"attr": 10}
        ]
        shuffle(test_list)
        utils.sort_list_by_attribute(test_list, "attr", None, True)

        result = [
            {"attr": 10},
            {"attr": 9},
            {"attr": 8},
            {"attr": 7},
            {"attr": 6},
            {"attr": 5},
            {"attr": 4},
            {"attr": 3},
            {"attr": 2},
            {"attr": 1}
        ]

        self.assertEqual(test_list, result)

    def test_sort_list_by_attribute_two_attrs(self):
        test_list = [
            {"attr": 1, "attr2": 1},
            {"attr": 1, "attr2": 2},
            {"attr": 1, "attr2": 3},
            {"attr": 1, "attr2": 4},
            {"attr": 1, "attr2": 5},
            {"attr": 2, "attr2": 6},
            {"attr": 2, "attr2": 7},
            {"attr": 2, "attr2": 8},
            {"attr": 2, "attr2": 9},
            {"attr": 2, "attr2": 10}
        ]
        shuffle(test_list)
        utils.sort_list_by_attribute(test_list, "attr", "attr2", False)

        result = [
            {"attr": 1, "attr2": 1},
            {"attr": 1, "attr2": 2},
            {"attr": 1, "attr2": 3},
            {"attr": 1, "attr2": 4},
            {"attr": 1, "attr2": 5},
            {"attr": 2, "attr2": 6},
            {"attr": 2, "attr2": 7},
            {"attr": 2, "attr2": 8},
            {"attr": 2, "attr2": 9},
            {"attr": 2, "attr2": 10}
        ]

        self.assertEqual(test_list, result)


def main():
    unittest.main()


if __name__ == '__main__':
    main()
