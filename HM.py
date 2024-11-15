# Клас «Правильний дріб»
class Fraction:
    def __init__(self, numer , den): #numer - numerator, den - denominator
        if den == 0:
            raise ValueError("Denominator can't be 0")
        self.numer  = numer
        self.den = den

    def __float__(self):
        return self.numer/self.den

    def __mul__(self, other):
        if isinstance(other, Fraction):
            new_numer = self.numer * other.numer
            new_den = self.den * other.den
            return Fraction(new_numer, new_den)
        else:
            raise ValueError("Illegal type of the argument")

    def __add__(self, other):
        if isinstance(other, Fraction):
            if self.den == other.den:
                return Fraction(self.numer + other.numer, self.den)
            else:
                new_denom = self.den * other.den
                new_numer = (self.numer * other.den) + (other.numer * self.den)
                return Fraction(new_numer, new_denom)
        else:
            raise ValueError("Illegal type of the argument")

    def __sub__(self, other):
        if isinstance(other, Fraction):
            if self.den != other.den:
                new_numer = self.numer * other.den - other.numer * self.den
                new_den = self.den * other.den
            else:
                new_numer = self.numer - other.numer
                new_den = self.den
            return Fraction(new_numer, new_den)
        else:
            raise ValueError("Illegal type of the argument")

    def __eq__(self, other):
        if isinstance(other, Fraction):
            return (self.numer == other.numer) and (self.den == other.den)
        else:
            return False

    def __lt__(self, other):
        if isinstance(other, Fraction):
            return self.__float__() < other.__float__()
        else:
            return False

    def __gt__(self, other):
        if isinstance(other, Fraction):
            return self.__float__() > other.__float__()
        else:
            return False

    def __str__(self):
        return f"Fraction:{self.numer}, {self.den}"

f_a = Fraction(2, 3)
f_b = Fraction(3, 6)
f_c = f_b + f_a
assert str(f_c) == 'Fraction: 21, 18'
f_d = f_b * f_a
assert str(f_d) == 'Fraction: 6, 18'
f_e = f_a - f_b
assert str(f_e) == 'Fraction: 3, 18'

assert f_d < f_c  # True
assert f_d > f_e  # True
assert f_a != f_b  # True
f_1 = Fraction(2, 4)
f_2 = Fraction(3, 6)
assert f_1 == f_2  # True
print('OK')










# Створити клас цифрового лічильника.
class Counter:
   def __init__(self, current=1, min_value=0, max_value=10):
       self.current = current
       self.min_value = min_value
       self.max_value = max_value

   def set_current(self, start):
       self.current = start

   def set_max(self, max_max):
       self.max_value = max_max

   def set_min(self, min_min):
       self.min_value = min_min

   def step_up(self):
       if self.current >= self.max_value:
           raise ValueError ("Досягнуто максимуму")
       else:
           self.current = self.current + 1

   def step_down(self):
       if self.current <= self.min_value:
           raise ValueError("Досягнуто мінімум")
       else:
           self.current = self.current - 1

   def get_current(self):
       return self.current

counter = Counter()
counter.set_current(7)
counter.step_up()
counter.step_up()
counter.step_up()
assert counter.get_current() == 10, 'Test1'
try:
    counter.step_up()  # ValueError
except ValueError as e:
    print(e) # Достигнут максимум
assert counter.get_current() == 10, 'Test2'

counter.set_min(7)
counter.step_down()
counter.step_down()
counter.step_down()
assert counter.get_current() == 7, 'Test3'
try:
    counter.step_down()  # ValueError
except ValueError as e:
    print(e) # Достигнут минимум
assert counter.get_current() == 7, 'Test4'

#Група студентів
class Human:
    def __init__(self, gender, age, name, surname):
        self.gender = gender
        self.age = age
        self.name = name
        self.surname = surname

    def __str__(self):
        return f'Human: Gender: {self.gender}, Age: {self.age}, Name: {self.name}, Surname: {self.surname}'

class Student(Human):
    def __init__(self, gender, age, name, surname, record_book):
        super().__init__(gender, age, name, surname)
        self.record_book = record_book

    def __str__(self):
        return f"Student: Gender: {self.gender}, Age: {self.age}, Name:{self.name}, Surname:{self.surname}, Record_book: {self.record_book}"

class Group:
    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if isinstance(student, Student):
            self.group.add(student)

    def delete_student(self, surname):
        self.group = {student for student in self.group if student.surname != surname}

    def find_student(self, surname):
        for student in self.group:
            if student.surname == surname:
                return student

    def __str__(self):
        all_students = '\n'.join(str(student) for student in self.group)
        return f'Number:{self.number}\n {all_students} '

st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
print(gr)
assert str(gr.find_student('Jobs')) == str(st1), 'Test1'
assert gr.find_student('Jobs2') is None, 'Test2'
assert isinstance(gr.find_student('Jobs'), Student) is True, 'Метод поиска должен возвращать экземпляр'
gr.delete_student('Taylor')
print(gr)
gr.delete_student('Taylor')  # No error!


#Очистити текст від html-тегів
import codecs
import re
def delete_html_tags(html_file, result_file='cleaned.txt'):
      with codecs.open(html_file, 'r', 'utf-8') as file:
          no_tags_text = []
          for line in file:
              no_tags_text = no_tags_text + re.findall(r'>(.+)</', line)
          if len(no_tags_text) > 0:
            print (f"Result:{no_tags_text}")
            with codecs.open(result_file, 'w', 'utf-8') as new_file:
                  new_file.write('\n'.join(no_tags_text))
delete_html_tags('D:\\Завантаження\\draft (1).html')

#Корзина для покупок
class Item:
    def __init__(self, name, price, description, dimensions):
        self.price = price
        self.description = description
        self.dimensions = dimensions
        self.name = name

    def __str__(self):
        return f"Name: {self.name}, Price: {self.price}, Dimensions: {self.dimensions}, Description: {self.description} "

class User:
    def __init__(self, name, surname, phonenumber):
        self.name = name
        self.surname = surname
        self.phonenumber = phonenumber

    def __str__(self):
        return f"{self.name} {self.surname}, Phone: {self.phonenumber}"

class Purchase:
    def __init__(self, user):
        self.products = {}
        self.user = user

    def add_item(self, item, cnt):
        if  item not in self.products:
            self.products[item] = cnt
        else:
            self.products[item] += cnt

    def __str__(self):
        all_products = ""
        for product, count in self.products.items():
            all_products = all_products + f"\n{product.name}:{count}pcs."
        return f"User: {self.user}\nItems: {all_products}\nTotal_cnt: {self.get_total()}"

    def get_total(self):
        return sum(product.price*count for product, count in self.products.items())

lemon = Item('lemon', 5, "yellow", "small", )
apple = Item('apple', 2, "red", "middle", )
print(lemon)
print(apple)
buyer = User("Ivan", "Ivanov", "02628162")

cart = Purchase(buyer)
cart.add_item(lemon, 4)
cart.add_item(apple, 20)
print(cart)
assert isinstance(cart.user, User) is True, 'Екземпляр класу User'
assert cart.get_total() == 60, "Всього 60"
assert cart.get_total() == 60, 'Повинно залишатися 60!'
print("Ok")

# Генератор простих чисел
def prime_generator(end):
    for num in range(2, end+1):
        for n in range(2, num): #n- дільники
            if num % n == 0:
                break
        else:
            yield num
from inspect import isgenerator
gen = prime_generator(1)
assert isgenerator(gen) == True, 'Test0'
assert list(prime_generator(10)) == [2, 3, 5, 7], 'Test1'
assert list(prime_generator(15)) == [2, 3, 5, 7, 11, 13], 'Test2'
assert list(prime_generator(29)) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29], 'Test3'
print('Ok')

# Перевірка на парність.
def is_even(number):
    num_is_even = str(number)[-1] in "02468"
    return num_is_even

assert is_even(2494563894038**2) == True, 'Test1'
assert is_even(1056897**2) == False, 'Test2'
assert is_even(24945638940387**3) == False, 'Test3'
print('Ok')


# Заповнення списку кубами чисел
def generate_cube_numbers(end):
    for x in range(2, end):
        cube_number = x**3
        if cube_number > end:
            return
        else:
            yield cube_number

from inspect import isgenerator

gen = generate_cube_numbers(1)
assert isgenerator(gen) == True, 'Test0'
assert list(generate_cube_numbers(10)) == [8], 'оскільки воно менше 10.'
assert list(generate_cube_numbers(100)) == [8, 27, 64], '5 у кубі це 125, а воно вже більше 100'
assert list(generate_cube_numbers(1000)) == [8, 27, 64, 125, 216, 343, 512, 729, 1000], '10 у кубі це 1000'
print("OK")

#Пошук першого слова
def first_word(text):
    text = text.replace('.', ' ').replace(',', ' ')
    text = text.strip()
    words = text.split()
    first_word = words[0]
    return first_word

assert first_word("Hello world") == "Hello", 'Test1'
assert first_word("greetings, friends") == "greetings", 'Test2'
assert first_word("don't touch it") == "don't", 'Test3'
assert first_word(".., and so on ...") == "and", 'Test4'
assert first_word("hi") == "hi", 'Test5'
assert first_word("Hello.World") == "Hello", 'Test6'
print('OK')

#Генераторна функція
def some_gen(begin, end, func):
    for x in range(end):
        yield begin
        begin = func(begin)

from inspect import isgenerator

gen = some_gen(2, 4, lambda x: x ** 2)
assert isgenerator(gen) == True, 'Test1'
assert list(gen) == [2, 4, 16, 256], 'Test2'
print('OK')

#Перевірити чи є парним чи ні
def is_even(digit):
    return digit % 2 == 0
assert is_even(2) == True, 'Test1'
assert is_even(5) == False, 'Test2'
assert is_even(0) == True, 'Test3'
print('OK')

# Різниця між числами
def difference (*nums):
    if  len(nums) == 0:
        return 0
    difference = round(max(nums)-min(nums), 2)
    return difference
assert difference(1, 2, 3) == 2, 'Test1'
assert difference(5, -5) == 10, 'Test2'
assert difference(10.2, -2.2, 0, 1.1, 0.5) == 12.4, 'Test3'
assert difference() == 0, 'Test4'
print('OK')

# Визначити популярність певних слів у тексті
def popular_words (text, words):
    text =  text.lower().split()
    popular_words = {}
    for word in words:
        result = text.count(word)
        popular_words[word] = result
    return popular_words
assert (popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near'])
        == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }), 'Test1'
print('OK')


#Додати 1
def add_one(some_list):
    one_number = ''.join([str(n) for n in some_list])
    result = int(one_number) + 1
    numbers =[]
    for n in str(result):
        num = int(n)
        numbers.append(num)
    return numbers
assert add_one([1, 2, 3, 4]) == [1, 2, 3, 5], 'Test1'
assert add_one([9, 9, 9]) == [1, 0, 0, 0], 'Test2'
assert add_one([0]) == [1], 'Test3'
assert add_one([9]) == [1, 0], 'Test4'
print("ОК")

#Унікальне число
def find_unique_value(nums: list[int]) -> list[int]:
    for num in nums:
        if nums.count(num) == 1:
            return num
assert find_unique_value([1, 2, 1, 1]) == 2, 'Test1'
assert find_unique_value([2, 3, 3, 3, 5, 5]) == 2, 'Test2'
assert find_unique_value([5, 5, 5, 2, 2, 0.5]) == 0.5, 'Test3'
print("ОК")

nums_list = input("Enter no more than 10 numbers:" )
numbers = nums_list.split()
if len(numbers) > 10:
    print("Invalid numbers. Please enter no more than 10 numbers.")
else:
    unique_value = []
    for num in numbers:
        if numbers.count(num) == 1:
            unique_value.append(num)
    print(unique_value)

#Паліандром
def is_palindrome(text):
    phrase = []
    for symbol in text:
        if symbol.isalpha() or symbol.isdigit():
            phrase.append(symbol.lower())
    phrase = "".join(phrase)
    is_palindrome = phrase == phrase[::-1]
    return is_palindrome

assert is_palindrome('A man, a plan, a canal: Panama') == True, 'Test1'
assert is_palindrome('0P') == False, 'Test2'
assert is_palindrome('a.') == True, 'Test3'
assert is_palindrome('aurora') == False, 'Test4'
print("ОК")

#Модифікувати рядок
def correct_sentence(text):
    if not text.endswith("."):
         text = text + "."
    sep = len(text) // 2
    part_1 = text[:sep].capitalize()
    part_2 = text[sep:]
    text = part_1 + part_2
    return text
assert correct_sentence("greetings, friends") == "Greetings, friends.", 'Test1'
assert correct_sentence("hello") == "Hello.", 'Test2'
assert correct_sentence("Greetings. Friends") == "Greetings. Friends.", 'Test3'
assert correct_sentence("Greetings, friends.") == "Greetings, friends.", 'Test4'
assert correct_sentence("greetings, friends.") == "Greetings, friends.", 'Test5'
print("OK")

#Пошук спільних елементів
def common_elements():
    first_list_3 = {num for num in range(100) if num % 3 == 0}
    second_list_5 = {num for num in range(100) if num % 5 ==0}
    common_el = first_list_3.intersection(second_list_5)
    return common_el
assert common_elements() == {0, 75, 45, 15, 90, 60, 30}
print("OK")

#Пошук підрядка
text = input("Перший рядок:")
some_str = input("Другий рядок: ")
def second_index(text, some_str):
    first_index = text.find(some_str)
    if first_index != -1:
        second_index = text.find(some_str, first_index + 1)
    if second_index != -1:
     return second_index
print(second_index(text, some_str))

#Вітання
def say_hi(name, surname, age):
  return f"Hi. My name is {name} {surname} and I'm {age} years old"

assert say_hi("Alex", "Dudkin", 60) == "Hi. My name is Alex Dudkin and I'm 60 years old", 'Test1'
assert say_hi("Frank", "Pupkin", 18) == "Hi. My name is Frank Pupkin and I'm 18 years old", 'Test2'

print(say_hi("Alex", "Dudkin", 60))
print(say_hi("Frank", "Pupkin", 18))


# Добуток чисел
number = int(input("Enter your number:"))
while number > 9:
    result = 1
    while number > 0:
     num = number % 10
     number = number // 10
     result = result * num
    number = result
    print(result)

#Конвертер із числа в дату
number = seconds = int(input("Enter your number:"))
if number in range(0, 8640000):
    days = seconds // (24 * 60 * 60)
    seconds = seconds % (24 * 3600) #3600 секунди в годині
    hours = seconds // 3600
    seconds = seconds % 3600
    minutes = seconds // 60
    seconds = seconds % 60
    result = f" {days}:{hours}:{minutes}:{seconds}"
    print(result)
else:
           print("incorrect number")




#Діапазон букв
import string
letters = input("Введіть дві літери через дефіс: ")

letters = letters.replace("-", " ")
letter_one, letter_two = letters.split()
letters = string.ascii_letters

letter_one = letters.index(letter_one)
letter_two = letters.index(letter_two)
result = letters[letter_one:letter_two +1]
print("Result:", result)





#hashtag
import string
phrase = input("Enter your phrase: ")

for symbol in phrase:
 if symbol  in string.punctuation:
     phrase = phrase.replace("symbol", "")

words = phrase.split()
phrasewords = []
for word in words:
    phrasewords.append(word.capitalize())
phrase = " ".join(phrasewords)
hashtag = "#" + "".join(phrasewords)

if len(phrase) > 140:
    hashtag = phrase[:140]

print(hashtag)


# Ім'я змінної
import string
import keyword
# print (keyword.kwlist)
name = input("Enter name:")

valid_name = True

if name[0].isdigit():
    valid_name = False

if name.upper():
    valid_name = False

for symbol in name:
  if symbol  in string.punctuation != "_" :
     valid_name = False

if name.count("_")  <= 1:
        valid_name = True

if name in keyword.kwlist:
  valid_name =  False

print(valid_name)



#Модифікувати калькулятор
while True:
        n1 = int(input("Enter your first number: "))
        maths_operation = input("Select your choice (+, -, *, /): ")
        n2 = int(input("Enter your second number: "))
        match maths_operation:
            case "+":
                result = n1+n2
            case "-":
                result = n1-n2
            case "*":
                result = n1*n2
            case "/":
                result = n1/n2
                if result == 0:
                    print("Ділення на 0 не дозволено")
        print("Result:", result)
        question = input("Продовжити роботу? (yes,no): ")
        if question  in "yes":
            continue
        elif question in "no":
            print("Завершення роботи")
            break






#Список із 3 елементів
i = 0
import random
list1 = []
NUM_SIZE = 10
for i in range (NUM_SIZE):
 list1.append (random.randint(3,10))
print (list1)

list2 = list1 [0], list1 [2], list1 [-2]
print (list2)


#Знайти суму елементів із парними індексами
i = 0
nums = [1,3,5,8,9,6,4]
for i in range(0, len(nums), 2):
    print (nums[i])
nums2 = sum(nums[i] for i in range(0, len(nums), 2))
result = nums2 * 4
print ("Result:", result )


#Перемістити всі нулі до кінця списку
nums = [4,0,3,0,5]
num1 = nums.remove (0)
num2 = nums.remove (0)
nums.append(0)
nums.append(0)
print (nums)





#HOMEWORK
# Найпростіший калькулятор
#V1
# n1 = int(input("Enter your number"))
# maths_operation = input("Select your choice (+, -, *, /" )
# n2 = int(input("Enter your number"))
# if maths_operation == "+":
#     result = n1+n2
# elif maths_operation == "-":
#     result = n1 - n2
# elif maths_operation == "*":
#     result = n1 * n2
# elif maths_operation == "/"!= 0:
#     result = n1 / n2
# else:
#     print ("Invalid input, please, try again")
#
# print ("Result:", result)

#V2
# n1 = int(input("Enter your number"))
# maths_operation = input("Select your choice (+, -, *, /" )
# n2 = int(input("Enter your number"))
# match maths_operation:
#     case "+":
#         result = n1+n2
#     case "-":
#         result = n1 - n2
#     case "*":
#         result = n1*n2
#     case "/":
#         result = n1/n2
#     case "/!= 0":
#           print ("Invalid input, please, try again")
# print ("Result:", result )


#Перемістити елемент у списку
# numbers = [1,5,7,4,9,8]
# numbers.insert (0, 8)
# print (numbers)
#
# result = numbers.pop()
# print (result)
# print (numbers)



#Розділити один список на два
# 1)
# nums = [2,5,8,3,9,4]
# first_part = nums[:len(nums) // 2]
# second_part = nums[:len(nums) // 2:]
# result = [first_part,second_part]
# print (result)
#2)
# nums = [3,7,6,4,9]
# first_part = nums[:3]
# second_part = nums [3:]
# result = [first_part,second_part]
# print (result)
#3)
# nums = []
# first_part = nums [:len(nums)//2]
# second_part = nums [len (nums) //2 :]
# result = [first_part,second_part]
# print (result)
