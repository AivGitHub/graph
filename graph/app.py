import argparse
from .graph import Graph
from .graph import GraphException

def run():
    parser = argparse.ArgumentParser(description='Process Graph.')
    parser.add_argument('-p', '--path', required=True, nargs=1, help='Path to adjacency matrix')
    args = parser.parse_args()

    graph = Graph(path_matrix=args.path[0])


if __name__ == '__main__':
    run()
