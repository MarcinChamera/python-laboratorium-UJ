import random

def binarne_rek(L, left, right, y):
    """Wyszukiwanie binarne w wersji rekurencyjnej."""
    if right >= left: 
  
        mid = (right + left) // 2
  
        # If element is present at the middle itself 
        if L[mid] == y: 
            return mid 
  
        # If element is smaller than mid, then it can only 
        # be present in left subarray 
        elif L[mid] > y: 
            return binarne_rek(L, left, mid - 1, y) 
  
        # Else the element can only be present in right subarray 
        else: 
            return binarne_rek(L, mid + 1, right, y) 
  
    else: 
        # Element is not present in the array 
        return None

if __name__ == '__main__':
	n = 99
	k = 50
	L = [random.randint(0, n) for _ in range(k)]
	print(L)
	for _ in range(k//10):
		y = random.randint(0, n)
		index = binarne_rek(L, 0, len(L)-1, y)
		print(y, 'not found' if index is None else 'found at index {0}'.format(index))