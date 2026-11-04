# a=10
# b=20
# c=a+b
# print(c)


# print("enter a value")
# a=input()
# b=input()
# c=a+b
# print(c)

# a=int(input("enter a value:"))
# b=int(input("enter a value"))
# c=a+b
# print(c)


# a=int(input("enter a value"))
# b=int(input("enter a value"))
# if(a>b):
#     print("a is greater")
# elif(a<b):
#     print("b is greater")   
# else:
#     print("a is equal to b")


Balance = 10000
Pin = 1234
print("Welcome to SBI ATM")
print("Insert a card")
option = input("Enter YES or NO ")
if (option == "yes"):
    print("Enter 4 digit Pin")
    digit = int(input())
    if digit == Pin:
        print("PIN is correct")
    else:
        print("pin is wrong")
        exit()
    print("Enter a select language:")
    print("1. KANNADA")
    print("2. ENGLISH")
    language = int(input())
    if language == 1:
        print("KANNADA selected")
    elif language == 2:
        print("ENGLISH selected")
    else:
        print("Wrong language selection")
        exit()
else:
    print("selection is wrong")
    exit()
print("select a option:")
print("1. withdraw")
print("2. deposit")
print("3. balanace enquiry")
option = int(input())
if option == 1:
    print("withdraw selected")
elif option == 2:
    print("deposit selected")
elif option == 3:
    print("balance enquiry selected")
else:
    print("Wrong option")
    exit()
print("select account type:")
print("1 saving")
print("2 current")
account=int(input())
if account==1:
    print("1 saving")
elif account==2:
    print("2 current")
else:
    print(" wrong option")  
    exit()  
print("enter a amount to withdraw:")
withdraw=int(input())
print("please wait:")
print("collect the cash")
bank_Balance = Balance - withdraw
print("Do you want to see balance 1. yes 2. no")
balance_option = input()
if (balance_option == "1"):
    print("Your balance is:", bank_Balance)
print("Transaction Successfully")
print("Visit again")