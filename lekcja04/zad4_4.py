def fibonacci(n):
    if n < 1:
        print('Incorrect number')
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
    	nxt = 1
    	curr = 1
    	prev = 0
    	for i in range(n):
    		nxt = curr + prev
    		curr = prev
    		prev = nxt
    	return nxt

print(fibonacci(8))