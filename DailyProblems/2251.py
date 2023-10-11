import heapq
from typing import List

class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        sorted_flowers = sorted(flowers, reverse=True)

        flowers_end_time_min_heap = []
        result = [0 for _ in range(len(people))]

        sorted_people_with_index = sorted(enumerate(people), key=lambda x: x[1])
        print(sorted_people_with_index)

        for index, person in sorted_people_with_index:
            while sorted_flowers and sorted_flowers[-1][0] <= person:
                flower = sorted_flowers.pop()
                heapq.heappush(flowers_end_time_min_heap, flower[1])

            while flowers_end_time_min_heap and flowers_end_time_min_heap[0] < person:
                heapq.heappop(flowers_end_time_min_heap)

            result[index] = len(flowers_end_time_min_heap)

        return result

if __name__ == '__main__':
    sol = Solution()
    flowers = [[1,10], [3,3]]
    people = [3, 3, 2]
    print(sol.fullBloomFlowers(flowers, people))
