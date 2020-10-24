word = 'Word'
for c in word:
	print(c, end='')
	if c != word[-1]:
		print('_', end='')