
# input from user

print ("Hello!")
name = input("What is your name? \n >")
first_number = float(input("Enter your first number \n >"))
second_number = float(input("Alright, what is your second number? \n >"))
operational= input(" Enter '+' to add \n '-' to subtract \n '*' to multiply \n or '/' to divide \n > ")


# defining operations

def add(x,y,z):
    add_ans = y + z
    print (x,"your answer is",add_ans)

def sub(x,y,z):
    sub_ans = y - z
    print (x, "your answer is",sub_ans)

def mul(x,y,z):
    mul_ans = y * z
    print (x, "your answer is",mul_ans)

def div(x,y,z):
    div_ans = y / z
    print (x, "your answer is",div_ans)


# identifying larger number for subtraction and division through if function

if first_number > second_number and operational == "-":
    sub(name,first_number,second_number)
elif second_number > first_number and operational == "-":
    sub(name,second_number,first_number)

elif first_number > second_number and operational == "/":
    div(name,first_number,second_number)
elif second_number > first_number and operational == "/":
    div(name,second_number,first_number)


elif operational == "+":
    add(name,second_number,first_number)

elif operational == "*":
    mul(name,first_number,second_number)


else:
    print("invalid operation request")


# "for calculation w/ more numbers

'''yesorno = input("Do you want to include another number? \n >")

while "y" or "ok" in yesorno:
    extra_numbers = input("What is the number? \n >")
    yesorno = input("Do you want to include another number? \n >")'''


choice = input ("do you want to add multiple numbers? : ")
if choice == "yes":
    how_many = int(input("how many numbers do you want to add : "))
    first_number = int (input("enter number 1 : "))
    for i in range (2,how_many+1):
        next_number = int(input("enter your number",i," : "))
        first_number = next_number + first_number
    print (first_number)
