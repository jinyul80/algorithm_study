import sys
from typing import List


class FloydWarshall:
    """
    플로이드 워셜 알고리즘 : 최단 경로 문제에 활용
    (가중치에 음수가 있어도 사용 가능, 단 음수 사이클이 있으면 안됨)
    모든 노드간에 최단 거리값 계산(노드의 개수가 너무 크면 안됨)
    """

    def __init__(self):
        super().__init__()

    def floyd(self, node_count: int, edge_list: List[List[int]]):
        """
        플로이드 워셜 실행
        Args:
            node_count: 노드의 개수
            edge_list: edge 정보 리스트

        Returns:

        """
        # 인접 행렬 생성
        distance = [
            [sys.maxsize for _ in range(node_count + 1)] for _ in range(node_count + 1)
        ]

        # 경로 기록용 행렬
        # 목표 노드에 최소 가중치로 도달하기 위하여 다음에 가야할 노드번호
        next_node = [[0 for _ in range(node_count + 1)] for _ in range(node_count + 1)]

        # 자기 자신과의 값은 0으로 설정
        for i in range(1, node_count + 1):
            distance[i][i] = 0

        # edge 정보로 인접 행렬 업데이트
        for edge in edge_list:
            s, e, v = edge

            # 중복 edge가 있는 경우 가중치가 작은 값으로 업데이트
            if distance[s][e] > v:
                distance[s][e] = v
                next_node[s][e] = e

        # 플로이드 워셜 알고리즘 실행
        for k in range(1, node_count + 1):
            for s in range(1, node_count + 1):
                for e in range(1, node_count + 1):
                    # 직접 연결보다 경유지를 거치는 가중치가 더 적은 경우 인접 행열 업데이트
                    if distance[s][e] > distance[s][k] + distance[k][e]:
                        distance[s][e] = distance[s][k] + distance[k][e]
                        next_node[s][e] = next_node[s][k]

        # 결과 출력
        print("*최단 거리 테이블")
        for s in range(1, node_count + 1):
            for e in range(1, node_count + 1):
                if distance[s][e] == sys.maxsize:
                    # 갈수 없는 노드는 '0' 출력
                    print(f"{0:2}", end=" ")
                else:
                    print(f"{distance[s][e]:2}", end=" ")

            # 줄바꿈
            print("")

        print("\n*경로 추적 테이블")
        for s in range(1, node_count + 1):
            for e in range(1, node_count + 1):
                print(next_node[s][e], end=" ")

            # 줄바꿈
            print()

        # 경로 출력
        print()
        for s in range(1, node_count + 1):
            for e in range(1, node_count + 1):
                if distance[s][e] == sys.maxsize or distance[s][e] == 0:
                    print(f"[{s} - {e}] : 0")
                else:
                    path = [s]
                    cur = s

                    while cur != e:
                        path.append(next_node[cur][e])
                        cur = next_node[cur][e]

                    print(f"[{s} - {e}] : {' > '.join(map(str,path))}")


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

    # node_count = 5
    # edge_list = [
    #     [1, 2, 5],
    #     [1, 3, 2],
    #     [2, 5, 3],
    #     [2, 4, 6],
    #     [3, 4, 4],
    #     [3, 5, 1],
    #     [4, 5, 7],
    # ]

    obj = FloydWarshall()
    obj.floyd(node_count, edge_list)
