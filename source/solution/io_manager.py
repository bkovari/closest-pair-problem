import csv


class IOManager:
    """
    Class is responsible for I/O operations for tsv files including n dimensional points.
    """

    def __init__(self, input_file, output_file="../../venv/resources/calculation_output.txt"):
        self.input_file = input_file
        self.output_file = output_file

    def read_points_from_file(self):
        """
        This function reads n dimension points from input file and writes to list.
        :return: points (list)
        """

        points = []
        with open('../../venv/resources/' + self.input_file) as tsvfile:
            rows = csv.reader(tsvfile, delimiter="\t")
            for cols in rows:
                for i in range(len(cols)):
                    points.append(float(cols[i]))
        return points

    def get_element_per_line(self):
        """
        This function returns the tab separated element count per line from the input file.
        :return: element count (int)
        """
        with open('../../venv/resources/' + self.input_file) as tsvfile:
            # number of elements = found tabulators + 1
            count = list(tsvfile.readline()).count('\t') + 1
        return count

    def write_result_to_file(self, result):
        """
        This function writes formatted result to output file.
        :param result: formatted (string)
        :return: -
        """

        with open('../../venv/resources/' + self.output_file, "w") as tsvfile:
            tsvfile.write(result)

    @staticmethod
    def get_formatted_result(line_number, pairs):
        """
        This function returns the desired representation of pont pair result.
        :param line_number: position of point pairs (tuple)
        :param pairs: pairs (list)
        :return: formatted result (string)
        """

        # round floating point numbers to 1 digit when necessary
        # then recheck fractional part..
        for p in range(0, 2):
            for n in range(0, len(pairs[0])):
                if len(str(abs(pairs[p][n] - abs(int(pairs[p][n]))))) >= 14:
                    pairs[p][n] = round(pairs[p][n], 1)
                    if pairs[p][n] - int(pairs[p][n]) == 0:
                        pairs[p][n] = int(pairs[p][n])
                else:
                    pairs[p][n] = int(round(pairs[p][n]))

        # +1 is necessary: file line numbering starts from 1
        return ("{}:{}\n{}:{}".format(line_number[0] + 1,
                                      '\t'.join(str(p) for p in pairs[0]),
                                      line_number[1] + 1,
                                      '\t'.join(str(q) for q in pairs[1])))
