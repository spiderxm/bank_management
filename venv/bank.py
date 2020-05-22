# Importing random module to create account number
from random import randint
# Importing mysql.connector to execute commands
import mysql.connector

# Connecting to MySql server created using Amazon Web Services
mydb = mysql.connector.connect(
    host="bank.ct1ikgzgdh96.us-east-1.rds.amazonaws.com",
    user="admin",
    passwd="adminadmin"
)
# Creating a cursor to run and execute commands
mycursor = mydb.cursor()
try:
    mycursor.execute("USE BANK")
except:
    print("Error connecting to the database")


# Function to create a Bank account holder
def create_user():
    account_holder = input("Enter your name : ")
    email = input("Enter your email : ")
    address = input("Enter your address : ")
    phone_number = input("Enter your phone number :")
    account_type = input("Choose account type between lite, elite, executive : ")
    amount = input("Initial deposit in your account")
    account_number = str(randint(100 ** 9, (100 ** 10) - 1))
    if len(account_holder) > 0 and len(address) > 2 and len(phone_number) > 0 and len(account_type) > 0 and len(
            email) > 3 and float(amount) > 0:
        try:
            query = "INSERT INTO account_holder(account_holder, email, address, phone_number, account_number, account_type, initial_amount) VALUES" \
                    "('{}','{}','{}','{}','{}','{}',{})".format(account_holder, email, address, phone_number,
                                                                account_number, account_type, float(amount))
            mycursor.execute(query)
            mydb.commit()
            try:
                query = "INSERT INTO account_balance(account_number, balance) VALUES " \
                        "('{}', {})".format(account_number, amount)
                mycursor.execute(query)
                mydb.commit()
                try:
                    query = "INSERT INTO account_history(account_number, payment_type, balance_before, balance_afterwards, comments) values " \
                            "('{}', 'deposit', 0, {}, 'Deposit made on account opening')".format(account_number, amount)
                    mycursor.execute(query)
                    mydb.commit()
                    print("Your Account has been successfully created")
                    print(account_holder, "your account number is ", account_number, "and keep it classified and safe")
                    print("-----" * 2)
                except:
                    print("Error updating deposit for your account in the ledger")
            except:
                print("Error updating balance in your new account")

        except:
            print("There was some error in creating you account please try again later")
            print("-----" * 2)
    else:
        print("Please fill the fields correctly")
        create_user()


# Function to withdraw money from your bank account using your account_number
def withdrawal():
    account_number = input("Enter your account number to withdraw money : ")
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
                query = "UPDATE account_balance SET balance = {} WHERE account_number = '{}'".format(
                    balance_after_withdrawal,
                    account_number)
                mydb.commit()
                mycursor.execute(query)
                query = "INSERT INTO account_history(account_number, payment_type, balance_before, balance_afterwards, comments) values" \
                        "({}, 'withdraw', {}, {}, 'Withdrawal made from the account')".format(account_number, balance,
                                                                                              balance_after_withdrawal)
                print("Balance in your account after transaction is : ", balance_after_withdrawal)
                try:
                    mycursor.execute(query)
                    mydb.commit()
                except:
                    print("Error submitting record of your withdrawal")
            except:
                print("Error in updating balance")
        else:
            print("Insufficient funds in your bank account")

    else:
        print("Account number invalid or does not exist try again")
        withdrawal()


# Function to tranfer money from one account to other account using account_numbers
def transfer():
    your_account_number = input("Enter your account number : ")
    mycursor.execute(
        "SELECT account_number FROM account_holder WHERE account_number = '{}'".format(your_account_number))
    account_number_ = mycursor.fetchone()
    if account_number_:
        print("Valid account number")
    else:
        print("Account number invalid try again")
        transfer()
    account_number = input("Enter Account number of the account in which you want to transfer money : ")
    mycursor.execute(
        "SELECT account_number FROM account_holder WHERE account_number = '{}'".format(your_account_number))
    account_number_ = mycursor.fetchone()
    if account_number_:
        print("Valid account number")
    else:
        print("Account number invalid try again")
        transfer()
    amount = input("Enter amount you want to withdraw : ")
    amount = float(amount)
    try:
        query = "SELECT balance FROM account_balance WHERE account_number = '{}'".format(your_account_number)
        mycursor.execute(query)
        balance = mycursor.fetchone()[0]
        balance = float(balance)
        print(balance)
        if balance >= amount:
            balance_new = balance - amount
            try:
                query = "UPDATE account_balance SET balance = {} WHERE account_number = '{}'".format(balance_new,
                                                                                                     your_account_number)
                mycursor.execute(query)
                mydb.commit()
            except:
                print("Error 1")
            try:
                query = "UPDATE account_balance SET balance = balance + {} WHERE account_number = '{}'".format(
                    amount,
                    account_number)
                mycursor.execute(query)
                mydb.commit()
            except:
                print("Error 2")
            new_balance = 0
            try:
                query = "SELECT balance FROM account_balance WHERE account_number = '{}'".format(account_number)
                mycursor.execute(query)
                new_balance = float(mycursor.fetchone()[0])
            except:
                print("Error 3")
            try:
                query = "INSERT INTO account_history(account_number, payment_type, balance_before, balance_afterwards, comments) values" \
                        "({}, 'withdraw', {}, {}, 'Money transferred {} to account_number {}')".format(
                    your_account_number,
                    balance,
                    balance_new,
                    amount,
                    account_number)
                mycursor.execute(query)
                mydb.commit()
            except:
                print("Error 4")
            try:
                query = "INSERT INTO account_history(account_number, payment_type, balance_before, balance_afterwards, comments) values" \
                        "({}, 'deposit', {}, {}, 'Money recieived {} from  account_number {}')".format(
                    your_account_number,
                    new_balance - amount,
                    new_balance,
                    amount,
                    account_number)
                mycursor.execute(query)
                mydb.commit()
            except:
                ("Error 5")
            print("Transaction Successful")
        else:
            print("Insufficient funds in your bank account")
    except:
        print("Error in getting balance")


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
            mydb.commit()
            print("Amount added successfully")
            query = "INSERT INTO account_history(account_number, payment_type, balance_before, balance_afterwards, comments) values" \
                    "({}, 'deposit', {}, {}, 'Deposit made in account')".format(account_number, balance, final_amount)
            print(query)
            try:
                mycursor.execute(query)
                mydb.commit()
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
        print("Account opening amount (initial balance) : ", float(details[6]))
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
    print("Choose 7 to create Bank in our account")
    choice = int(input("Enter your choice"))
    return choice


print(" ----------W-E-L-C-O-M-E-----T-O------R-O-Y-A-L-----B-A-N-K-------")
option = True
while option == True:
    choice = menu()
    print("You choosed option {}".format(choice))
    if choice == 1:
        account_details()
    if choice == 2:
        balance()
    if choice == 3:
        deposit()
    if choice == 4:
        withdrawal()
    if choice == 5:
        passbook()
    if choice == 6:
        transfer()
    if choice == 7:
        create_user()
    option = input("Enter 1 to continue or any other key to exit: ")
    if int(option) == 1:
        option = True
    else:
        option = False

# Finally committing any uncommitted changes
mydb.commit()
# Closing the cursor connection
mycursor.close()
# Closing the datbase connection
mydb.close()
