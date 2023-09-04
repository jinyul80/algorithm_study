from typing import List
from queue import PriorityQueue


class MinimumSpanningTree:
    """
    최소 신장 트리: 최소의 비용으로 모든 노드를 연결
    """

    def __init__(self):
        super().__init__()
        self.parent: List[int] = []

    def mst(self, node_count: int, edge_list: List[List[int]]):
        # 가중치 기준 정렬된 에지 리스트 생성
        pq = PriorityQueue()
        for edge in edge_list:
            s, e, w = edge
            pq.put((w, s, e))  # 첫 번째 값을 기준으로 정렬됨

        # 대표 리스트 생성
        self.parent = [x for x in range(node_count + 1)]

        # 사용된 edge 개수
        edge_count = 0
        # 적용된 가중치 합계
        weight_sum = 0

        while edge_count < node_count - 1:
            # 가중치가 제일 작은 edge 정보 부터 순차 반복
            w, s, e = pq.get()

            # 시작노드와 종료노드의 대표노드가 다르면(연결되지 않았다면) 연결
            if self.__find(s) != self.__find(e):
                self.__union(s, e)
                edge_count += 1
                weight_sum += w

        print(f"가중치 합: {weight_sum}")

    def __union(self, a: int, b: int):
        """
        두 노드의 대표 노드가 다르면 연결
        Args:
            a: 첫 번째 노드
            b: 두 번째 노드

        Returns: None

        """
        a = self.__find(a)
        b = self.__find(b)

        if a != b:
            self.parent[b] = a

    def __find(self, a: int):
        """
        노드의 대표 노드 정보를 조회
        Args:
            a: 노드 인덱스

        Returns: 대표 노드 인덱스

        """
        if a == self.parent[a]:
            return a
        else:
            self.parent[a] = self.__find(self.parent[a])
            return self.parent[a]


if __name__ == "__main__":
    node_count = 3
    edge_list = [
        [1, 2, 2],
        [1, 3, 5],
        [2, 3, 2],
    ]

    obj = MinimumSpanningTree()
    obj.mst(node_count, edge_list)
