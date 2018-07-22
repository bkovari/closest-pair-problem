import unittest
from source.solution.io_manager import IOManager


class TestIOManager(unittest.TestCase):

    def setUp(self):
        self.point_file_manager = IOManager('mysample_input_3_3.tsv', 'mysample_output_3_3.txt')

    def test_get_element_per_line(self):
        # Element per line = dimension
        # test with basic setup: expected 3 element
        element_per_line = self.point_file_manager.get_element_per_line()
        self.assertEqual(element_per_line, 3)

        # test output file is correct as well
        self.point_file_manager.input_file = 'mysample_output_3_3.txt'
        element_per_line = self.point_file_manager.get_element_per_line()
        self.assertEqual(element_per_line, 3)

        # try another file: expected 100 element
        self.point_file_manager.input_file = 'sample_input_100_100.tsv'
        element_per_line = self.point_file_manager.get_element_per_line()
        self.assertEqual(element_per_line, 100)

    def test_read_points_from_file(self):
        self.point_file_manager.input_file = "sample_input_100_100.tsv"
        points = self.point_file_manager.read_points_from_file()
        self.assertEqual(len(points), 100 * 100)

    def test_get_formatted_result(self):
        pairs = [[1.4123456789111111, 1.5, 1.0], [2.0, 3.99, 5.0]]
        line_nums = (1, 5)
        self.result = "2:1.4\t2\t1\n6:2\t4\t5"  # line nums incremented

        formatted_res = self.point_file_manager.get_formatted_result(line_nums, pairs)
        self.assertEqual(self.result, formatted_res)


if __name__ == '__main__':
    unittest.main()
