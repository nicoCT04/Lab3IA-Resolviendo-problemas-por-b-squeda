class PriorityQueue:
   """Cola de Prioridad para UCS y A* - Ordena automáticamente por costo"""
   def __init__(self, use_heuristic=False):
      self.items = []
      # True = A* (Ordena por f = g + h) | False = UCS (Ordena por g)
      self.use_heuristic = use_heuristic 

   def EMPTY(self):
      return len(self.items) == 0

   def TOP(self):
      if not self.EMPTY():
         return self.items[0]
      return None

   def POP(self):
      if not self.EMPTY():
         return self.items.pop(0)
      return None

   def ADD(self, item):
      self.items.append(item)
      
      # Mágia de la prioridad: Se reordena cada vez que agregas un nodo
      if self.use_heuristic:
         self.items.sort(key=lambda node: node.f())
      else:
         self.items.sort(key=lambda node: node.path_cost)
         
      return self.items