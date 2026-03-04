class FIFOQueue:
   """Cola para Breadth-First Search (BFS) - Primero en entrar, primero en salir"""
   def __init__(self):
      self.items = []

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
      return self.items