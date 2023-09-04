class Solution:
    def furthestDistanceFromOrigin(self, moves: str) -> int:
        right_moves = 0
        left_moves = 0
        empty_moves = 0

        for i, move in enumerate(moves):
            if move == "R":
                right_moves += 1
            if move == "L":
                left_moves += 1
            if move == "_":
                empty_moves += 1

        return abs(right_moves - left_moves) + empty_moves


if __name__ == '__main__':
    sol = Solution()
    moves = "L_RL__R"
    result = sol.furthestDistanceFromOrigin(moves)
    print(result)
