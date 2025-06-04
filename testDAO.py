from database.DAO import DAO

myDAO = DAO()
stores = myDAO.fillDD()

# for store in stores:
#     print(store)

nodi = myDAO.get_all_nodes(1)
for node in nodi:
    print(node)