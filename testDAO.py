from database.DAO import DAO
from model.model import Model
myDAO = DAO()
stores = myDAO.fillDD()
myModel = Model()
for store in stores:
    print(store.store_id)

nodi = myDAO.get_all_nodes(1)
# for node in nodi:
#     print(node)
# myModel.buildGraph(3,5)
# edges = myDAO.get_all_edges(3, 5, myModel._idMap)

# print(edges)