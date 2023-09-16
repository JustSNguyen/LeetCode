from functools import lru_cache


class Solution:
    def candy(self, ratings):
        number_of_children = len(ratings)

        @lru_cache(maxsize=number_of_children)
        def longest_strictly_decreasing_sequence_starts_at(index):
            if index == number_of_children - 1 or ratings[index] <= ratings[index + 1]:
                return 1

            return 1 + longest_strictly_decreasing_sequence_starts_at(index + 1)

        candy_for_children = [1 for _ in range(number_of_children)]
        for i in range(number_of_children):
            previous_candy_for_children = 0
            previous_rating = 0
            if i > 0:
                previous_candy_for_children = candy_for_children[i - 1]
                previous_rating = ratings[i - 1]

            current_rating = ratings[i]
            if current_rating > previous_rating:
                candy_for_children[i] = 1 + previous_candy_for_children

            candy_for_children[i] = max(candy_for_children[i], longest_strictly_decreasing_sequence_starts_at(i))

        return sum(candy_for_children)


if __name__ == '__main__':
    ratings = [1, 2, 3, 2, 1, 0]
    sol = Solution()
    result = sol.candy(ratings)
    print(result)
