from typing import List

class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        for i in range(len(target)):
            exist = False
            for triplet in triplets:
                valid = True
                for j in range(len(triplet)):
                    if j != i and triplet[j] > target[j]:
                        valid = False
                        break

                    if j == i and triplet[j] != target[j]:
                        valid = False
                        break

                if valid:
                    exist = True

                if exist:
                    break

            if not exist:
                return False

        return True