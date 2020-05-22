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
        transaction_number = mycursor.fetchone()
        print("Total Number of deposits made till date : ", transaction_number[0])
    except:
        print("Error")
total_deposits()
average_money()
money_in_bank()
no_of_users()
total_transactions()
mycursor.close()
mydb.close()
