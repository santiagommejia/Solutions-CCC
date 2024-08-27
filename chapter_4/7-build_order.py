# Problem Description
# You are given a list of projects and a list of dependencies (which is a list of pairs of projects, where the second project is dependent on the first project). All of a project's dependencies must be built before the project is. Find a build order that will allow the projects to be built. If there is no valid build order, return an error.

# EXAMPLE
# Input:
#   projects: a, b, c, d, e, f
#   dependencies: (a, d), (f, b), (b, d), (f, a), (d, c)
# Output: f, e, a, b, d, c

from collections import deque

def buildGraph(projects, dependencies):
  graph = { project: [] for project in projects }
  for dependency in dependencies:
    graph[dependency[0]].append(dependency[1])
  return graph 

def getBuildOrder(graph):
  inDegree = { u: 0 for u in graph }  
  for u in graph:
    for v in graph[u]:
      inDegree[v] += 1
  queue = deque([u for u in graph if inDegree[u] == 0])
  topologicalOrder = []
  while queue:
    u = queue.popleft()
    topologicalOrder.append(u)
    for v in graph[u]:
      inDegree[v] -= 1
      if inDegree[v] == 0:
        queue.append(v)
  if len(topologicalOrder) == len(graph):
    return topologicalOrder
  else:
    raise ValueError('cycle detected')

projects = ['a','b','c','d','e','f']
dependencies = [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c')]
dependencies2 = [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c'), ('f','c')]
cyclicDependencies = [('a', 'd'), ('f', 'b'), ('b', 'd'), ('f', 'a'), ('d', 'c'), ('c', 'd')]
cases = [dependencies, dependencies2, cyclicDependencies]
for i in range(len(cases)):
  case = cases[i]
  try:
    graph = buildGraph(projects, case)
    order = getBuildOrder(graph)
    print(f'Case {i}:', order)
  except Exception as e:
    print(f'Case {i}:', e)