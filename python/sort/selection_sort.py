from typing import List


class SelectionSort:
    def __init__(self):
        super().__init__()

    def sort(self, num_list: List[int]):
        """
        선택 정렬 오름차순
        Args:
            num_list(List[int]) : 숫자 리스트

        """
        for idx_s in range(len(num_list) - 1):
            temp_idx = idx_s

            for idx_e in range(idx_s + 1, len(num_list)):
                if num_list[idx_e] < num_list[temp_idx]:
                    temp_idx = idx_e

            temp_num = num_list[idx_s]
            num_list[idx_s] = num_list[temp_idx]
            num_list[temp_idx] = temp_num
