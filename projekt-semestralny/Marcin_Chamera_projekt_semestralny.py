'''
Projekt semestralny Python
Algorytm binarnego drzewa poszukiwań ze wskaźnikiem do rodzica.
Autor: Marcin Chamera
'''
from math import pow, floor, log

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

  def DSW(self):
    '''Doprowadza drzewo do postaci zrównoważonej.'''
    if self.root:
      self.create_backbone(self.root, self.root)
      self.create_perfect_BST()

  def create_backbone(self, root, top):
    '''Zamienia drzewo w listę przez wielokrotne użycie metody rotate_right.'''
    left_child = None
    parent = top
    while parent:
      left_child = parent.left
      if left_child:
        root = self.rotate_right(root, parent)
        parent = left_child
      else:
        parent = parent.right
    self.root = root

  def rotate_right(self, root, top):
    '''Rotacja wierzchołków w prawo z zachowaniem struktury BST.'''
    if top.left is None:
      return root
    node = top.left
    top.left = node.right
    if node.right:
      node.right.parent = top
    node.parent = top.parent
    if top.parent is None:
      root = node
    elif top == top.parent.right:
      top.parent.right = node
    else:
      top.patent.left = node
    node.right = top
    top.parent = node
    return root

  def rotate_left(self, root, top):
    '''Rotacja wierzchołków w lewo z zachowaniem struktury BST.'''
    if top.right is None:
      return root, top
    node = top.right
    top.right = node.left
    if node.left:
      node.left.parent = top
    node.parent = top.parent
    if top.parent is None:
      root = node
    elif top == top.parent.left:
      top.parent.left = node
    else:
      top.parent.right = node
    node.left = top
    top.parent = node
    return root

  def create_perfect_BST(self):
    '''Przywraca kształt drzewa poprzez wielokrotne wywołanie metody
    make_rotations.'''
    root = self.root
    n = self.count(self.root)
    m = int(pow(2, floor(log(n+1, 2)))-1)
    root = self.make_rotations(root, n - m)
    while m > 1:
      m //= 2
      root = self.make_rotations(root, m)
    self.root = root

  def make_rotations(self, root, bound):
    '''Wykonuje wielokrotne lewe rotacja na co drugim węźle, względem jego
    rodzica.'''
    parent = root
    for _ in range(bound):
      if parent:
        root = self.rotate_left(root, parent)
        if parent.parent:
          parent = parent.parent.right
    return root

  def height(self, root):
    '''Zwraca wysokość drzewa.'''
    if root == None: 
        return 0
    return 1 + max(self.height(root.left), self.height(root.right))

import unittest

class TestBinarySearchTree(unittest.TestCase):
  def setUp(self):
    self.t = BinarySearchTree()
    self.nodes = [Node(10), Node(20), Node(30), Node(100), Node(90), Node(40),
      Node(50), Node(60), Node(70), Node(80), Node(150), Node(110), Node(120)]
    for node in self.nodes:
      self.t.insert(node)

  def test_print(self):      
    self.assertEqual(str(Node(10)), '10')

  def test_count(self):
    self.assertEqual(self.t.count(self.t.root), 13)

  def test_search(self):
    self.assertTrue(self.t.search(self.t.root, 50))
    self.assertFalse(self.t.search(self.t.root, 130))

  def test_remove(self):
    self.t.remove(10)
    self.assertEqual(self.t.count(self.t.root), 12)
    self.assertRaises(Exception, lambda: self.t.remove(10))
  
  def test_height(self):
    self.assertEqual(self.t.height(self.t.root), 10)

  def test_DSW(self):
    self.t.DSW()
    self.assertEqual(self.t.height(self.t.root), 4)

  def tearDown(self): pass

if __name__ == '__main__':
    unittest.main()