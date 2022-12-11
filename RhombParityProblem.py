from copy import deepcopy

def reverseGraph(g):
  res = dict()
  for node in g:
    res[node] = []
  for node, neigh in g.items():
    for n in neigh:
      res[n].append(node)
  
  return res

def test_parity(p, t):
  if t % 2 == 0:
    return p == 'even' or p == 'all'
  else:
    return p == 'odd' or p == 'all'

def getValidSinks(g, parity, t):
  res = []
  p = lambda n: test_parity(parity[n], t)

  for n in g:
    if len(g[n]) == 0 and p(n):
      res.append(n)
  return res

def remove(val, g): 
  g = deepcopy(g)
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

class RhombParityProblemNaive:
  def __init__(self, obstructedBy, potentiallyObstructing, parity):
    self.o1 = deepcopy(obstructedBy)
    self.o2 = deepcopy(potentiallyObstructing)
    self.parity = parity
    self.nodes = self.o1.keys()
    self.sol = None
    self.sol = self.solution()

  def solution(self, t=0):
    if self.sol is not None:
      return self.sol

    g = fuseGraphs(self.o1, self.o2)
    parity = self.parity
    n = len(self.nodes)

    return self.solutionRec([], g, parity, 0, n)

  def solutionRec(self, sol, g, parity, t, n):
    if (len(sol) == n):
      return sol
    p = getValidSinks(g, parity, t)

    for x in p:
      sol_t = sol + [x]
      g_t = remove(x, g)

      sol_t = self.solutionRec(sol_t, g_t, parity, t+1, n)
      if sol_t != 'no solution':
        return sol_t

    return 'no solution'

# g1 = {
#   1: [2, 5],
#   2: [],
#   3: [4],
#   4: [7],
#   5: [6],
#   6: [],
#   7: []
# }

# g2 = {
#   1: [2],
#   2: [3],
#   3: [],
#   4: [],
#   5: [6],
#   6: [4],
#   7: []
# }

# even = 'even'
# odd = 'odd'
# none = 'all'
# p = {
#   1: even,
#   2: even,
#   3: odd,
#   4: none,
#   5: none,
#   6: none,
#   7: none,
# }

if __name__ == '__main__':
  g1 = {
    1: [],
    2: [],
    3: [1],
    4: [8],
    5: [8],
    6: [],
    7: [6,5,4,3],
    8: []
  }

  g2 = {
    1: [2],
    2: [],
    3: [],
    4: [],
    5: [],
    6: [3],
    7: [2],
    8: [2]
  }

  even = 'even'
  odd = 'odd'
  none = 'all'

  parity = {
    1: even,
    2: none,
    3: even,
    4: none,
    5: none,
    6: odd,
    7: none,
    8: odd
  }

  r = RhombParityProblemNaive(g1, g2, parity)
  print(r.sol)
