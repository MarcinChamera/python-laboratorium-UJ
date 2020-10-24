line = """Język Python stworzony przez
Guido van Rossum, holenderskiego programistę,
jest jednym z najpopularniejszych
języków programowania w ostatnich latach"""
word_list = list()
for line in line.splitlines():
	for word in line.split():
		word_list.append(word)
alphabetical_order = sorted(word_list)
length_order = sorted(word_list, key=len)
print(alphabetical_order)
print(length_order)