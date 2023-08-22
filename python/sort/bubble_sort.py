from typing import List

class BubbleSort:

    def __init__(self):
        super().__init__()

    def sort(self, num_list: List[int]):

        for idx_e in reversed(range(len(num_list))):
            for idx_s in range(0, idx_e):
                if num_list[idx_s] > num_list[idx_e]:
                    temp_num = num_list[idx_s]
                    num_list[idx_s] = num_list[idx_e]
                    num_list[idx_e] = temp_num
