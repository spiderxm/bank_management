import mysql.connector

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


def money_in_bank():
    query = "SELECT SUM(balance) FROM account_balance"
    try:
        mycursor.execute(query)
        money = mycursor.fetchone()
        print("Total money in Royal bank is ", float(money[0]))
    except:
        print("Error")


def no_of_users():
    query = "SELECT COUNT(*) FROM account_holder"
    try:
        mycursor.execute(query)
        users = mycursor.fetchone()
        print("Number of users in Royal Bank is ", users[0])
    except:
        print("Error")


def average_money():
    query = "SELECT AVG(balance) FROM account_balance"
    try:
        mycursor.execute(query)
        avg_money = mycursor.fetchone()
        print("Average money in each account in Royal bank is ", float(avg_money[0]))
    except:
        print("Error")


def total_transactions():
    query = "SELECT COUNT(*) FROM account_history"
    try:
        mycursor.execute(query)
        transaction_number = mycursor.fetchone()
        print("Total Number of transactions made till date : ", transaction_number[0])
    except:
        print("Error")


def total_deposits():
    query = "SELECT COUNT(*) FROM account_history where payment_type = 'deposit'"
    try:
        mycursor.execute(query)
        transaction_number_deposit = mycursor.fetchone()
        print("Total Number of deposits made till date : ", transaction_number_deposit[0])
    except:
        print("Error")


def total_withdraw():
    query = "SELECT COUNT(*) FROM account_history where payment_type = 'withdraw'"
    try:
        mycursor.execute(query)
        transaction_number_withdraw = mycursor.fetchone()
        print("Total Number of deposits made till date : ", transaction_number_withdraw[0])
    except:
        print("Error")


def total_elite():
    query = "SELECT COUNT(*) FROM account_holder where account_type = 'elite'"
    try:
        mycursor.execute(query)
        elite = mycursor.fetchone()
        print("Total Number of elite accounts : ", elite[0])
    except:
        print("Error")


def total_executive():
    query = "SELECT COUNT(*) FROM account_holder where account_type = 'executive'"
    try:
        mycursor.execute(query)
        executive = mycursor.fetchone()
        print("Total Number of executive accounts : ", executive[0])
    except:
        print("Error")


def total_lite():
    query = "SELECT COUNT(*) FROM account_holder where account_type = 'lite'"
    try:
        mycursor.execute(query)
        executive = mycursor.fetchone()
        print("Total Number of lite accounts : ", executive[0])
    except:
        print("Error")


def users():
    query = "SELECT * FROM account_holder inner join account_balance on account_balance.account_number = account_holder.account_number"
    try:
        print("all user details of the bank")
        print("*" * 50)
        mycursor.execute(query)
        details = mycursor.fetchone()
        while details:
            print("*" * 250)
            print("Account holder name : ", details[0])
            print("Email id : ", details[1])
            print("Address : ", details[2])
            print("Phone number : ", details[3])
            print("Account type : ", details[5])
            print("Account opening amount (initial balance) (indian rupees) : ", float(details[6]))
            print("Current balance in account (indian rupees) : ",float(details[9]))
            details = mycursor.fetchone()
    except:
        print("Error retrieving records")

def account_transactions():
    query = "SELECT * FROM account_holder INNER JOIN account_history ON account_history.account_number = account_holder.account_number"
    try:

# total number of withdrawals
print("*" * 50)
total_withdraw()
# total number of deposits
print("*" * 50)
total_deposits()
# total number of transactions
print("*" * 50)
total_transactions()
# average money per bank account holder
print("*" * 50)
average_money()
# total money in bank accounts
print("*" * 50)
money_in_bank()
# total number of users
print("*" * 50)
no_of_users()
# total number of lite users
print("*" * 50)
total_lite()
# total number of elite users
print("*" * 50)
total_elite()
# total number of executive users
print("*" * 50)
total_executive()
# details of users of bank account holder
print("*" * 50)
users()

# closing the cursor
mycursor.close()
# closing the connection to the database
mydb.close()
