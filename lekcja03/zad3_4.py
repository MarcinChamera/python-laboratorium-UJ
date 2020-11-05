# Napisać program pobierający w pętli od użytkownika liczbę rzeczywistą x (typ float)
#i wypisujący parę x i trzecią potęgę x. Zatrzymanie programu następuje po wpisaniu
#z klawiatury stop. Jeżeli użytkownik wpisze napis zamiast liczby, to program ma wypisać
#komunikat o błędzie i kontynuować pracę.
from re import search
while True:
	x = input("Podaj liczbę rzeczywistą x: ")
	if isinstance(x, float):
		print('Druga potęga:', x**2, ', trzecia potęga:', x**3)
	if search('[a-zA-Z]', the_string) != None:
		print('To nie jest liczba, spróbuj ponownie :)')
	if x == 'stop':
		break
