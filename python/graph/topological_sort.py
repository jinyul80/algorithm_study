from typing import List


class TopologicalSort:
    """
    위상 정렬 - 사이클이 없는 방향 그래프의 모든 노드 방향성을 거스르지 않도록 순서대로 정렬
    """

    def __init__(self):
        super().__init__()

    def sort(self, node_count: int, edge_list: List[List[int]]):
        """
        위상 정렬 실행

        Args:
            node_count: Node 개수
            edge_list: edge 정보 리스트

        Returns: None

        """
        # 인접 리스트 초기화
        A: List[List[int]] = [[] for x in range(node_count + 1)]

        # 진입차수 리스트 초기화
        indegree: List[int] = [0 for x in range(node_count + 1)]

        # edge 정보로 인접리스트 및 진입차수 초기화
        for edge in edge_list:
            s = edge[0]
            e = edge[1]
            A[s].append(e)
            indegree[e] += 1

        # 진입차수가 '0' 인 node를 queue에 추가
        queue: List[int] = []
        for idx in range(1, node_count + 1):
            if indegree[idx] == 0:
                queue.append(idx)

        result: List[int] = []

        # 큐가 있는 동안 반복
        while len(queue) > 0:
            # 큐에서 처음 값 꺼내기
            now = queue.pop(0)
            result.append(now)

            # 현재 노드의 연결된 노드들 반복
            for next_idx in A[now]:
                # 다음 노드의 진입차수를 1 빼기
                indegree[next_idx] -= 1

                # 다음 노드의 진입차수가 0이면 큐에 추가
                if indegree[next_idx] == 0:
                    queue.append(next_idx)

        # 정렬 결과 출력
        print(result)


if __name__ == "__main__":
    node_count = 4
    edge_list = [[4, 2], [3, 1]]

    obj = TopologicalSort()
    obj.sort(node_count, edge_list)

    node_count = 3
    edge_list = [[2, 3], [1, 2]]

    obj.sort(node_count, edge_list)
