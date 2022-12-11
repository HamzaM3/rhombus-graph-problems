from RhombParityProblem import RhombParityProblemNaive
from copy import deepcopy

def fuseLists(l1, l2):
  res = set(l1)
  for x in l2:
    res.add(x)
  return list(res)

def groupList(l, gr):
  v = False
  res = []

  for x in l:
    if x in gr:
      v = True
    else:
      res.append(x)

  if v:
    res.append(gr[0])

  return res

def uniqueConcat(lists):
  res = []
  for l in lists:
    res += l
  return list(set(res))

def groupNodes(g, grps):
  for gr in grps:
    g[gr[0]] = uniqueConcat([g[k] for k in gr])
    for k in gr[1:]:
      del g[k]

    for k, l in g.items():
      g[k] = groupList(l, gr)
  
  return g

def getParity(p, gr):
  res = 'all'
  for x in gr:
    if res == 'all':
      res = p[x]
    elif (p[x] != 'all' and res != p[x]):
      raise Exception('Grouping is both even and odd')
  return res

def groupParity(p, grps):
  for gr in grps:
    p[gr[0]] = getParity(p, gr)
    for k in gr[1:]:
      del p[k]
  return p

def fuseGraph(o1, o2):
  res = dict()
  for x, n1 in o1.items():
    n2 = o2[x]
    n = fuseLists(n1, n2)
    res[x] = n
  return res

def decycle(g):
  for x in g:
    g[x] = [n for n in g[x] if n != x]
  return g

def fuseGroupGraph(o1, o2, gr, p):
  o1 = groupNodes(o1, gr)
  o2 = groupNodes(o2, gr)
  p = groupParity(p, gr)
  g = fuseGraph(o1, o2)
  g = decycle(g)
  return [g, p]

class RhombWifiProblem(RhombParityProblemNaive):
  def __init__(self, obstructedBy, potentiallyObstructing, parity, groupings):
    self.o1 = deepcopy(obstructedBy)
    self.o2 = deepcopy(potentiallyObstructing)
    self.parity = parity
    self.groupings = groupings
    self.sol = None
    self.sol = self.solution()

  def solution(self):
    if self.sol is not None:
      return self.sol

    [g, p] = fuseGroupGraph(self.o1, self.o2, self.groupings, self.parity)

    n = len(g.keys())

    return self.solutionRec([], g, p, 0, n)

####-----------------------------------####

if __name__ == '__main__':
  g1 = {
    1: [],
    2: [1],
    3: [2, 7],
    4: [5],
    5: [],
    6: [],
    7: [4, 8],
    8: []
  }

  g2 = {
    1: [],
    2: [],
    3: [],
    4: [],
    5: [8],
    6: [3],
    7: [5],
    8: []
  }

  even = 'even'
  odd = 'odd'
  none = 'all'

  p = {
    1: odd,
    2: none,
    3: none,
    4: none,
    5: none,
    6: none,
    7: none,
    8: none
  }

  gr = [
    [2,5],
  ]

  r = RhombWifiProblem(g1, g2, p, gr)
  print(r.sol)
