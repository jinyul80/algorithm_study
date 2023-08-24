from typing import List


class Bfs:
    def __init__(self):
        super().__init__()

        # 미로
        self.A: List[List[int]] = [[]]
        # 미로 방문 여부 리스트
        self.visited: List[List[bool]] = [[]]

        # 현재 위치에서 다음 위치를 찾기 위한 리스트
        self.dx = [1, 0, -1, 0]
        self.dy = [0, -1, 0, 1]

    def search(self, row: int, col: int, grid: List[List[int]]):
        """
        0,0 에서 row, col 위치까지 가장 빠른 길 탐색
        Args:
            row: 미로의 행 개수
            col: 미로의 열 개수
            grid: 미로 행열 리스트

        Returns: None

        """
        self.A = grid
        self.visited = [[False for x in range(col)] for y in range(row)]

        self.__bfs(row, col, [0, 0])

        print(f"최소 이동 횟수: {self.A[row - 1][col - 1]}")
        for line in self.A:
            print(line)

    def __bfs(self, row: int, col: int, cur: List[int]):
        """
        너비 우선 탐색 기법으로 미로 최단거리 탐색
        Args:
            row: 미로의 행 개수
            col: 미로의 열 개수
            cur: 초기 위치

        Returns: None

        """

        # 큐 생성 및 초기 위치 추가
        queue: List[List[int]] = [cur]
        # 초기 위치 방문으로 설정
        self.visited[0][0] = True

        # 큐가 비어있을 때까지 반복
        while len(queue) != 0:
            now = queue.pop()

            for i in range(4):
                nx = now[1] + self.dx[i]
                ny = now[0] + self.dy[i]

                # 다음 위치가 미로 행열 내부 좌표인지 체크
                if nx >= 0 and ny >= 0 and nx < col and ny < row:
                    # 다음 위치가 갈 수 있는 곳인지 and 방문하지 않은 곳인지 체크
                    if self.A[ny][nx] != 0 and not self.visited[ny][nx]:
                        queue.append([ny, nx])
                        self.visited[ny][nx] = True
                        # 다음 위치가 몇번째 깊이(depth)인지 기록
                        self.A[ny][nx] = self.A[now[0]][now[1]] + 1


if __name__ == "__main__":
    # 미로 크기
    row = 6
    col = 7

    # 미로 배열 생성
    grid = [
        [1, 1, 0, 0, 1, 0, 1],
        [1, 1, 0, 0, 1, 1, 1],
        [0, 1, 1, 1, 0, 1, 0],
        [1, 1, 0, 1, 1, 1, 0],
        [1, 0, 0, 0, 1, 0, 0],
        [1, 1, 0, 0, 1, 1, 1],
    ]

    obj = Bfs()
    obj.search(row, col, grid)
