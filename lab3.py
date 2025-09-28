#1
squares = [x**2 for x in range(1, 11)]
print("список квадротов чисел от 1 до 10\n",squares)


#2
even_numbers = [x for x in range(1, 20) if x % 2 == 0]
print("список только четных чисел из диапазона 1-20\n",even_numbers)


#3
words = ["python", "java", "c++", "rust", "go"]
result = [word.upper() for word in words if len(word) > 3]
print("все слова в верхнем регистре и длинее 3-х символов\n",result)
