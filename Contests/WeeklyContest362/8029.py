from typing import List

class Solution:
    def numberOfPoints(self, cars: List[List[int]]) -> int:
        covered = dict()

        for car in cars:
            start, end = car 
            for i in range(start, end + 1):
                covered[i] = True 
        
        return len(covered)
        