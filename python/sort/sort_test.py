from typing import List
import random
import unittest
import copy
from bubble_sort import BubbleSort
from selection_sort import SelectionSort
from merge_sort import MergeSort


class SortTestCase(unittest.TestCase):
    shuffle_list: List[int] = []
    actual_list: List[int] = []

    def init_num_list(self):
        """
        정렬 테스트를 위한 숫자 리스트 생성
        """
        max_num = 10000
        self.shuffle_list = [x for x in range(1, max_num + 1)]
        self.actual_list = copy.deepcopy(self.shuffle_list)

        random.seed(777)
        random.shuffle(self.shuffle_list)

    def print_before(self, num_list: List[int]):
        if len(num_list) <= 100:
            print(f"정렬 전: {num_list}")

    def print_after(self, num_list: List[int]):
        if len(num_list) <= 100:
            print(f"정렬 후: {num_list}")

    def test_bubble(self):
        self.init_num_list()
        self.print_before(self.shuffle_list)

        sorter = BubbleSort()
        sorter.sort(self.shuffle_list)

        self.print_after(self.shuffle_list)

        self.assertEqual(self.shuffle_list, self.actual_list)

    def test_selection(self):
        self.init_num_list()
        self.print_before(self.shuffle_list)

        sorter = SelectionSort()
        sorter.sort(self.shuffle_list)

        self.print_after(self.shuffle_list)

        self.assertEqual(self.shuffle_list, self.actual_list)

    def test_merge_sort(self):
        self.init_num_list()
        self.print_before(self.shuffle_list)

        sorter = MergeSort()
        sorter.sort(self.shuffle_list)

        self.print_after(self.shuffle_list)

        self.assertEqual(self.shuffle_list, self.actual_list)


# if __name__ == "__main__":
#     unittest.main()
