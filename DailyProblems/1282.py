from typing import List

class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups_with_size = dict()

        for i, size in enumerate(groupSizes):
            if size not in groups_with_size:
                groups_with_size[size] = [[]]
            
            cur_group = groups_with_size[size][-1]
            cur_group.append(i)

            if len(cur_group) == size:
                groups_with_size[size].append([])
        
        result = []
        for size, groups in groups_with_size.items():
            for group in groups:
                if len(group) == 0:
                    continue 

                result.append(group)
        
        return result 

if __name__ == '__main__':
    sol = Solution()
    groupSizes = [1]
    result = sol.groupThePeople(groupSizes)
    print(result)