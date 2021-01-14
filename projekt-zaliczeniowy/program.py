import random

class Node:
    '''Klasa reprezentująca węzeł drzewa.'''
    
    def __init__(self, data=None, left=None, right=None, parent=None):
        self.data = data
        self.left = left
        self.right = right
        self.parent = parent

    def __str__(self):
        return str(self.data)

    def insert(self, node):
        if node.data < self.data:  
            if self.left:
                self.left.insert(node)
            else:
                node.parent = self
                self.left = node
        else:   
            if self.right:
                self.right.insert(node)
            else:
                node.parent = self
                self.right = node

    def count(self):
        counter = 1
        if self.left:
            counter += self.left.count()
        if self.right:
            counter += self.right.count()
        return counter

    def search(self, data):
        if self.data == data:
            return self
        if data < self.data:
            if self.left:
                return self.left.search(data)
        else:
            if self.right:
                return self.right.search(data)
        return None

    # define BST_SEARCH_MIN_KEY(Node):
    # while (Node->left != NULL)
    #     Node = Node->left
    # return Node

    def __find_successor(self):
        node = self
        if self.right is not None:
            while self.left is not None:
                node = node.left
            return node
        tmp = self.parent
        while tmp is not None and tmp.left is not self:
            node = tmp
            tmp = tmp.parent
        return tmp

    def remove(self, data, bst):
        if data < self.data:
            if self.left:
                self.left = self.left.remove(data ,bst)
        elif self.data < data:
            if self.right:
                self.right = self.right.remove(data, bst)
        else:     
            print('Starting removing...')
            if self.left is None or self.right is None:
                y = self
            else:
                y = self.__find_successor()
            if y.left is not None:
                x = y.left
            else:
                x = y.right
            if x is not None:
                x.parent = y.parent
            if y.parent is None:
                bst.root = x
            else:
                if y == y.parent.left:
                    y.parent.left = x
                else:
                    y.parent.right = x
            if y != self:
                self.data = y.data
            return y

    # def remove(self, data):
    #     if data < self.data:
    #         if self.left:
    #             self.left = self.left.remove(data)
    #     elif self.data < data:
    #         if self.right:
    #             self.right = self.right.remove(data)
    #     else:     
    #         print('Starting removing', data)
    #         #korzeń
    #         if self.parent is None:
    #             self.left.parent = None
    #             self.left.right = self.right
    #             self.right.parent = self.left          
    #         # liść
    #         elif self.left is None and self.right is None:
    #             removed_node = self
    #             # liść mniejszy od rodzica
    #             if self.data < self.parent.data:
    #                 self.parent.left = None
    #             # liść równy lub większy od rodzica
    #             else:
    #                 self.parent.right = None
    #             return removed_node
    #         # węzeł do usunięcia posiada jeden węzeł potomny,
    #         # o mniejszej wartości
    #         if self.right is None and self.left is not None:
    #             self.parent.right = self.left
    #         # węzeł do usunięcia posiada jeden węzeł potomny,
    #         # o wartości co najmniej równej
    #         elif self.right is not None and self.left is None:
    #             self.parent.left = self.right
    #         # węzeł do usunięcia posiada dwa węzły potomne
    #             # węzeł ma mniejszą wartość niż rodzic
    #         elif self.data < self.parent.data:
    #             self.parent.left = self.left
    #             self.left.right = self.right
    #             # węzeł ma niemniejszą wartość niż rodzic
    #         else:
    #             self.parent.right = self.left
    #             self.left.right = self.right
    #         return self

class BinarySearchTree:
    '''Klasa reprezentująca binarne drzewo poszukiwań.'''

    def __init__(self):
        self.root = None

    def insert(self, node):
        '''Wstawia węzeł 'node' do drzewa w odpowiednie miejsce.'''
        if self.root:
            self.root.insert(node)
        else:
            self.root = node

    def count(self):
        '''Zwraca liczbę węzłów w drzewie.'''
        if self.root:
            return self.root.count()
        else:
            return 0

    def search(self, data):   
        '''Szuka w drzewie węzeł o podanej wartości 'data'.'''
        if self.root:
            return self.root.search(data)
        else:
            return None

    def remove(self, data):
        '''Usuwa z drzewa węzeł o podanej wartości 'data'.'''
        if self.search(data) is None:
            raise ValueError("W tym drzewie nie ma węzła z taką wartością.")
        return self.root.remove(data, self)

    def inorder(self, root):
        '''Przechodzi przez drzewo w kolejności poprzecznej (in-order)
        i wyświetla wartość, i rodzica każdego z odwiedzonych węzłów.'''
        if root:
            self.inorder(root.left)
            print('Node:', root.data, ', Parent:',
                root.parent.data if root.parent is not None else 'None')
            self.inorder(root.right)

if __name__ == '__main__':
    node_data = list(range(10))
    random.shuffle(node_data)
    print('Nodes to be inserted:', node_data)
    BST = BinarySearchTree()
    # for i in range(10):
    #     BST.insert(Node(i))
    while node_data:
        data = node_data.pop()
        print('Inserting', data)
        BST.insert(Node(data))
    print('count =', BST.count())
    BST.inorder(BST.root)
    for i in range(9, 0, -1):
        result = BST.search(i)
        print('BST search of {0}: {1}'.format(i, result))
        if result is not None:
            print('Removed node:', BST.remove(result.data))
            BST.inorder(BST.root)
