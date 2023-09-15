import heapq


class Solution:
    def minCostConnectPoints(self, coordinates):
        number_of_points = len(coordinates)
        points = []
        max_distance = 0
        for index, coordinate in enumerate(coordinates):
            neighbor_indexes_and_weights = []
            for other_index in range(number_of_points):
                if other_index == index:
                    continue
                distance = Solution.calculate_distance(coordinate, coordinates[other_index])
                max_distance = max(max_distance, distance)
                neighbor_indexes_and_weights.append((other_index, distance))

            points.append(Point(neighbor_indexes_and_weights))

        return PrimAlgorithm.find_minimum_span_tree_weights(points, max_distance)

    @staticmethod
    def calculate_distance(coordinate1, coordinate2):
        return abs(coordinate1[0] - coordinate2[0]) + abs(coordinate1[1] - coordinate2[1])


class Point:
    def __init__(self, neighbor_indexes_and_weights):
        self.neighbor_indexes_and_weights = neighbor_indexes_and_weights


class PrimAlgorithm:
    @staticmethod
    def find_minimum_span_tree_weights(points, max_distance):
        if not points:
            return 0

        number_of_points = len(points)
        processed_points = [False for _ in range(number_of_points)]
        weight_of_edge_to_point = [max_distance for _ in range(number_of_points)]

        prim_edges_min_heap = []
        start_point_index = 0
        heapq.heappush(prim_edges_min_heap, PrimEdge(start_point_index, 0))
        weight_of_edge_to_point[start_point_index] = 0

        while prim_edges_min_heap:
            edge = heapq.heappop(prim_edges_min_heap)
            cur_point_index = edge.point_index
            if processed_points[cur_point_index]:
                continue

            processed_points[cur_point_index] = True

            for neighbor_index, weight in points[cur_point_index].neighbor_indexes_and_weights:
                if weight < weight_of_edge_to_point[neighbor_index] and not processed_points[neighbor_index]:
                    weight_of_edge_to_point[neighbor_index] = weight
                    heapq.heappush(prim_edges_min_heap, PrimEdge(neighbor_index, weight))

        return sum(weight_of_edge_to_point)


class PrimEdge:
    def __init__(self, point_index, weight):
        self.point_index = point_index
        self.weight = weight

    def __lt__(self, other):
        return self.weight < other.weight


if __name__ == '__main__':
    sol = Solution()
    coordinates = [[0,0],[2,2],[3,10],[5,2],[7,0]]
    result = sol.minCostConnectPoints(coordinates)
