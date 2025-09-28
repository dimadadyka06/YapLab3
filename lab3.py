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


#4
class Countdown:
    def __init__(self, n):
        self.n = n
        self.current = n

    def __iter__(self):
        return self

    def __next__(self):
        if self.current < 1:
            raise StopIteration
        value = self.current
        self.current -= 1
        return value

sim = int(input("введи число"))
print("класс итератор который возвращает число от",sim," до 1")
for x in Countdown(sim):
    print(x)


#5
def fibonacci(n):
    a, b = 0, 1
    count = 0
    while count < n:
        yield a
        a, b = b, a + b
        count += 1

print("генератор фибоначи")
n1 = int(input("введи длину фибоначи: "))
print("числа фибоначи")
for num in fibonacci(n1):
    print(num, end=" ")


