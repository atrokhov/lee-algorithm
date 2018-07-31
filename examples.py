from bfs_algo import *

graph = {
         'A': set(['B', 'C']),
         'B': set(['A', 'C', 'D']),
         'C': set(['A', 'B']), 
         'D': set(['B'])
         }

graph2= {
         'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'E']), 
         'D': set(['B']), 
         'E': set(['B', 'C', 'F']), 
         'F': set(['E'])
         }

graph3 = {
         'A': set(['B', 'C', 'D']),
         'B': set(['A', 'C', 'E', 'F']),
         'C': set(['A', 'B', 'D', 'F']), 
         'D': set(['A', 'C', 'G']), 
         'E': set(['B', 'F', 'K']), 
         'F': set(['B', 'C', 'E', 'G', 'K']),
         'G': set(['D', 'F', 'K']),
         'K': set(['E', 'F', 'G'])
         }

graph4 = {
         'A': set(['B', 'C', 'D']),
         'B': set(['A', 'D']),
         'C': set(['A', 'F']), 
         'D': set(['A', 'B', 'E']), 
         'E': set(['D', 'K']), 
         'F': set(['C']),
         'K': set(['E'])
         }

graph5 = {
         'A': set(['B']),
         'B': set(['A', 'C']),
         'C': set(['B']), 
         'D': set(['E']), 
         'E': set(['D', 'F']), 
         'F': set(['E'])
         }


print bfs(graph3, 'A')
print [ '->'.join(str) for str in list(bfs_paths(graph3, 'A', 'K')) ]
print '->'.join(shortest_path(graph3, 'A', 'K'))