from point import Point
import sys


class SimpleCalculator:
    """
    Class implements a brute force approach to n dimensional closest pair problem.
    """

    def __init__(self):
        pass

    def get_minimum_distance_pair(self, points, dimension):
        """
        This function determines the closest n dimension points using brute force method.
        :param points: points (list)
        :param dimension: dimension (int)
        :return: position of closest n dimension pair in list (tuple)
        """
        min_dist = sys.float_info.max
        n = len(points)
        if n % dimension != 0:
            raise Exception('Minimum distance pair cannot be calculated: dimension error!')
        for i in range(0, n, dimension):
            j = i + dimension
            while j < n:
                dist = Point.get_pair_distance(points[i:i + dimension], points[j:j + dimension])
                if dist < min_dist:
                    min_dist = dist
                    pair_idx_start = (i, j)
                j += dimension
        # position of point group in sequence
        pair_pos = (pair_idx_start[0] / dimension, pair_idx_start[1] / dimension)
        return pair_pos
