from typing import List 
from collections import defaultdict
import math 

class DetectSquares:
    def __init__(self):
        self.points = defaultdict(int)
        
    def add(self, point) -> None:
        self.points[point] += 1 

    def find_symmetric(self, point, mid_point):
        symmetric_x = mid_point[0] + (mid_point[0] - point[0])
        symmetric_y = mid_point[1] + (mid_point[1] - point[1])
        return (symmetric_x, symmetric_y)

    def find_mid_point(self, point1, point2):
        mid_x = (point1[0] + point2[0]) / 2
        mid_y = (point1[1] + point2[1]) / 2 
        return (mid_x, mid_y)
    
    def find_distance(self, point1, point2):
        return math.sqrt((point1[0] - point2[0])**2 + (point1[1] - point2[1])**2)
    
    def find_slope(self, point1, point2):
        INF = 10**8 
        delta_y = point1[1] - point2[1]
        delta_x = point1[0] - point2[0]
        if delta_x == 0:
            return INF 
        return delta_y / delta_x
    
    def find_perpendicular_slope(self, slope):
        INF = 10**8 
        if slope == 0: 
            return INF 
        
        if slope == INF:
            return 0 
        
        return -1 / slope

    def count(self, point1) -> int:
        result = 0 
        slopes = dict()

        for point2 in self.points:
            slope = self.find_slope(point1, point2)
            distance = self.find_distance(point1, point2)
            if slope not in slopes:
                slopes[slope] = dict()
            
            slopes[slope][distance] = point2
            
        for slope in slopes:
            perpendicular_slope = self.find_perpendicular_slope(slope)
            if perpendicular_slope not in slopes:
                continue 

            for distance in slopes[slope]:
                if distance not in slopes[perpendicular_slope]:
                    continue 

                point2 = slopes[slope][distance]
                point3 = slopes[perpendicular_slope][distance]
                mid_point = self.find_mid_point(point2, point3)
                symmetric_point = self.find_symmetric(point1, mid_point)
                if symmetric_point not in self.points:
                    continue 

                number_of_point2 = self.points[point2]
                number_of_point3 = self.points[point3]
                number_of_symmetric_point = self.points[symmetric_point]

                result += number_of_point2 * number_of_point3 * number_of_symmetric_point
        
        return result / 2 
    
if __name__ == '__main__':
    detect = DetectSquares()
    detect.add((4, 6))
    detect.add((4, 2))
    detect.add((6, 4))
    detect.add((6, 4))
    detect.add((2, 7))
    detect.add((5, 4))
    detect.add((5, 7))
    # detect.add([5, 10])
    # detect.add([10, 5])
    # detect.add([10, 10])
    # detect.add([3, 0])
    # detect.add([8, 0])
    # detect.add([8, 5])
    # detect.add([9, 0])
    # detect.add([9, 8])
    # detect.add([1, 8])
    # detect.add([0, 0])
    # detect.add([8, 0])
    # detect.add([8, 8])
    result = detect.count((2, 4))
    print(result)

