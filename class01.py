# # # # name = "Fahim" # String
# # # # age = 27 # Integer
# # # # height = 5.9 # Float
# # # # under_18 = False # Boolean

# # # # print(f"{name}\n{age}\n{height}\n{under_18}")

# # # # stdList = ["Fahim","John","Naeem","Zak","Zaman"]

# # # # print(stdList)
# # # # print(stdList[1])
# # # # print(stdList[3])

# # # import random
# # # listToss = ["Heads","Tails"]
# # # listDice = [1,2,3,4,5,6]

# # # for x in range(6):
# # #     # print(random.choice(listToss))
# # #     print(random.choice(listDice))

# # # stdList = ["Fahim","John","Naeem","Zak","Zaman"]

# # # for student in stdList:
# # #     print(student)

# # # first_name = input("Please Enter the First Name: ")
# # # last_name = input("Please Enter the Last Name: ")

# # # print(f"The Full Name is this: {first_name} {last_name}")

# # # stdList = ["Fahim","John","Naeem","Zak","Zaman"]
# # # print(stdList)
# # # stdList.append("Nuh")
# # # print(stdList)

# number_of_student = int(input("Please enter the number of students: "))
# studentList = []
# for x in range(number_of_student):
#     studentName = input(f"Please Enter the {x+1} Student Name: ")
#     studentList.append(studentName)
# print(studentList)


# # stdList = ["Fahim","John","Naeem","Zak","Zaman"]
# # print(stdList)
# # stdList.append("Nuh")
# # print(stdList)
# # stdList.pop(3)
# # print(stdList)

# # import random
# # import time 
# # responses = ["yes","no","maybe"]
# # question = input("Please ask me a question: 9")
# # time.sleep(2)
# # print(random.choice(responses))


# # i = 0
# # while i < 5:
# #     print(f"hello: {i}")
# #     i = i + 1 # increament        

# number_of_student = int(input("Please enter the number of students: "))
# studentList = []
# x = 0
# while x < number_of_student:
#     studentName = input(f"Please Enter the {x+1} Student Name: ")
#     studentList.append(studentName)
#     x = x + 1
# print(studentList)

def square(x): # input parameters    
    result = f"The square of {x} is: {x*x}" # actual logic/code
    return result #retrun parameter
user_number = int(input("Enter the number please: "))
print(square(user_number))