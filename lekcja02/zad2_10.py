line = """Wielowierszowy
napis w języku
Python"""
number_of_words = 0
for line in line.splitlines():
	for word in line.split():
		number_of_words += 1
print(number_of_words)