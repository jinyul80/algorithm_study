from bubble_sort import BubbleSort
from selection_sort import SelectionSort
import random
import unittest
import copy


class SortTestCase(unittest.TestCase):
    def get_num_list(self):
        max_num = 10000
        num_list = [x for x in range(1, max_num + 1)]

        return num_list

    def test_bubble(self):
        num_list = self.get_num_list()
        actual_list = copy.deepcopy(num_list)

        random.seed(777)
        random.shuffle(num_list)

        if len(num_list) <= 100:
            print(f"정렬 전: {num_list}")

        sorter = BubbleSort()
        sorter.sort(num_list)

        if len(num_list) <= 100:
            print(f"정렬 후: {num_list}")

        self.assertEqual(num_list, actual_list)

    def test_selection(self):
        num_list = self.get_num_list()
        actual_list = copy.deepcopy(num_list)

        random.seed(777)
        random.shuffle(num_list)

        if len(num_list) <= 100:
            print(f"정렬 전: {num_list}")

        sorter = SelectionSort()
        sorter.sort(num_list)

        if len(num_list) <= 100:
            print(f"정렬 후: {num_list}")

        self.assertEqual(num_list, actual_list)


# if __name__ == "__main__":
#     unittest.main()
