line = """Wielowierszowy
napis w języku
Python"""
first_char_string = ''
last_char_string = ''
for line in line.splitlines():
	for word in line.split():
		first_char_string += word[0]
		last_char_string += word[-1]
print(first_char_string)
print(last_char_string)