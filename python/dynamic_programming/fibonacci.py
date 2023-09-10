from typing import List


class Fibonacci:
    """
    피보나치 수열 : 현재 값은 바로 앞 2자리의 합
    """

    def __init__(self):
        super().__init__()

        self.D: List[int] = []

    def top_down(self, n: int):
        """
        Top down방식 - 문제의 위치부터 찾아가는 방식
        Args:
            n: 출력할 피보나치 수열 위치

        Returns: None

        """
        # 리스트 초기화
        self.D = [-1 for _ in range(n + 1)]
        self.D[0] = 0
        self.D[1] = 1

        # 재귀함수 방식으로 수열 계산
        self.__fibon(n)

        print(f"List: {self.D}")
        print(f"Top down : {self.D[n]}")

    def __fibon(self, n: int):
        # 초기값이 아닌 경우는 재귀함수 탈출
        if self.D[n] != -1:
            return self.D[n]

        # 재귀함수 호출
        self.D[n] = self.__fibon(n - 1) + self.__fibon(n - 2)

        return self.D[n]

    def bottom_up(self, n: int):
        """
        Bottom up 방식 - 작은 단위부터 점점 큰 범위의 문제로 해결하는 방식
        Args:
            n: 출력할 피보나치 수열 위치

        Returns: None

        """
        # 리스트 초기화
        D = [-1 for _ in range(n + 1)]
        D[0] = 0
        D[1] = 1

        # 반복문으로 문제 해결
        for idx in range(2, n + 1):
            D[idx] = D[idx - 1] + D[idx - 2]

        print(f"Bottom up : {self.D[n]}")


if __name__ == "__main__":
    n = 20

    obj = Fibonacci()
    obj.top_down(n)
    obj.bottom_up(n)
