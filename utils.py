import numpy as np
import random
import networkx as nx
import matplotlib.pyplot as plt
import tabulate
from collections import deque


def breadth_first_search(graph, i_vert_initial, i_vert_last):
    queue = deque([i_vert_initial])
    level = {i_vert_initial: 0}
    parent = {i_vert_initial: None}
    i = 1
    while queue:
        v = queue.popleft()
        for n in graph[v]:
            if n not in level:
                queue.append(n)
                level[n] = i
                parent[n] = v
            if v == i_vert_last:
                break
            i += 1
    path = backtrace(parent, i_vert_initial, i_vert_last)
    print('The path between %i and %i - %s' % (i_vert_initial, i_vert_last, path))


# Breadth-first search
def backtrace(parent, start, end):
    path = [end]
    while path[0] != start:
        path.append(parent[path[-1]])
        path.reverse()
    return path[:path.index(end) + 1]


def connect_component(graph, n):
    # List of unvisited nodes
    visited = [False] * n
    num_components = 0
    for v in range(n):
        # If after one step of dfs we have unvisited nodes, we increase num_components by 1.
        # Else we visited all nodes and number of the connected components of the graph equals 1
        if not visited[v]:
            depth_first_search(visited, graph, v)
            num_components += 1
    print('Number of the connected components of the graph - %i' % num_components)


# Depth-first search
def depth_first_search(visited, graph, node):
    visited[node] = True
    for w in graph[node]:
        if not visited[w]:
            depth_first_search(visited, graph, w)
