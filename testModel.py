from model.model import Model
from UI.controller import Controller

myModel = Model()
# print(myModel.fillDD())
a = myModel.fillDD()
for b in a:
    print(b)
myModel.get_all_nodes(3)

idMap = myModel._idMap
myModel.buildGraph(3,5)
n, e = myModel.get_info()
print(n, e)