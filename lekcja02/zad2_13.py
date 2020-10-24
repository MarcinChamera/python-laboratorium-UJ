line = """Wielowierszowy
napis w języku
Python"""
total_word_length = 0
for line in line.splitlines():
	for word in line.split():
		total_word_length += len(word)
print(total_word_length)