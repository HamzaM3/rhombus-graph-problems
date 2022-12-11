from copy import deepcopy

def reverseGraph(g):
  res = dict()
  for node in g:
    res[node] = []
  for node, neigh in g.items():
    for n in neigh:
      res[n].append(node)
  
  return res

def getSinks(g1):
  res = []
  for n in g1:
    if len(g1[n]) == 0:
      res.append(n)
  return res

def remove(val, g):
  del g[val]
  for x in g:
    g[x] = [n for n in g[x] if n != val]
  return g

def fuseLists(l1, l2):
  res = set(l1)
  for x in l2:
    res.add(x)
  return list(res)

def fuseGraphs(g1, g2):
  res = dict()
  for x, n1 in g1.items():
    n2 = g2[x]
    n = fuseLists(n1, n2)
    res[x] = n
  return res

class RhombProblem:
  def __init__(self, obstructedBy, potentiallyObstructedBy):
    self.o1 = deepcopy(obstructedBy)
    self.o2 = deepcopy(reverseGraph(potentiallyObstructedBy))
    self.sol = None
    self.sol = self.solution()

  def solution(self):
    if self.sol is not None:
      return self.sol

    g = fuseGraphs(self.o1, self.o2)

    n = len(g.keys())
    sol = []

    while len(sol) < n:
      p = getSinks(g)

      print(sol, p)
      if (len(p) == 0):
        self.sol = 'no solution'
        return 'no solution'

      sol = sol + p
      for s in p:
        g = remove(s, g)

    self.sol = sol
    return sol

# node -> obstructor
g1 = {
  1: [2,3,7,8],
  2: [],
  3: [4],
  4: [],
  5: [],
  6: [],
  7: [6],
  8: [6],
}

# node -> potential obstructor
g2 = {
  1: [],
  2: [],
  3: [2],
  4: [],
  5: [1,4,6],
  6: [],
  7: [],
  8: [],
}

r = RhombProblem(g1, g2)
print(r.sol)
