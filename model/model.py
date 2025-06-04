import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._nodes = []
        self._edges = []
        self._graph = nx.Graph()


    def fillDD(self):
        return DAO.fillDD()

    def get_all_nodes(self, store):
        self._nodes = DAO.get_all_nodes(store)



    def buildGraph(self, store):
        self._graph.clear()
        self.get_all_nodes(store)
        self._graph.add_nodes_from(self._nodes)


    def get_info(self):
        return self._graph.number_of_nodes(), self._graph.number_of_edges()





