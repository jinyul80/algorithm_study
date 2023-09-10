import sys
from typing import List

sys.setrecursionlimit(10**6)


class BinaryTree:
    """
    트리의 부모 노드 찾기
    """

    def __init__(self):
        super().__init__()

        # 변수 선언
        self._visited: List[bool] = []
        self._tree: List[List[int]] = []
        self._parent: List[int] = []

    def parent_print(self, n: int, edge_list: List[List[int]]):
        """
        트리의 부모 노드 찾기
        Args:
            n: 노드의 개수
            edge_list: edge 정보 리스트

        Returns: None

        """
        # 변수 초기화
        self._visited = [False for _ in range(n + 1)]
        self._tree = [[] for _ in range(n + 1)]
        self._parent = [0 for _ in range(n + 1)]

        # edge 정보로 인접 리스트 생성
        for edge in edge_list:
            self._tree[edge[0]].append(edge[1])
            self._tree[edge[1]].append(edge[0])

        # DFS 재귀함수 실행
        # 루트 노드는 1로 고정
        self.__dfs__(1)

        # 2번 인덱스부터 부모노드 정보 출력
        for i in range(2, n + 1):
            print(self._parent[i])

    def __dfs__(self, idx):
        """
        입력된 노드의 자식 노드들 재귀적 탐색
        Args:
            idx: 노드의 인덱스

        Returns: None

        """
        # 현재 노드를 방문으로 저장
        self._visited[idx] = True

        # 연결된 노드에 대해서 반복 탐색
        for next_idx in self._tree[idx]:
            # 방문하지 않은 노드인 경우만 실행
            if not self._visited[next_idx]:
                self._parent[next_idx] = idx
                self.__dfs__(next_idx)


if __name__ == "__main__":
    node_count = 7
    edge_list = [
        [1, 6],
        [6, 3],
        [3, 5],
        [4, 1],
        [2, 4],
        [4, 7],
    ]

    obj = BinaryTree()
    obj.parent_print(node_count, edge_list)
