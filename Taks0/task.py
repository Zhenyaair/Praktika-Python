from random import randint
x = []
y = []
maxnum = 0
for a in range(30):
    x.append(randint(-100, 100))
print("\n Список 30 випадкових чисел: \n",x)
for a in x:
    if a > maxnum:
        maxnum = a
print("\n Максимальне число iз спискy:",maxnum)
print(" Індекс:",x.index(maxnum)+1)
for a in x:
    if a % 2 == 0:
        continue
    else: y.append(a)
y.sort(reverse = True)
print("Список  впорядку зменшення елементів: ",y)
