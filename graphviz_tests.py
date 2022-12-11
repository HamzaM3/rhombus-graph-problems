import graphviz

def getGraph(size, adj):
  graph = graphviz.Digraph()
  for node, edges in adj.items():
    graph.node(str(node))
    [graph.edge(str(n), str(node)) for n in edges]
  return graph

def getNextGraph(size, adj):
  graph = graphviz.Digraph()

  with graph.subgraph(name='r1') as c:
    for node in adj:
      c.node(str(node)+'1', label=str(node), shape='box')

  with graph.subgraph(name='r2') as c:
    for node in adj:
      c.node(str(node)+'2', label=str(node), shape='circle')

  for node, edges in adj.items():
    [graph.edge( str(node)+'1',str(n)+'2') for n in edges]
  return graph



size = 8

activated = []



# potentially obstructing these
t = {
  1: [5], 
  2: [3], 
  3: [], 
  4: [5], 
  5: [], 
  6: [5], 
  7: [], 
  8: []
}

# fuse g1 and g2

g2 = reverseGraph(g2)
print(g2)

graph = getGraph(size, g1)
graph.format = 'png'
graph.render('res')

graph = getNextGraph(size, g2)
graph.format = 'png'
graph.render('res2')


p1 = unobstructed(g1)
p2 = nonObstructor(g2)

print(p1, p2)
print(intersection(p1,p2))