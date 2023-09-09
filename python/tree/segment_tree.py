from typing import List


class SegmentTree:
    """
    세그먼트 트리 : 구간합, 구간 최소값, 구간 최대값 조회에 최적화된 알고리즘
                   (숫자 리스트의 업데이트가 자주 발생하는 경우에 최적화된 알고리즘)
    """

    def __init__(self):
        super().__init__()
        self.num_tree: List[int] = []

    def init_tree(self, num_list):
        """
        Segment tree 초기화
        Args:
            num_list: 숫자 리스트

        Returns: None

        """
        # Num 리스트 전체를 커버하는 k를 계산
        k = 1
        while 2**k < len(num_list):
            k += 1

        # Tree의 시작 인덱스
        start_idx = 2**k

        # Tree의 사이즈
        tree_size = start_idx * 2

        # Tree 초기화
        self.num_tree = [0 for _ in range(tree_size)]
        for idx in range(len(num_list)):
            in_idx = idx + start_idx
            self.num_tree[in_idx] = num_list[idx]

        # Tree 구간합 설정
        # Tree의 마지막 노드부터 시작하여 노드 2개의 합을 부모 노드에 저장
        for idx in range(tree_size - 1, 1, -2):
            before_idx = idx - 1
            parent_idx = int(idx / 2)

            self.num_tree[parent_idx] = self.num_tree[idx] + self.num_tree[before_idx]

        # Tree 출력
        depth_limit = 2
        print("Segment Tree")
        print(f"{self.num_tree[1]:2}")
        for idx in range(2, tree_size):
            print(f"{self.num_tree[idx]:2} ", end="")
            if idx + 1 == depth_limit * 2:
                depth_limit = depth_limit * 2
                print()

    def area_sum(self, start: int, end: int):
        """
        숫자 리스트에서 구간합 계산
        Args:
            start: 시작 인덱스
            end: 종료 인덱스

        Returns: None

        """
        # 구간합 결과 저장 변수
        sum = 0

        # 구간합에 사용할 노드 리스트
        choice_idx_list = []

        # 트리의 시작, 종료 인덱스로 변경
        s_idx = int(start + (len(self.num_tree) / 2) - 1)
        e_idx = int(end + (len(self.num_tree) / 2) - 1)

        while True:
            # 시작 노드가 트리의 오른쪽이면 구간합에 사용
            if s_idx % 2 == 1:
                choice_idx_list.append(s_idx)

            # 종료 노드가 트리의 왼쪽이면 구간합에 사용
            if e_idx % 2 == 0:
                choice_idx_list.append(e_idx)

            # 부모 노드로 이동
            s_idx = int((s_idx + 1) / 2)
            e_idx = int((e_idx - 1) / 2)

            # 시작, 종료 노드가 교차되면 종료
            if s_idx > e_idx:
                break

        # 선택된 노드들의 구간합 계산
        for idx in choice_idx_list:
            sum += self.num_tree[idx]

        print(f"[{start} ~ {end}] 구간합 : {sum}")


if __name__ == "__main__":
    num_list: List[int] = [1, 3, 4, 2, 6, 3, 6, 8]

    obj = SegmentTree()
    obj.init_tree(num_list)

    obj.area_sum(3, 7)
