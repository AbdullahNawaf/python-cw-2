my_name = input("what is your name")
my_age = input("what is your age")
print (f"My name is {my_name} and I am {my_age} years old")

First_Number= float(input("number one: "))
Second_Number= float(input("number two: "))
operation= input("enter an operation:")

if operation == "+":
    print(First_Number + Second_Number)

elif operation == "-":
    print(First_Number - Second_Number)

elif operation == "*":
    print(First_Number * Second_Number)

elif operation == "/":
    print(First_Number / Second_Number)
else:
    print("operation not vaild")


bus_capacity = 50
People_Inside_Bus = float(input("People in bus"))
Like_to_enter_bus = float(input("People outside bus"))

empty_seats= bus_capacity - People_Inside_Bus

if empty_seats >= Like_to_enter_bus:
    print("you can enter")
else:
    print("its full you can't enter")
