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
