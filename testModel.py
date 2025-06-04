from model.model import Model

myModel = Model()
myModel.buildGraph(1)
n, e = myModel.get_info()
print(n)