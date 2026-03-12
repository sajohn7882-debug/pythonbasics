# num=5

# while num<=15:

#     print(num)

#     num+=1
# create a script starting with 50
# num=50
# while num>=0:
#     print(num)
#     num-=1

secret=7
guess=0
while guess!=secret:
    guess=int(input("Enter the number"))
    if guess == secret:
        print("correct")
    else:
        print("Try again")
cars=["mercedes","Volvo", "Bmw", "Mazda", "Subaru"]
for i in cars:
    print(i)