#function in python

# A function is a reusable block of code that performs a specific task.
# It runs when it is called.

# Greeting Function
# def greeting(name):
#     print("Welcome", name)

# greeting("Khushi")


# Addition Function
# def add():
#     a = int(input("Enter first number: "))
#     b = int(input("Enter second number: "))
#     print("Sum =", a + b)

# add()

# Even or Odd
# def even_odd(num):
#     if num % 2 == 0:
#         return "Even"
#     else:
#         return "Odd"

# number = int(input("Enter an integer: "))

# result = even_odd(number)
# print("The number is", result)

# Fatorial calculator
# def factorial():
#     n = int(input("Enter a number: "))
#     fact = 1

#     for i in range(1, n + 1):
#         fact = fact * i

#     print("Factorial =", fact)

# factorial()

# Largest of three numbers
# def largest():
#     a = int(input("Enter first number: "))
#     b = int(input("Enter second number: "))
#     c = int(input("Enter third number: "))

#     if a >= b and a >= c:
#         print("Largest =", a)
#     elif b >= a and b >= c:
#         print("Largest =", b)
#     else:
#         print("Largest =", c)

# largest()


# Grade calculator
# def grade():
#     marks = int(input("Enter your marks: "))

#     if marks >= 90:
#         print("Grade A")
#     elif marks >= 75:
#         print("Grade B")
#     elif marks >= 60:
#         print("Grade C")
#     elif marks >= 33:
#         print("Grade D")
#     else:
#         print("Fail")

# grade()

# List statistics
# def statistics():
#     numbers = []

#     n = int(input("How many numbers: "))

#     for i in range(n):
#         num = int(input("Enter a number: "))
#         numbers.append(num)

#     print("Total =", sum(numbers))
#     print("Average =", sum(numbers) / len(numbers))
#     print("Minimum =", min(numbers))
#     print("Maximum =", max(numbers))

# statistics()

# Banking application
# def banking():
#     balance = 1000

#     while True:
#         print("1. Deposit")
#         print("2. Withdraw")
#         print("3. Check Balance")
#         print("4. Exit")

#         choice = input("Enter your choice: ")

#         if choice == "1":
#             amount = int(input("Enter deposit amount: "))
#             if amount > 0:
#                 balance = balance + amount
#                 print("Amount deposited successfully")
#             else:
#                 print("Invalid amount")

#         elif choice == "2":
#             amount = int(input("Enter withdrawal amount: "))
#             if amount > 0 and amount <= balance:
#                 balance = balance - amount
#                 print("Amount withdrawn successfully")
#             else:
#                 print("Invalid amount or insufficient balance")

#         elif choice == "3":
#             print("Balance =", balance)

#         elif choice == "4":
#             print("Thank you!")
#             break

#         else:
#             print("Invalid choice")

# banking()

# Student record processor
# def student():
#     name = input("Enter student name: ")

#     hindi = int(input("Enter Hindi marks: "))
#     english = int(input("Enter English marks: "))
#     maths = int(input("Enter Maths marks: "))

#     total = hindi + english + maths
#     average = total / 3

#     print("Student Name:", name)
#     print("Total Marks:", total)
#     print("Average Marks:", average)

#     if hindi >= 33 and english >= 33 and maths >= 33:
#         print("Result: Pass")
#     else:
#         print("Result: Fail")

# student()