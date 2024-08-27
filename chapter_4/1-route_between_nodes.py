# Problem Description
# Given a directed graph, design an algorithm to find out whether there is a route between two nodes.

from collections import deque
from testing_functions import testFunction

def routeExistsBFS(graph, nodeA, nodeB):
  queue = deque([])
  queue.append(nodeA)
  visitedSet = set()
  while len(queue) > 0:
    node = queue.popleft()
    if node == nodeB:
      return True
    if not node in visitedSet:
      if node in graph:
        queue.extend(graph[node])
    visitedSet.add(node)
  return False

def routeExistsDFS(graph, nodeA, nodeB, visitedSet = set()):
  if nodeA == nodeB:
    return True
  if not nodeA in visitedSet:
    visitedSet.add(nodeA)
    if nodeA in graph:
      neighbours = graph[nodeA]
      for neighbour in neighbours:
        routeExists = routeExistsDFS(graph, neighbour, nodeB, visitedSet)
        if routeExists:
          return True
  return False

def testRouteExistsBFS(args):
  graph = args[0]
  nodeA = args[1]
  nodeB = args[2]
  route1Exists = routeExistsBFS(graph, nodeA, nodeB)
  return True if route1Exists else routeExistsBFS(graph, nodeB, nodeA)

def testRouteExistsDFS(args):
  graph = args[0]
  nodeA = args[1]
  nodeB = args[2]
  route1Exists = routeExistsDFS(graph, nodeA, nodeB, set())
  return True if route1Exists else routeExistsDFS(graph, nodeB, nodeA, set())

# Build Graph
graph = {}
graph[1] = [8]
graph[2] = [5]
graph[3] = [7,1]
graph[4] = [2,6]
graph[5] = [3,4]
graph[6] = [3]
testCases = [[graph, 1, 2], [graph, 6, 8], [graph, 7, 8], [graph, 1, 7], [graph, 2, 7]]
expectedResults = [True, True, False, False, True]
testFunction(testCases, expectedResults, testRouteExistsBFS)
testFunction(testCases, expectedResults, testRouteExistsDFS)
