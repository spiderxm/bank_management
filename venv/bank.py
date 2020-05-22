from random import randint
import mysql.connector
# mydb = mysql.connector.connect(
#     host = "database.ct1ikgzgdh96.us-east-1.rds.amazonaws.com",
#     user = "admin",
#     passwd = "mrigank52",
#     dbname = "BANK"
# )
# mycursor = mydb.cursor()
def create_user():
    account_holder = input("Enter your name : ")
    address = input("Enter your address : ")
    phone_number = input("Enter your phone number :")
    account_type = input("Choose account type between lite, elite, executive : ")
    account_number = str(randint(100 ** 9, (100 ** 10) - 1))
    if len(account_holder) > 3 and len(address) > 9  and len(phone_number) > 7 and len(account_type) > 3:
        print(account_holder, "your account number is ", account_number, "and keep it classified and safe")
        try:
            mycursor.execute("INSERT INTO ")
        except:
            print("Error")
    else:
        print("Please fill the fields correctly")
        create_user()

# create_user()
def withdrawal():
    account_number = input("Enter your account number : ")
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
    amount = input("Enter amount you want to deposit : ")
    try:
        mycursor.execute("UPDATE account_balance SET balance = balance + %s WHERE account_number = %s", amount, account_number)
    except:
        print("Error")

def transfer():
    your_account_number = input("Enter your account number : ")
    account_number = input("Enter Account number of the account in which you want to transfer money : ")
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
            mycursor.execute("UPDATE account_balance SET balance = %s WHERE account_number = %s", balance, your_account_number)
            mycursor.execute("UPDATE account_balance SET balance = balance + %s WHERE account_number = %s", amount, account_number)
            print("Transaction Successful")
        except:
            print("Error")
    else:
        print("Insufficient funds in your bank account")
