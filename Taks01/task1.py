import re
stroka = input("\nVedit slovo: ")
slovo = ''.join([i for i in stroka if not i.isdigit()])
numbers = re.findall(r'\d+', stroka) 
numbers = [int(i) for i in numbers] 
print("\n Без чисел: ", slovo)
print("Числа:", numbers)
print("\nMax елемент масиву:", max(numbers))
numbers.remove(max(numbers))
ChSlovo = ' '.join(word[0].upper() + word[1:-1] + word[-1:].upper() for word in slovo.split())
print("Змінений рядок:", ChSlovo)
index = [numbers[i]**i for i in range(0,len(numbers))] 
print("Числa, піднесені до степеню по їхніх індексах:",index)

