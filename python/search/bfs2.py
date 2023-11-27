class BFS:
    """BFS는 너비 우선 탐색이라고도 부르며, 그래프에서 가까운 노드부터 우선적으로 탐색하는 알고리즘이다"""

    def __init__(self):
        super().__init__()
        self._visited: list[bool] = []

    def search(self, node_list: list[list[int]], start: int):
        # 각 노드의 방문 배열 생성
        self._visited = [False] * len(node_list)

        # 시작 index 큐에 삽입
        queue = [start]

        # 시작 index 방문 처리
        self._visited[start] = True

        while len(queue):
            # 큐에서 Node 가져오기
            idx = queue.pop(0)

            # Node 방문 순서를 출력
            print(idx, end=" ")

            for n in node_list[idx]:
                if not self._visited[n]:
                    queue.append(n)
                    self._visited[n] = True


test_case = [[], [2, 3, 8], [1, 7], [1, 4, 5], [3, 5], [3, 4], [7], [2, 6, 8], [1, 7]]

bfs = BFS()
bfs.search(test_case, 1)
