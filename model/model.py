import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._nodes = []
        self._edges = []
        self._graph = nx.Graph()
        self._idMap = {}


    def fillDD(self):
        return DAO.fillDD()

    def get_all_nodes(self, store):
        self._nodes = DAO.get_all_nodes(store)
        for node in self._nodes:
            self._idMap[node.order_id] = node
        return self._nodes


    def buildGraph(self, store, interval):
        self._graph.clear()
        self.get_all_nodes(store)
        self._graph.add_nodes_from(self._nodes)
        self._edges = DAO.get_all_edges(store, interval, self._idMap)
        for a in self._edges:
          arco = [(a.Ordine1, a.Ordine2, a.weight)]
          self._graph.add_weighted_edges_from(arco)



    def get_info(self):
        return self._graph.number_of_nodes(), self._graph.number_of_edges()





