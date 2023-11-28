class Solution:
    def numberOfWays(self, corridor: str) -> int:
        seat_index = -1
        result = 1
        k = 0
        MOD = 10 ** 9 + 7

        N = len(corridor)

        for i in range(N):
            if corridor[i] == "P":
                k += 1

            if corridor[i] == "S":
                seat_index += 1

                if seat_index > 0 and seat_index % 2 == 0:
                    result *= (k + 1)
                    result %= MOD

                k = 0

        number_of_seats = seat_index + 1

        if number_of_seats == 0 or number_of_seats % 2 == 1:
            return 0

        return result


if __name__ == '__main__':
    sol = Solution()
    corridor = "SSPPSPS"
    result = sol.numberOfWays(corridor)
    print(result)
