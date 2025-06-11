import copy

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


    # def getCammino(self, nodoP):
    #     nodosorgente = self._idMap[int(nodoP)]
    #     listaNodiPercorso = []
    #
    #     # for nodosorgente in self._graph.nodes:
    #     tree = nx.dfs_tree(self._graph, nodosorgente)
    #     nodi = list(tree.nodes())
    #
    #     for node in nodi:
    #         cammino = [node]
    #         #cammino è un array che contiene inizialmente il nodo sorgente,
    #         #all'array si aggiungono man mano i nodi dell'albero tramite la funzione nx.predecessor
    #
    #         while cammino[0] != nodosorgente:
    #         #nodo iniziale != dal nodo sorgente
    #             pred = nx.predecessor(tree, nodosorgente, cammino[0])
    #             cammino.insert(0, pred[0])
    #         if len(cammino) > len(listaNodiPercorso):
    #             listaNodiPercorso = copy.deepcopy(cammino)
    #
    #     return listaNodiPercorso

    def getCammino(self, nodoP):
        #uso la _idMap per trovare il mio oggetto nodo (ordine)
        nodosorgente = self._idMap[int(nodoP)]

        # Prima BFS per trovare il nodo più lontano
        distances = nx.single_source_shortest_path_length(self._graph, nodosorgente)
        farthest_node = max(distances, key=distances.get)

        # Poi ricostruisci il cammino più lungo (diametro locale)
        longestpath = nx.shortest_path(self._graph, source=nodosorgente, target=farthest_node)
        #(si, usa nx.shortest_path per il longest, kinda gay but ok)
        return longestpath



