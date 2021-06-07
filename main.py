# #00-00
# print("Hello world! It is I, Arthur, son of Uther Pendragon, from the castle of Camelot.")
#
# #00-01
# print(50)
# print(-42.00001)
# print("Monty Python")
# print(True)
#
# #00-02
# my_int=1
# my_float=2.123
# my_str="Tis but scratch"
# my_bool=False
# print(type(my_int))
# print(type(my_float))
# print(type(my_str))
# print(type(my_bool))
#
# #00-03
# first_name = "Monty"
# last_name = "Python"
# full_name = first_name + " " + last_name
# print(full_name)
#
# #00-04
# print("What is your name?")
# name = input()
# print("What is your quest?")
# quest = input()
# print("What is your favorite color?")
# color = input()
# print(f"BRIDGEKEEPER: Stop.\nWho would cross the Bridge of Death must answer me these questions three.\n"
#       f"BRIDGEKEEPER: What is your name?\n{name}\nBRIDGEKEEPER: What is your quest?\n{quest}\nBRIDGEKEEPER: What is your favorite color?\n{color}\n"
#       f"----------\nTraveler info:\nYour name is Sir Lancelot of Camelot\nYour quest is to seek the Holy Grail\n"
#       "Your favorite color is blue\n----------\nBRIDGEKEEPER: Right. Off you go.")
#
# #00-05
# a = input('Enter the first number: ')
# b = input('Enter the second number: ')
# a = int(a)
# b = int(b)
# print(f"{a} + {b} = {a+b}")
# print(f"{a} - {b} = {a-b}")
# print(f"{a} * {b} = {a*b}")
# print(f"{a} / {b} = {a/b}")
# print(f"{a} % {b} = {a%b}")
# print(f"{a} ** {b} = {a**b}")
# print(f"{a} // {b} = {a//b}")
#
# #00-06
# a = 3
# b = 10
# c = -14.8
# d = True
# print(f"Available variables:\na = {a}\nb = {b}\nc = {c}\nd = {d}\n"
#       f"Result:\n{a} + {b} = {float(a+b)}\n"
#       f"{c} - {b} = {int(c-b)}\n"
#       f"{str(c)+str(b)}\n"
#       f"{a} - {a} = {bool(a-a)}")
#
# #00-07
# sign = input("There are 3 signs in front of you. Which one would you like to read? ")
# if sign == "right":
#     print('The right sign says: "DEAD PEOPLE ONLY"')
# elif sign == "left":
#     print('The left sign says: "BEWARE!"')
# elif sign == "middle":
#     print('The middle sign says: "CERTAIN DEATH"')
# else:
#     print(f"There is no {sign} sign")
#
# #00-08
# first = 1000
# second = 1000
# third = 999
# print(f"first = {first}, address id {id(first)}\n"
#       f"second = {second}, address id {id(second)}\n"
#       f"third = {third}, address is {id(third)}\n"
#       f"{first} is {second} = {first is second}\n"
#       f"{first} is {third} = {first is third}")
#
# #00-09
# my_number = 1
# print(my_number)
# del my_number
# print(my_number)
#
# #00-10
# print("--- Simple calculator ---\n"
#       "Let's add some numbers")
# first = input("Input your first value: ")
# operator = input("Input your operator: ")
# if operator != "+" and operator != "-" and operator != "*" and operator != "/":
#     print("usage: the operator must be '*' or '+' or '-' or '/'")
#     print("--- Simple calculator ---")
#     exit()
# second = input("Input your seconnd value: ")
# if operator == "+":
#     print(f"{first} + {second} = {int(first)+int(second)}")
# elif operator == "-":
#     print(f"{first} - {second} = {int(first) - int(second)}")
# elif operator == "*":
#     print(f"{first} * {second} = {int(first) * int(second)}")
# elif operator == "/":
#     print(f"{first} / {second} = {int(first) / int(second)}")
# print("--- Simple calculator ---")
#
# #00-11
x = input("Enter your first string: ")
y = input("Enter your second string: ")
#if not x or y:
#   print("...")
if x == "" or y == "":
    print("one of the string is empty")
    quit()
command = input("Enter your command: ")
if command == "find":
    print(y in x)
elif command == "concat":
    print(f"{x} {y}")
elif command == "beatbox":
    d = input("Enter your first beatbox number: ")
    f = input("Enter your second beatbox number: ")
    print((x*int(d))+(y*int(f)))

else:
    print("Usage: command find | concat | beatbox")
