from typing import List 
from collections import defaultdict

class DetectSquares:
    def __init__(self):
        self.points_by_x = defaultdict(list)
        self.points_by_y = defaultdict(list)
        

    def add(self, point: List[int]) -> None:
        x, y = point 
        self.points_by_x[x].append(y)
        self.points_by_y[y].append(x)


    def count(self, point: List[int]) -> int:
        result = 0 
        heights = defaultdict(int)

        x1, y1 = point 
        for y2 in self.points_by_x[x1]:
            if y2 - y1 == 0: continue 
            heights[y2 - y1] += 1 
        
        for x2 in self.points_by_y[y1]:
            width = x2 - x1 
            for y2 in self.points_by_x[x2]:
                height = y2 - y1 

                if abs(width) != abs(height):
                    continue 

                result += heights[y2 - y1]
        
        return result 
    
if __name__ == '__main__':
    detect = DetectSquares()
    detect.add([5, 10])
    detect.add([10, 5])
    detect.add([10, 10])
    detect.add([3, 0])
    detect.add([8, 0])
    detect.add([8, 5])
    detect.add([9, 0])
    detect.add([9, 8])
    detect.add([1, 8])
    detect.add([0, 0])
    detect.add([8, 0])
    detect.add([8, 8])
    result = detect.count([0, 8])
    print(result)

