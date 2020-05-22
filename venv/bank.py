from random import randint
import mysql.connector
from datetime import datetime, date, time
# mydb = mysql.connector.connect(
#     host="database.ct1ikgzgdh96.us-east-1.rds.amazonaws.com",
#     user="admin",
#     passwd="mrigank52",
#     dbname="BANK"
# )
# mycursor = mydb.cursor()


def create_user():
    account_holder = input("Enter your name : ")
    address = input("Enter your address : ")
    email = input("Enter your email : ")
    phone_number = input("Enter your phone number :")
    account_type = input("Choose account type between lite, elite, executive : ")
    amount = input("Initial deposit in your account")
    account_creation_time = datetime.today()
    account_number = str(randint(100 ** 9, (100 ** 10) - 1))
    if len(account_holder) > 3 and len(address) > 9 and len(phone_number) > 7 and len(account_type) > 3 and len(
            email) > 6 and float(amount) > 0:
        print(account_holder, "your account number is ", account_number, "and keep it classified and safe")
        try:
            values = (account_holder, email, address, phone_number, account_number, account_type, float(amount), account_creation_time)
            mycursor.execute("INSERT INTO account_holder VALUES (%s,%s,%s,%s,%s,%s, %s, %s)", values)
            print("Your Account has been successfully created")
            print("-----" * 2)
        except :
            print("There was some error in creating you account please try again later")
            print("-----" * 2)
        else:
            print("Please fill the fields correctly")
            create_user()


# create_user()
def withdrawal():
    account_number = input("Enter your account number : ")
    mycursor.execute("SELECT account_number FROM account_holder")
    account_numbers = mycursor.fetchall()
    if account_number in account_numbers:
        print(account_number)
    else:
        print("Account number invalid try again")
        withdrawal()
    amount = input("Enter amount you want to withdraw : ")
    amount = float(amount)
    try:
        mycursor.execute("SELECT amount FROM account_balance WHERE account_number = %s", account_number)
    except:
        print("Error")
    balance = mycursor.fetchone()
    if balance >= amount:
        print("Transaction successful take money from cashier")
    else:
        print("Insufficient funds in your bank account")
    balance = balance - amount
    try:
        mycursor.execute("UPDATE account_balance SET balance = %s WHERE account_number = %s", balance, account_number)
    except:
        print("Error")


def deposit():
    account_number = input("Enter your account number : ")
    mycursor.execute("SELECT account_number FROM account_holder")
    account_numbers = mycursor.fetchall()
    if account_number in account_numbers:
        print(account_number)
    else:
        print("Account number invalid try again")
        deposit()
    amount = input("Enter amount you want to deposit : ")
    try:
        mycursor.execute("UPDATE account_balance SET balance = balance + %s WHERE account_number = %s", amount,
                         account_number)
    except:
        print("Error")


def transfer():
    your_account_number = input("Enter your account number : ")
    mycursor.execute("SELECT account_number FROM account_holder")
    account_numbers = mycursor.fetchall()
    if account_number in account_numbers:
        print(account_number)
    else:
        print("Account number invalid try again")
        transfer()
    account_number = input("Enter Account number of the account in which you want to transfer money : ")
    mycursor.execute("SELECT account_number FROM account_holder")
    account_numbers = mycursor.fetchall()
    if account_number in account_numbers:
        print(account_number)
    else:
        print("Account number invalid try again")
        transfer()
    amount = input("Enter amount you want to withdraw : ")
    amount = float(amount)
    try:
        mycursor.execute("SELECT amount FROM account_balance WHERE account_number = %s", your_account_number)
    except:
        print("Error")
    balance = mycursor.fetchone()
    if mycursor.fetchone() >= amount:
        try:
            balance = balance - amount
            mycursor.execute("UPDATE account_balance SET balance = %s WHERE account_number = %s", balance,
                             your_account_number)
            mycursor.execute("UPDATE account_balance SET balance = balance + %s WHERE account_number = %s", amount,
                             account_number)
            print("Transaction Successful")
        except:
            print("Error")
    else:
        print("Insufficient funds in your bank account")


def passbook():
    account_number = input("Enter your account number : ")
    mycursor.execute("SELECT account_number FROM account_holder")
    account_numbers = mycursor.fetchall()
    if account_number in account_numbers:
        print(account_number)
        mycursor.execute("SELECT * FROM transactions WHERE account_number = %s", account_number)
        print("----------")
        for transaction in mycursor:
            print(transaction)
        print("----------")
        print("Thanks for selecting our bank you are a valuable customer")
    else:
        print("Account number invalid try again")
        passbook()


print(datetime.today())
