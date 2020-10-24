line = """Wielowierszowy
napis w języku
Python"""
shortest_word = line[0]
longest_word = line[0]
for line in line.splitlines():
	for word in line.split():
		if len(word) < len(shortest_word):
			shortest_word = word
		elif len(word) > len(longest_word):
			longest_word = word
print("Najkrotsze slowo: {0:s}\nNajdluzsze slowo: {1:s}".format(shortest_word, longest_word))