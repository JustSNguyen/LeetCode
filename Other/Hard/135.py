from typing import List 

class Solution:
    def candy(self, ratings: List[int]) -> int:
        number_of_kids = len(ratings)
        longest_decreasing_sequence_from = [-1 for _ in range(number_of_kids)]

        def find_longest_decreasing_sequence_from(index):
            if index >= number_of_kids:
                return 0 

            if longest_decreasing_sequence_from[index] != -1:
                return longest_decreasing_sequence_from[index]
            
            next_index = index + 1
            if index == number_of_kids - 1 or ratings[next_index] >= ratings[index]:
                longest_decreasing_sequence_from[index] = 1 

            else:
                longest_decreasing_sequence_from[index] = 1 + find_longest_decreasing_sequence_from(next_index)
            
            return longest_decreasing_sequence_from[index]

        result = [1 for _ in range(number_of_kids)]

        for i in range(number_of_kids):
            result[i] = 1
            if i - 1 >= 0 and ratings[i] > ratings[i - 1]:
                result[i] = result[i - 1] + 1 

            longest_decreasing_sequence_from_cur_index = find_longest_decreasing_sequence_from(i)
            result[i] = max(result[i], longest_decreasing_sequence_from_cur_index)

        return sum(result)

if __name__ == "__main__":
    ratings = [1, 9, 4, 6, 7 ]
    sol = Solution()
    result = sol.candy(ratings)
    print(result)
