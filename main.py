from treeNode import TreeNode
from fifo import FIFOQueue
from lifo import LIFOQueue
from priorityQueue import PriorityQueue
from datos import cargar_datos

# Ahora ya puedes inicializar todo
grafo, heuristica = cargar_datos()
frontera = PriorityQueue(use_heuristic=True) # Para A*