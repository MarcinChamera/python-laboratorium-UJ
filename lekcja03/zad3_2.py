#Funkcja sort jest wykonywana "inplace", dlatego błędem jest założenie, że zwraca posortowaną listę i trzeba ten wynik przypisać do listy.
L = [3, 5, 4] ; L = L.sort()

#Próba przypisania trzech wartości do dwóch zmiennych
x, y = 1, 2, 3

#Jeśli ze zmiennej X chciano zrobić listę, trzeba było cyfry 1,2,3 ująć w kwadratowe nawiasy
X = 1, 2, 3 ; X[1] = 4

#Lista X ma tylko trzy elementy, a X[3] byłoby odwołaniem do czwartego elementu w liście
X = [1, 2, 3] ; X[3] = 4

#W Pythonie nie można modyfikować w ten sposób stringów, w zamian można użyć konkatenacji przy pomocy symbolu "+"
X = "abc" ; X.append("d")

#Map brakuje trzeciego argumentu, w którym przekazywalibyśmy podstawę potęgi
L = list(map(pow, range(8)))