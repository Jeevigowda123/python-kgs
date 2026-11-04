Balance = 10000
Pin = 1234
print("Welcome to SBI ATM")
print("\nInsert a card")
option = input("Enter YES or NO ")
if (option== "yes"):
    print("Enter 4 digit Pin")
    digit = int(input())
    if digit == Pin:
        print("PIN is correct")
    else:
            print("pin is wrong ")
            exit
    print("Enter a select language:")
    print("1. KANNADA")
    print("2. ENGLISH")
    language = int(input())
else:
    print("selection is wrong")
    exit

print("select a option:")
print("1. withdraw")
print("2. deposit")
print("3. balanace enquiry")
# option=input()
# print("select account type:")
# print("1 saving")
# print("2 current")
# account=input()
# print("enter a amount to withdraw:")
# withdraw=int(input())
# print("please wait:")
# print("collect the cash")
# bank_Balance = Balance - withdraw
# print("Do you want to see balance 1. yes 2. no")
# balance_option = input()
# if (balance_option == "1"):
#     print("Your balance is:", bank_Balance)
# print("Transaction Successfully")
# print("Visit again")



