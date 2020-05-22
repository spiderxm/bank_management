from random import randint
import mysql.connector
from datetime import datetime, date, time

mydb = mysql.connector.connect(
    host="bank.ct1ikgzgdh96.us-east-1.rds.amazonaws.com",
    user="admin",
    passwd="adminadmin"
)
mycursor = mydb.cursor()
try:
    mycursor.execute("USE BANK")
except:
    print("Error connecting to the database")


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
            values = (account_holder, email, address, phone_number, account_number, account_type, float(amount),
                      account_creation_time)
            mycursor.execute("INSERT INTO account_holder VALUES ('%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s')",
                             values)
            print("Your Account has been successfully created")
            print("-----" * 2)
        except:
            print("There was some error in creating you account please try again later")
            print("-----" * 2)
        else:
            print("Please fill the fields correctly")
            create_user()


# create_user()
def withdrawal():
    account_number = input("Enter your account number : ")
    try:
        mycursor.execute("SELECT account_number FROM account_holder where account_number = '{}'".format(account_number))
    except:
        print("Error in checking account number")
    account = mycursor.fetchone()
    if account:
        print(account_number)
        amount = input("Enter amount you want to withdraw : ")
        amount = float(amount)
        try:
            query = "SELECT balance FROM account_balance WHERE account_number = '{}'".format(account_number)
            mycursor.execute(query)
        except:
            print("Error in retrieving previous balance")
        balance = float(mycursor.fetchone()[0])
        if balance >= amount:
            print("Transaction successful take money from cashier")
            balance_after_withdrawal = balance - amount
            try:
                query = "UPDATE account_balance SET balance = {} WHERE account_number = '{}'".format(balance_after_withdrawal,
                                                                                                     account_number)
                mycursor.execute(query)
                query = "INSERT INTO account_history(account_number, payment_type, balance_before, balance_afterwards, comments) values" \
                        "({}, 'withdraw', {}, {}, 'Withdrawal made from the account')".format(account_number, balance,
                                                                                              balance_after_withdrawal)
                print("Balance in your account after transaction is : ", balance_after_withdrawal)
                try:
                    mycursor.execute(query)
                except:
                    print("Error submitting record of your withdrawal")
            except:
                print("Error in updating balance")
        else:
            print("Insufficient funds in your bank account")

    else:
        print("Account number invalid or does not exist try again")
        withdrawal()


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


# Function to display all your transactions and money related events in your bank account
def passbook():
    account_number = input("Enter your account number to get all the transaction details of your account : ")
    mycursor.execute("SELECT account_number FROM account_holder")
    account_numbers = mycursor.fetchall()
    if account_numbers:
        print("*****************")
        query = "SELECT * FROM account_history WHERE account_number = '{}'".format(account_number)
        mycursor.execute(query)
        print("----------")
        for number, transaction in enumerate(mycursor):
            print("Transaction type :", transaction[1])
            print("Balance before transaction : ", float(transaction[2]))
            print("Balance after transaction :", float(transaction[3]))
            print("Date and time of transaction :", transaction[5])
            print("Message : ", transaction[4])
            print("*****************")
        print("----------")
        print("Thanks for selecting our bank you are a valuable customer")
    else:
        print("Account number invalid try again")
        passbook()


# Function to see the current balance for your account using account number
def balance():
    account_number = str(input("Enter your account number : "))
    try:
        query = "SELECT balance from account_balance where account_number = '{}'".format(account_number)
        mycursor.execute(query)
        balance = mycursor.fetchone()
        print("Balance in your account is : ", balance[0])
    except:
        print("Error your account maybe not correct")
        print("Please Try aggain")


# Function to deposit money in your account
def deposit():
    account_number = input("Enter your account number : ")
    mycursor.execute("SELECT account_number FROM account_holder where account_number = '{}'".format(account_number))
    number = mycursor.fetchall()
    if number:
        print(account_number)
        query = "SELECT balance from account_balance where account_number = '{}'".format(account_number)
        mycursor.execute(query)
        balance = mycursor.fetchone()
        balance = float(balance[0])
        amount = float(input("Enter amount you want to deposit : "))
        print(amount + balance)
        final_amount = amount + balance
        print(balance)
        query = "UPDATE account_balance SET balance = {} where account_number = '{}'".format(final_amount,
                                                                                             account_number)
        print(query)
        try:
            mycursor.execute(query)
            print("Amount added successfully")
            query = "INSERT INTO account_history(account_number, payment_type, balance_before, balance_afterwards, comments) values" \
                    "({}, 'deposit', {}, {}, 'Deposit made in account')".format(account_number, balance, final_amount)
            print(query)
            try:
                mycursor.execute(query)
                print("Deposit record successfully added")
            except:
                print("Error updating your records")
        except:
            print("Error updating amount in your account")

    else:
        print("Account number invalid try again")


# Function to show your details using your account number
def account_details():
    account_number = input("Enter your account number to show your details : ")
    try:
        query = "SELECT * FROM account_holder where account_number = '{}'".format(account_number)
        mycursor.execute(query)
        details = mycursor.fetchone()
        try:
            query = "SELECT balance from account_balance where account_number = '{}'".format(account_number)
            mycursor.execute(query)
            balance = mycursor.fetchone()
        except:
            print("Error getting your balance")
    except:
        print("Error")
    if details:
        print("Account holder name : ", details[0])
        print("Email id : ", details[1])
        print("Address : ", details[2])
        print("Phone number : ", details[3])
        print("Account type : ", details[5])
        print("Account opening amount : ", float(details[6]))
        print("Balance in your account is : ", balance[0])
    else:
        print("No details possibly wrong account number try again")
        account_details()


def menu():
    print("*" * 20)
    print("Choose 1 to select show your account details")
    print("*" * 20)
    print("Choose 2 to show your balance")
    print("*" * 20)
    print("Choose 3 to deposit money")
    print("*" * 20)
    print("Choose 4 to withdraw money")
    print("*" * 20)
    print("Choose 5 to show your account history (passbook)")
    print("*" * 20)
    print("Choose 6 to transfer money")
    print("*" * 20)
    choice = int(input("Enter your choice"))
    return choice


# print(" ----------W-E-L-C-O-M-E-----T-O------R-O-Y-A-L-----B-A-N-K-------")
# choice = menu()
# while True:
#     print(choice)
#     break

withdrawal()
mydb.commit()
mycursor.close()
mydb.close()
