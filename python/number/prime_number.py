import math


class PrimeNumber:
    def __init__(self):
        super().__init__()

    def print_prime_numbers(self, start: int, end: int):
        """
        입력된 두 수 사이의 소수를 출력
        Args:
            start: 시작 숫자
            end: 종료 숫자
        Returns: None
        """

        # 숫자 리스트 형성
        num_list = [x for x in range(end + 1)]

        for i in range(2, int(math.sqrt(end))):
            for j in range(i * 2, end + 1, i):
                if num_list[j] == 0:
                    continue

                num_list[j] = 0

        for i in range(start, end + 1):
            if num_list[i] != 0:
                print(num_list[i])


if __name__ == "__main__":
    start = 3
    end = 16

    obj = PrimeNumber()
    obj.print_prime_numbers(start, end)
