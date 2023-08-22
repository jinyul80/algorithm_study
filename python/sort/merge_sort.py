from typing import List


class MergeSort:
    def __init__(self):
        super().__init__()

        self.sorted_list: List[int] = []

    def sort(self, num_list: List[int]):
        """
        병합 정렬 오름차순
        Args:
            num_list(List[int]): 숫자 리스트
        """
        self.sorted_list = [0 for x in range(len(num_list))]

        self.merge_sort_sub(num_list, 0, len(num_list) - 1)

    def merge_sort_sub(self, num_list: List[int], left: int, right: int):
        """
        병합 정렬 서브 재귀함수(리스트 분리)
        Args:
            num_list(List[int]): 숫자 리스트
            left(int): 시작 인덱스
            right(int): 종료 인덱스
        """
        if left < right:
            mid = int((left + right) / 2)  # 리스트를 균등 분할

            self.merge_sort_sub(num_list, left, mid)  # 앞 부분 리스트
            self.merge_sort_sub(num_list, mid + 1, right)  # 뒷 부분 리스트

            self.merge(num_list, left, mid, right)  # 정렬 실행

    def merge(self, num_list: List[int], left: int, mid: int, right: int):
        """
        병합 정렬 서브(정렬하면서 병합)
        Args:
            num_list(List[int]): 숫자 리스트
            left(int): 시작 인덱스
            mid(int): 앞 부분 리스트의 종료 인덱스
            right(int): 종료 인덱스
        """
        idx_left = left
        idx_right = mid + 1
        idx_sorted = left

        while idx_left <= mid and idx_right <= right:
            if num_list[idx_left] < num_list[idx_right]:
                self.sorted_list[idx_sorted] = num_list[idx_left]
                idx_left += 1
                idx_sorted += 1

            else:
                self.sorted_list[idx_sorted] = num_list[idx_right]
                idx_right += 1
                idx_sorted += 1

        if idx_left > mid:
            for x in range(idx_right, right + 1):
                self.sorted_list[idx_sorted] = num_list[x]
                idx_sorted += 1
        else:
            for x in range(idx_left, mid + 1):
                self.sorted_list[idx_sorted] = num_list[x]
                idx_sorted += 1

        for x in range(left, right + 1):
            num_list[x] = self.sorted_list[x]
