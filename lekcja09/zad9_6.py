class Node:
    """Klasa reprezentująca węzeł drzewa binarnego."""

    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.data)

def count_leafs(top):
	if (top == None):
	    return 0
	if (top.left == None and top.right == None):
	    return 1
	return count_leafs(top.left) + count_leafs(top.right)

def count_total(top):
    if (top == None): 
        return 0
    return (top.data + count_total(top.left) + count_total(top.right))

if __name__ == '__main__':
	root = None           # puste drzewo
	root = Node("alone")  # drzewo z jednym węzłem
	# Ręczne budowanie większego drzewa.
	root = Node(1)
	root.left = Node(2)
	root.right = Node(3)
	root.left.left = Node(4)
	root.left.right = Node(5)
	root.right.left = Node(6)
	root.right.right = Node(7)
	print(count_leafs(root))
	print(count_total(root))