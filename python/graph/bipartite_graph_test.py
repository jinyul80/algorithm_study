import unittest

from bipartite_graph import BipartiteGraph


class GraphTestCase(unittest.TestCase):
    def test_graph1(self):
        V = 3
        E = 2
        edge_list = [[1, 2], [2, 3]]

        graph = BipartiteGraph()
        result = graph.is_bipartite(V, E, edge_list)

        self.assertEqual(result, True)

    def test_graph2(self):
        V = 4
        E = 4
        edge_list = [[1, 2], [2, 3], [3, 4], [4, 2]]

        graph = BipartiteGraph()
        result = graph.is_bipartite(V, E, edge_list)
        self.assertEqual(result, False)
