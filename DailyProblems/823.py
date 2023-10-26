from typing import List
from functools import lru_cache

import math

class Solution:
    def numFactoredBinaryTrees(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        number_of_nodes = len(arr)
        sorted_arr = sorted(arr)
        set_arr = set(arr)

        @lru_cache(maxsize=number_of_nodes)
        def count_binary_trees(root_value: int) -> int:
            result = 1

            for node in sorted_arr:
                if node > math.sqrt(root_value):
                    break

                if root_value % node != 0:
                    continue

                other_node = root_value // node
                if other_node not in set_arr:
                    continue

                addition_trees = (count_binary_trees(node) * count_binary_trees(other_node)) % MOD

                if other_node != node:
                    addition_trees *= 2
                    addition_trees %= MOD

                result += addition_trees
                result %= MOD

            return result

        number_of_binary_trees = 0
        for node in sorted_arr:
            number_of_binary_trees += count_binary_trees(node)
            number_of_binary_trees %= MOD

        return number_of_binary_trees


if __name__ == '__main__':
    sol = Solution()
    arr = [2, 3]
    result = sol.numFactoredBinaryTrees(arr)
    print(result)



