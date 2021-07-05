import random
Number = random.sample(range (-100, 100), 30)
print (Number)
print ("\nМаксимальне число: ", max(Number))
print ("Порядковий номер: ", Number.index(max(Number))+1, "\n")
print ("Пошук пари від’ємних чисел, що стоять поруч")
for a in range(29):
   if Number[a] < 0 and Number[a+1]< 0:
      print("Числа => ", str(Number[a]), "<---------------->", str(Number[a+1]))
