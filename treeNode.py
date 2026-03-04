class TreeNode:
   def __init__(self, state, path_cost=0, heuristic=0):
      self.state = state          # Nombre del ejercicio (ej. "Warm-up activities")
      self.path_cost = path_cost  # Costo g(n): Tiempo real acumulado
      self.heuristic = heuristic  # Costo h(n): Heurística hacia la meta
      
      # Punteros para formar la estructura de árbol
      self.parent = None          # Nodo padre del que venimos
      self.children = []          # Nodos hijos descubiertos
      
   def add_child(self, child_node):
      """Método para agregar un hijo y conectar el árbol"""
      child_node.parent = self
      self.children.append(child_node)
      
   def f(self):
      """Calcula f(n) = g(n) + h(n) para el algoritmo A*"""
      return self.path_cost + self.heuristic

   def __repr__(self):
      # Representación en texto para poder imprimirlo en consola
      return f"[{self.state} (g={self.path_cost}, h={self.heuristic}, f={self.f()})]"