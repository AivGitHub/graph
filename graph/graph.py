import os


class GraphException(Exception):
    pass


class Graph(object):
    """ Main graph object

    """
    def __init__(self, path_matrix=None):
        self.matrix = path_matrix

    @property
    def matrix(self):
        return self._matrix

    @matrix.setter
    def matrix(self, path_matrix):
        if path_matrix and os.path.exists(path_matrix):
            with open(path_matrix) as file_matrix:
                self._matrix = [list(map(int, row.split())) for row in file_matrix.readlines()]
        else:
            raise GraphException('File \'%s\' not found' % path_matrix)

    def depth_first_search(self, start_vertex):
        """ We should forget about recursive functions.

        :param start_vertex: Start vertex
        :return: Return depth first search path
        """
        if not start_vertex:
            raise GraphException('Start vertex must be vertex number')

        path = []

        stack = [start_vertex]

        while len(stack):
            s = stack.pop()

            if s not in path:
                path.append(s)
