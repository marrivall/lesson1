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
