x = 2; y = 3;
if (x > y):
    result = x;
else:
    result = y;
#Kod jest poprawny

for i in "qwerty": if ord(i) < 100: print (i)
#Kod jest niepoprawny, ponieważ w Pythonie taki blok instrukcji moglibyśmy wykonać albo za pomocą list comprehension albo tak jak w przykładzie poniżej

for i in "axby": print (ord(i) if ord(i) < 100 else i)
#Kod jest poprawny