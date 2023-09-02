import sys
from typing import List, Tuple
from queue import PriorityQueue


class Dijkstra:
    """
    다익스트라 알고리즘 : 최단 경로 문제에 활용
    (모든 Edge 가중치가 양수만 있어야 함)
    Start 노드를 기준으로 모든 노드에 대한 최단 거리(가중치)를 각각 계산
    """

    def __init__(self):
        super().__init__()

    def search(self, node_count: int, edge_list: List[List[int]], start: int, end: int):
        """
        시작 노드에서 목적 노드까지의 최단 거리를 계산
        Args:
            node_count: 노드의 개수
            edge_list: edge 정보 리스트
            start: 시작 노드
            end: 종료 노드

        Returns: None

        """
        # 인접 리스트 생성
        A: List[List[Tuple[int, int]]] = [[] for x in range(node_count + 1)]

        for edge in edge_list:
            s: int = edge[0]  # 시작 노드
            e: int = edge[1]  # 다음 노드
            value: int = edge[2]  # 가중치
            A[s].append((e, value))

        # 방문 배열 생성
        visited: List[int] = [False for x in range(node_count + 1)]

        # 최단 경로 추적 배열 생성
        prev: List[int] = [-1 for x in range(node_count + 1)]

        # 최단 거리 배열 생성(시작 노드부터 각 노드까지 누적된 최단 거리값)
        dist: List[int] = [sys.maxsize for x in range(node_count + 1)]
        dist[start] = 0

        # 우선순위 큐 생성(처음 인덱스를 기준으로 정렬되므로 (가중치, 노드번호) 순으로 추가
        queue = PriorityQueue()
        queue.put((0, start))

        while queue.qsize() > 0:
            # 가중치가 제일 작은 노드를 찾아서 반복
            cur = queue.get()
            cur_idx = cur[1]

            # 현재 노드 방문처리
            visited[cur_idx] = True

            # 현재 노드의 연결된 노드들 반복
            for next_info in A[cur_idx]:
                next_idx = next_info[0]
                next_val = next_info[1]

                # 현재 노드+가중치가 다음 노드의 최단 거리값보다 작으면
                # 다음 노드 최단 거리값 업데이트
                # 추적 배열 다음 노드의 값으로 현재 노드값을 저장
                if (dist[cur_idx] + next_val) < dist[next_idx]:
                    dist[next_idx] = dist[cur_idx] + next_val
                    prev[next_idx] = cur_idx

                    # 다음 노드가 방문하지 않은 노드인 경우 큐에 추가
                    if not visited[next_idx]:
                        queue.put((dist[next_idx], next_idx))

        # 결과 출력
        print("최단거리 배열:", dist[1:])
        print("경로추적 배열:", prev[1:])

        # 목적 노드까지의 최단 경로
        path = [end]
        idx = end

        while prev[idx] != -1:
            path.append(prev[idx])
            idx = prev[idx]

        path.reverse()
        print("최단 경로:", path)
        print("최단 거리:", dist[end])


if __name__ == "__main__":
    node_count = 6
    edge_list = [
        [1, 2, 2],
        [1, 3, 5],
        [1, 4, 1],
        [2, 3, 3],
        [2, 4, 2],
        [3, 6, 5],
        [3, 2, 3],
        [4, 3, 3],
        [4, 5, 1],
        [5, 3, 1],
        [5, 6, 2],
    ]

    obj = Dijkstra()
    obj.search(node_count, edge_list, 1, 3)
