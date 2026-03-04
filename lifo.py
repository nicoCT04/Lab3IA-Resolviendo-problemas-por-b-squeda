class LIFOQueue:
   """Pila para Depth-First Search (DFS) - Último en entrar, primero en salir"""
   def __init__(self):
      self.items = []

   def EMPTY(self):
      return len(self.items) == 0

   def TOP(self):
      if not self.EMPTY():
         return self.items[-1] # Retorna el último elemento agregado
      return None

   def POP(self):
      if not self.EMPTY():
         return self.items.pop() # Saca el último elemento
      return None

   def ADD(self, item):
      self.items.append(item)
      return self.items