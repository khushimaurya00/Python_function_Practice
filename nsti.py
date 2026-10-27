# # rectangle pattern

# for i in range (1,5):
#     for j in range (1,7):
#         print ("*", end=" ")
#     print()

# # Increasing triangle

# for i in range (1,8):
#     for j in range (i):
#         print("+",end=" ")
#     print()

# # Number Square

# for num in range (1,5):
#     for k in range (1,5):
#         print(k,end=" ")
#     print()

# # multiplication tables

# for num in range (2,11):
#     print("Table of" ,num)
#     for t in range(1,11):
#         multiply = num*t
#         print(num, "*",t,"=", multiply)

# # Classroom seating

# for c in range(1,6):
#     for r in range(1,9):
#         print("Seats",end=" ")
#     print()

# # prime number

# for i in range(2,51):
#     count=0
#     for j in range(1, i+1):
#         if i % j == 0:
#             count += 1
#     if count == 2:
#         print(i, end=" ")

# # Pattern challenge

# for i in range(1,6):
#     print(" " * (5 - i), end=" ")
#     print("* " * i)


#while loop

# i=1

# while i<= 10:
#     print(i)
#     i +=1

#even number b/t 1 to 20
# i=2

# while i<=20:
#     if i ==12:
#         break
#     print(i)
#     i +=2

#calculator programs

# print("My Calculator !")
# print("Type 'exit' to quit")

# while True:

#     op=input("Enter operation (+,-,*,/ or exit):")
#     if op == "exit":
#         print("Calculator closed!")
#         break
#     num1=float(input("Enter first number:"))
#     num2=float(input("Enter second number:"))

#     if op == "+":
#         print(num1,"+",num2,"=",num1+num2)
#     elif op == "-":
#         print(num1,"-",num2,"=",num1-num2)

#     elif op == "*":
#         print(num1,"*",num2,"=",num1*num2)
#     elif op == "/":
#         print(num1,"/",num2,"=",num1/num2)
#     else:
#         print("Invalid operation")

# try:
#     x=10
#     y=0
#     print(x / y)
# except ZeroDivisionError:
#     print("No. cannot be devided by 0")
# a=10
# b=10
# print(a * b)

# student={
#     "Name":"Khushi",
#     "Trade":"AIPA",
#     "Session":2026,
# }
# print(student["Trade"])


# try:
#     age=int(input("Enter your age:"))
#     print("Age is ",age)

# except ValueError:
#     print("Please enter a valid whole no.")


# try:
#     a=int(input("Enter first no."))
#     b=int(input("Enter second no."))

#     print(a / b)

# except ValueError:
#     print("Please enter valid integers")

# except ZeroDivisionError:
#     print("Cannot divide by 0.")

# print("Successful.")

# try:
#     a=int(input("Enter first no."))
#     b=int(input("Enter second no."))

#     print(a / b)

# except (ValueError, ZeroDivisionError):
#     print("Invalid entry!")

# print("Successful.")


# try:
#     num=int(input("enter number:"))

# except ValueError:
#     print("Invalid input.")

# else:
#     print("square of no. :", num**2)

# finally:
#     print("Run Successful!")
# try:
#     marks=int(input("Enter your marks:"))
#     if marks <0 or marks>100:
#       raise ValueError("Marks cannot be less than 0 or more than 100.")

# except ValueError as khushi:
#     print("Invalid marks",khushi)

# else:
#     print("marks accepted:",marks)

# finally:
#     print("coding completed")

# class AIPAError(Exception):
#     pass

# try:
#     eligible=int(input("input your qualification:"))
#     if eligible <= 10 :
#         raise AIPAError("You are not qualified for AIPA Admission.")
#     print("You are Eligible.")
# except ValueError:
#     print("please enter valid number.")

# except AIPAError as ai:
#     print("Eligibility issue: " ,ai)

# try:
#     num=int(input("enter number"))
#     print(100/0)

# except Exception as e:
#     print("Enter occured:",e)


