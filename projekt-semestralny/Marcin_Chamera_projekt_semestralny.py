'''
Projekt semestralny Python
Algorytm binarnego drzewa poszukiwań ze wskaźnikiem do rodzica.
Autor: Marcin Chamera
'''

class Node:
  '''Klasa reprezentująca węzeł drzewa.'''

  def __init__(self, data=None, left=None, right=None, parent=None):
    self.data = data
    self.right = None
    self.left = None
    self.parent = None

  def __str__(self):
    return str(self.data)

class BinarySearchTree:
  '''Klasa reprezentująca binarne drzewo poszukiwań.'''

  def __init__(self):
    self.root = None

  def minimum(self, x):
    '''Zwraca węzeł o najmniejszej wartości 'data' w drzewie o korzeniu x.'''
    while x.left != None:
      x = x.left
    return x

  def insert(self, node):
    '''Wstawia węzeł 'node' do drzewa w odpowiednie miejsce.'''
    y = None
    temp = self.root
    while temp != None:
      y = temp
      if node.data < temp.data:
        temp = temp.left
      else:
        temp = temp.right

    node.parent = y

    if y == None:
      self.root = node
    elif node.data < y.data:
      y.left = node
    else:
      y.right = node

  def count(self, node):
    '''Zwraca liczbę węzłów w drzewie.'''
    if not node:
      return 0
    return 1 + self.count(node.left) + self.count(node.right)

  def search(self, node, data):   
    '''Szuka w drzewie węzeł o podanej wartości 'data'.'''
    if node.data == data:
      return node
    if data < node.data:
      if node.left:
        return self.search(node.left, data)
    else:
      if node.right:
        return self.search(node.right, data)
    return None

  def transplant(self, u, v):
    '''Przekleja poddrzewo zakorzenie w węźle v w miejsce poddrzewa
    zakorzenionego w węźle u.'''
    if u.parent == None:
      self.root = v
    elif u == u.parent.left:
      u.parent.left = v
    else:
      u.parent.right = v

    if v != None:
      v.parent = u.parent

  def remove(self, data):
    '''Usuwa z drzewa węzeł o podanej wartości 'data'.'''
    z = self.search(self.root, data)
    if z is None:
      raise Exception('W tym drzewie nie ma wezla o takiej wartosci.')
    if z.left == None:
      self.transplant(z, z.right)

    elif z.right == None:
      self.transplant(z, z.left)

    else:
      y = self.minimum(z.right) 
      if y.parent != z:
        self.transplant(y, y.right)
        y.right = z.right
        y.right.parent = y

      self.transplant(z, y)
      y.left = z.left
      y.left.parent = y
    return z

  def inorder(self, node):
    '''Przechodzi przez drzewo w kolejności poprzecznej (in-order)
    i wyświetla wartość, i rodzica każdego z odwiedzonych węzłów.'''
    if node:
        self.inorder(node.left)
        print('Wezel:', node.data, ', Rodzic:',
            node.parent.data if node.parent is not None else 'None')
        self.inorder(node.right)

if __name__ == '__main__':
  t = BinarySearchTree()

  a = Node(10)
  b = Node(20)
  c = Node(30)
  d = Node(100)
  e = Node(90)
  f = Node(40)
  g = Node(50)
  h = Node(60)
  i = Node(70)
  j = Node(80)
  k = Node(150)
  l = Node(110)
  m = Node(120)

  nodes = [a, b, c, d, e, f, g, h, i, j, k, l, m]

  for node in nodes:
    t.insert(node)

  print('Po dodaniu wezlow:')
  t.inorder(t.root)

  print('Usunieto wezel o wartosci ', t.remove(10))
  print('Usunieto wezel o wartosci ', t.remove(120))
  not_exst_node_val = 130
  try:
    t.remove(not_exst_node_val)
  except Exception as e:
    z = e
    print('Proba usuniecia wezla o wartosci', not_exst_node_val)
    print(z)

  print('Po usuwaniu wezlow:')
  t.inorder(t.root)

  print('Liczba wezlow w drzewie:', t.count(t.root))