from simple_calc import SimpleCalculator
from io_manager import IOManager
from point import Point


def main():
    point_file_manager = IOManager('sample_input_4_4.tsv')

    points = point_file_manager.read_points_from_file()
    dimension = point_file_manager.get_element_per_line()

    n_dim_points = Point(points)
    n_dim_points.dimension = dimension

    calculator = SimpleCalculator()
    min_dist_pairs = calculator.get_minimum_distance_pair(n_dim_points.points,
                                                          n_dim_points.dimension)

    pair_values = n_dim_points.get_point_pairs(min_dist_pairs)

    result = point_file_manager.get_formatted_result(min_dist_pairs, pair_values)
    point_file_manager.write_result_to_file(result)
    print result


main()
