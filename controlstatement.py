

# write a script that checks a ('python123') is valid else wrong password
# else wrong password

# correct_password = "7882"

# password = input("Enter your password: ")

# if password == correct_password:
#     print("Access granted")
# else:
#     print("Incorrect password")
# write a script that checks the largest number of three numbers
num1=int(input("Enter first number:"))
num2=int(input("Enter second number:"))
num3=int(input("Enter third number:"))
if num1>num2 and num1>num3:
    print(f"{num1} is the largest number")
elif num2>num1 and num2>num3:
    print(f"{num2} is the largest number")   
elif num3>num1 and num3>num2:
    print(f"{num3} is the largest number") 
else:
    print("they are equal")
