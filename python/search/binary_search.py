import random
from typing import List


class BinarySearch:
    def __init__(self):
        super().__init__()

    def search(self, num_list: List[int], find_list: List[int]):
        """
        숫자 리스트에서 특정 숫자가 존재하는지 체크
        Args:
            num_list: 숫자 리스트
            find_list: 찾으려는 숫자 리스트

        Returns: None
        """

        # 숫자 리스트 정렬
        num_list.sort()

        # 찾으려는 숫자를 하나씩 탐색
        for find_num in find_list:
            find_flag = False

            # 시작, 종료 index 설정
            start = 0
            end = len(num_list) - 1

            while start <= end:
                # 중앙 index 설정
                mid = int((start + end) / 2)

                if find_num < num_list[mid]:
                    # 찾는 값이 mid 위치의 값보다 작다면
                    # 종료 인덱스를 mid -1로 변경
                    end = mid - 1
                elif find_num > num_list[mid]:
                    # 찾는 값이 mid 위치의 값보다 큰 경우
                    start = mid + 1
                else:
                    # 값을 찾은 경우
                    find_flag = True
                    break

            # 결과 출력
            print(f"숫자: {find_num}, 탐색 결과: {find_flag}")


if __name__ == "__main__":
    # 숫자 리스트 생성
    limit = 1000
    temp_list = [x for x in range(1, limit * 3)]
    random.shuffle(temp_list)

    num_list = temp_list[:limit]

    # 찾으려는 숫자 리스트 생성
    random.shuffle(temp_list)
    find_list = temp_list[:10]

    obj = BinarySearch()
    obj.search(num_list, find_list)
