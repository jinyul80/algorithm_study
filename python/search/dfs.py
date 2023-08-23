from typing import List


class Dfs:
    def __init__(self):
        super().__init__()

        from typing import List

        self.link_list: List[List[int]] = []
        self.visited: List[bool] = []

    def search(self, node_count: int, edge_list: List[List[int]]):
        """
        노드 개수와 연결 리스트를 입력받아 그래프의 개수를 검색
        Args:
            node_count: 노드의 개수
            edge_list: 노드간 연결 리스트

        Returns: None

        """
        # 노드 연결 리스트 생성
        self.link_list = [[] for x in range(node_count + 1)]
        for s, e in edge_list:
            # 방향성이 없어서 양방향으로 연결 정보 추가
            self.link_list[s].append(e)
            self.link_list[e].append(s)

        # 노드 방문 리스트 생성
        self.visited = [False for x in range(node_count + 1)]

        # 그래프의 개수
        count = 0

        # 노드 리스트를 순차 적으로 반복
        for idx in range(1, node_count + 1):
            # 방문하지 않은 노드인 경우만 실행
            if not self.visited[idx]:
                count += 1
                self.__dfs(idx)

        print(f"그래프 개수: {count}")

    def __dfs(self, idx: int):
        """
        노드 인덱스를 입력받아 연결된 노드들을 검색하는 재귀함수
        Args:
            idx: 노드의 인덱스

        Returns: None

        """
        # 이미 방문한 노드인 경우
        if self.visited[idx]:
            return

        # 현재 노드를 방문한 노드로 설정
        self.visited[idx] = True

        # 현재 노드의 연결된 노드들을 방문
        for link_idx in self.link_list[idx]:
            self.__dfs(link_idx)


if __name__ == "__main__":
    # 노드의 개수
    node_count = 6
    # 노드 연결 리스트
    link_list: List[List[int]] = [[1, 2], [2, 5], [5, 1], [3, 4], [4, 6]]

    obj = Dfs()
    obj.search(node_count, link_list)
