from bubble_sort import BubbleSort
import random
import unittest
import copy


class SortTestCase(unittest.TestCase):
    def test_bubble(self):
        max_num = 50000

        num_list = [x for x in range(1, max_num + 1)]
        actual_list = copy.deepcopy(num_list)

        random.shuffle(num_list)

        if max_num <= 100:
            print(f"정렬 전: {num_list}")

        sorter = BubbleSort()
        sorter.sort(num_list)

        if max_num <= 100:
            print(f"정렬 후: {num_list}")

        self.assertEqual(num_list, actual_list)


# if __name__ == "__main__":
#     unittest.main()
