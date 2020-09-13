from graphviz import Digraph
import csv

parents = []
children = []
data = []
with open("sampleData.csv") as file:
    reader = csv.reader(file)  # change contents to floats
    next(reader)
    for row in reader:  # each row is a list
        data.append(row)
        parents.append(row[0])
        children.append(row[1])

data = list(filter(None, data))

nodes = parents + children
nodes = list(dict.fromkeys(nodes))
nodes = sorted(nodes)

dot = Digraph(comment='Hierarchy Diagram', engine='dot')

for node in nodes:
    dot.node(node)

for x in data:
    dot.edge(x[0], x[1], constraint='true')

dot.render('test-output/sampleDiagram', view=True)