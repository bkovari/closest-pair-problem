import math


class Point:
    """
    Class is responsible for the model used in calculations.
    """

    def __init__(self, points):
        self.points = points
        self.dimension = None

    @staticmethod
    def get_pair_distance(p1, p2):
        """
        This function calculates the Euclidean distance of n dimension points.
        :param p1: point1
        :param p2: point2
        :return: Distance of p1 and p2 the points.
        """
        if len(p1) == len(p2):
            n = len(p1)
            p_sum = 0
            for i in range(0, n):
                p_sum += (p1[i] - p2[i]) ** 2
            return math.sqrt(p_sum)
        raise Exception('Distance cannot be calculated: dimension error!')

    def get_point_pairs(self, indices):
        """
        This function returns the point pair values for given indices.
        :param indices: indices of pairs (tuple)
        :return: point pairs (list)
        """
        p1 = self.points[indices[0] * self.dimension:indices[0] * self.dimension + self.dimension]
        p2 = self.points[indices[1] * self.dimension:indices[1] * self.dimension + self.dimension]

        return p1, p2
