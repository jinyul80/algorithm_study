from typing import List


class UnionFind:
    """
    유니온 파인드 : 두 노드가 같은 그룹 인지 체크
    """

    def __init__(self):
        super().__init__()
        self.parent: List[int] = []

    def union(self, node_count: int, edge_list: List[List[int]]):
        """
        유니온 연산 : 두 노드의 대표 노드끼리 연결
        Args:
            node_count: 노드의 개수
            edge_list: edge 정보 리스트

        Returns: None

        """
        # 대표 노드 리스트
        self.parent = [x for x in range(node_count + 1)]

        # edge 연결
        for edge in edge_list:
            # 각 노드의 대표 노드를 조회
            a = self.__find(edge[0])
            b = self.__find(edge[1])

            # 각 노드의 대표 노드가 다르면 대표 노드를 연결
            if a != b:
                self.parent[b] = a

    def __find(self, idx: int):
        """
        노드의 대표 노드를 조회
        Args:
            idx: 노드의 인덱스

        Returns: 노드의 대표 노드 인덱스

        """
        if self.parent[idx] == idx:
            # 현재 노드의 대표노드가 자신이라면 자신의 인덱스 리턴
            return idx
        else:
            # 대표 노드가 자신이 아닌 경우 현재 노드의 대표노드로 find 연산 다시 실행
            self.parent[idx] = self.__find(self.parent[idx])
            return self.parent[idx]

    def check_same(self, first: int, second: int):
        """
        두 노드의 대표 노드가 동일한지 체크
        Args:
            first: 첫 번째 노드
            second: 두 번째 노드

        Returns: 대표 노드의 동일 여부. True or False

        """
        a = self.__find(first)
        b = self.__find(second)

        if a == b:
            return True
        else:
            return False


if __name__ == "__main__":
    N = 7

    edge_list = [[1, 3], [7, 6], [3, 7], [4, 2], [1, 1]]
    q_list = [[1, 7], [1, 5], [2, 6]]

    obj = UnionFind()
    obj.union(N, edge_list)

    for q in q_list:
        result = obj.check_same(q[0], q[1])
        if result:
            print("YES")
        else:
            print("NO")
