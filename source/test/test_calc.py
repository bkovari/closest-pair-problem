import unittest
from source.solution.point import Point
from source.solution.io_manager import IOManager
from source.solution.simple_calc import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):
    """
    Class is responsible for testing brute force calculation.
    """

    def setUp(self):
        self.calculator = SimpleCalculator()

    def tearDown(self):
        pass

    def test_result_from_sample(self):
        # {0}: 1,1,1 | {1}: 5,5,5 | {2}: 2,2,2
        # closest pair position (dim=3) : (0,2)
        self.test_points = [1, 1, 1, 5, 5, 5, 2, 2, 2]
        self.dimension = 3
        self.result = (0, 2)

        n_dim_points = Point(self.test_points)
        n_dim_points.dimension = self.dimension

        min_dist_pairs = self.calculator.get_minimum_distance_pair(n_dim_points.points,
                                                                   n_dim_points.dimension)

        self.assertEqual(self.result, min_dist_pairs)
        # try different point set and dimension
        # {0}:0,0 | {1}:6,3 | {2}:4,5 | {3}:2,2
        self.test_points = [0, 0, 6, 3, 4, 5, 2, 2]
        self.dimension = 2
        self.result = (0, 3)

        n_dim_points = Point(self.test_points)
        n_dim_points.dimension = self.dimension
        min_dist_pairs = self.calculator.get_minimum_distance_pair(n_dim_points.points,
                                                                   n_dim_points.dimension)

        self.assertEqual(self.result, min_dist_pairs)

    def test_result_from_file(self):
        point_file_manager = IOManager('../../venv/resources/sample_input_2_8.tsv')

        self.test_points = point_file_manager.read_points_from_file()
        self.dimension = point_file_manager.get_element_per_line()

        with open('../../venv/resources/sample_output_2_8.txt', 'r') as output_textfile:
            txt = list(output_textfile.readlines())

        p1_fileline = int(txt[0][txt[0].find(":") - 1])
        p2_fileline = int(txt[1][txt[1].find(":") - 1])

        n_dim_points = Point(self.test_points)
        n_dim_points.dimension = self.dimension
        min_dist_pairs = self.calculator.get_minimum_distance_pair(n_dim_points.points,
                                                                   n_dim_points.dimension)

        self.result = (min_dist_pairs[0],min_dist_pairs[1])

        # map file line to list position
        self.assertTupleEqual((p1_fileline - 1, p2_fileline - 1), self.result)

    def test_dimension_check(self):
        self.test_points = [1, 1, 1, 5, 5, 5, 2, 2]
        self.dimension = 3

        n_dim_points = Point(self.test_points)
        n_dim_points.dimension = self.dimension

        with self.assertRaises(Exception):
            self.calculator.get_minimum_distance_pair(n_dim_points.points,
                                                      n_dim_points.dimension)


if __name__ == '__main__':
    unittest.main()
