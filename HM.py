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
