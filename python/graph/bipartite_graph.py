from typing import List


class BipartiteGraph:
    """
    이분 그래프 : 인접한 노드끼리 서로 다른 색으로 칠해서 모든 정점을 두가지 색으로만 칠할 수 있는 그래프
    """

    def __init__(self):
        super().__init__()

        self.visited: List[bool] = []
        self.check: List[int] = []
        self.isEven = True
        self.A: List[List[int]] = []

    def is_bipartite(self, V: int, E: int, edge_list: List[List[int]]):
        # 체크 결과 초기화
        self.isEven = True

        # 방문 리스트 및 분류 리스트 초기화
        self.visited = [False for x in range(V + 1)]
        self.check = [0 for x in range(V + 1)]

        # 인접 리스트 초기화
        self.A = [[] for x in range(V + 1)]

        # 인접 리스트에 에지 정보 추가
        for edge in edge_list:
            s = edge[0]
            e = edge[1]

            self.A[s].append(e)
            self.A[e].append(s)

        # 모든 노드에 대해서 체크
        for idx in range(1, V + 1):
            if self.isEven:
                self.DFS(idx)
            else:
                break

        return self.isEven

    def DFS(self, start):
        # 현재 노드 방문 표시
        self.visited[start] = True

        for next in self.A[start]:
            # 체크 결과가 False이면 추가 검사 안함
            if not self.isEven:
                return

            # 다음 노드가 방문하지 않은 노드인 경우만 체크
            if not self.visited[next]:
                # 다음 노드의 분류를 설정
                self.check[next] = (self.check[start] + 1) % 2
                self.DFS(next)

            else:
                # 다음 노드가 이미 방문한 노드인 경우
                # 현재 노드의 분류와 다음 노드의 분류가 같으면 False
                if self.check[start] == self.check[next]:
                    self.isEven = False
