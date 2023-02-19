from sys import maxsize
from itertools import permutations
V = 4
# implementation of traveling Salesman Problem
def travellingSalesmanProblem(graph, s):
 # store all vertex apart from source vertex
 vertex = []
 for i in range(V):
 if i != s:
 vertex.append(i)
 # store minimum weight
 min_path = maxsize
 next_permutation=permutations(vertex)
 for i in next_permutation:
 # store current Path weight(cost)
 current_pathweight = 0
 # compute current path weight
 k = s
 for j in i:
 current_pathweight += graph[k][j]
 k = j
 current_pathweight += graph[k][s]
 # update minimum
 min_path = min(min_path, current_pathweight)

 return min_path
# Driver Code
if __name__ == "__main__":
 # matrix representation of graph
 graph = [[0, 10, 15, 20], [10, 0, 35, 25],
 [15, 35, 0, 30], [20, 25, 30, 0]]
 s = 0
 print(travellingSalesmanProblem(graph, s))
Output
80
7. Write a Program to Implement Tower of Hanoi using Python.
# Recursive Python function to solve tower of hanoi
def TowerOfHanoi(n , from_rod, to_rod, aux_rod):
 if n == 1:
 print("Move disk 1 from rod",from_rod,"to rod",to_rod)
 return
 TowerOfHanoi(n-1, from_rod, aux_rod, to_rod)
 print("Move disk",n,"from rod",from_rod,"to rod",to_rod)
 TowerOfHanoi(n-1, aux_rod, to_rod, from_rod)

# Driver code
n = 4
TowerOfHanoi(n, 'A', 'C', 'B')
# A, C, B are the name of rods
