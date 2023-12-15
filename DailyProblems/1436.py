from typing import List

class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        out = dict()
        for path in paths:
            start, end = path

            if start not in out:
                out[start] = 1

            out[start] += 1

            if end not in out:
                out[end] = 0

        for city in out:
            if out[city] == 0:
                return city

