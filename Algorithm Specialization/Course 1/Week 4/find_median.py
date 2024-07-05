import random
from collections import namedtuple

Edge = namedtuple('Edge', ['src', 'dest'])  # Simplified Edge structure

class Graph:
    def __init__(self, V, E):
        self.V = V
        self.E = E
        self.edge = [Edge(-1, -1)] * E  # Initialize edges with placeholders

class Subset:
    def __init__(self, parent=None, rank=0):
        self.parent = parent if parent is not None else self
        self.rank = rank

def find(subsets, i):
    if subsets[i].parent != i:
        subsets[i].parent = find(subsets, subsets[i].parent)
    return subsets[i].parent

def union(subsets, x, y):
    xroot = find(subsets, x)
    yroot = find(subsets, y)

    if subsets[xroot].rank < subsets[yroot].rank:
        subsets[xroot].parent = yroot
    elif subsets[xroot].rank > subsets[yroot].rank:
        subsets[yroot].parent = xroot
    else:
        subsets[yroot].parent = xroot
        subsets[xroot].rank += 1

def random_contraction(graph):
    V, E, edge = graph.V, graph.E, graph.edge
    subsets = [Subset(i) for i in range(V)]  # Initialize subsets

    vertices = V
    while vertices > 2:
        i = random.randrange(E)
        subset1 = find(subsets, edge[i].src)
        subset2 = find(subsets, edge[i].dest)
        if subset1 != subset2:
            union(subsets, subset1, subset2)
            vertices -= 1

    cut_edges = 0
    for i in range(E):
        subset1 = find(subsets, edge[i].src)
        subset2 = find(subsets, edge[i].dest)
        if subset1 != subset2:
            cut_edges += 1
    return cut_edges


V = 200
E = 0  # Initialize edge count

graph = Graph(V, 0)  # Start with empty edge list

with open("kargerMinCut.txt", "r") as file:
    for line in file:
        vertices = [int(x) - 1 for x in line.strip().split()] 
        for i in range(1, len(vertices)): 
            if vertices[i] > vertices[0]: 
                graph.edge.append(Edge(vertices[0], vertices[i]))  # Use append to add edges dynamically
                E += 1

graph.E = E  # Update the actual edge count

# Main execution
random.seed()  # Seed the random number generator (optional)

# Count edges from "kargerMinCut.txt" 


min_contractions = float('inf')
for i in range(200):
    calculated = random_contraction(graph)
    if calculated < min_contractions:
        min_contractions = calculated
print(min_contractions)
