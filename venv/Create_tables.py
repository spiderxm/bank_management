import mysql.connector
from datetime import datetime

mydb = mysql.connector.connect(
    host="bank.ct1ikgzgdh96.us-east-1.rds.amazonaws.com",
    user="admin",
    passwd="adminadmin"
)
mycursor = mydb.cursor()
try:
    mycursor.execute("CREATE DATABASE IF NOT EXISTS BANK ")
except:
    print("Error")

try:
    mycursor.execute("USE BANK")
except:
    print("Error")

try:
    mycursor.execute("DROP TABLE IF EXISTS account_holder")
except:
    print("Error deleting account_holder")
try:
    mycursor.execute("DROP TABLE IF EXISTS account_balance")
except:
    print("Error deleting account_balance table")
try:
    mycursor.execute("DROP TABLE IF EXISTS account_history")
except:
    print("Error deleting account_history table")
try:
    mycursor.execute("DROP TABLE IF EXISTS balance_transfer")
except:
    print("Error deleting balance transfer table")
try:
    mycursor.execute("CREATE TABLE if NOT EXISTS account_holder("
                     "account_holder varchar(255) NOT NULL , "
                     "email varchar(30) NOT NULL , "
                     "address varchar(255)  NOT NULL , "
                     "phone_number varchar(20)  NOT NULL , "
                     "account_number varchar(20) primary key  NOT NULL , "
                     "account_type varchar(20)  NOT NULL , "
                     "initial_amount decimal(30,5)  NOT NULL ,"
                     "account_creation_time TIMESTAMP DEFAULT CURRENT_TIMESTAMP )")
except:

    print("Error creating account_holder ")
try:
    mycursor.execute("CREATE TABLE if NOT EXISTS account_balance("
                     "account_number varchar(20) primary key NOT NULL, "
                     "balance decimal(30,5) NOT NULL )")
except:
    print("Error creating account_balance table")
    # print(123)
try:
    mycursor.execute("CREATE TABLE if NOT EXISTS balance_tranfer("
                     "from_account_number varchar(20)  NOT NULL, "
                     "to_account_number varchar(20)  NOT NULL, "
                     "amount decimal(30,5)  NOT NULL,"
                     "transaction_time TIMESTAMP default CURRENT_TIMESTAMP)")
except:
    print("Error creating balance_transfer table")
try:
    mycursor.execute("CREATE TABLE if NOT EXISTS account_history("
                     "account_number varchar(20) NOT NULL, "
                     "payment_type varchar(10) NOT NULL, "
                     "balance_before decimal(30,5) NOT NULL, "
                     "balance_afterwards decimal(30,5) NOT NULL, "
                     "comments varchar(255), "
                     "transaction_time TIMESTAMP default CURRENT_TIMESTAMP )")
except:
    print("Error creating account_history table")
try:
    mycursor.execute(
        "INSERT INTO account_holder(account_holder, email, address, phone_number, account_number, account_type, initial_amount) VALUES "
        "('mrigank anand', 'mrigank@nith.ac.in', 'kailash boys hostel nith', '9999888877', '87151766626366737611', 'elite', 100000), "
        "('aman chauhan', 'aman-d-1-n-only@nith.ac.in', 'kailash boys hostel nith', '9876543211', '92120805165080483546','lite', 990000), "
        "('shekhar motiyan', 'shekhar@nith.ac.in', 'kailash boys hostel nith', '9999999999', '11458183925071153386', 'executive', 10000)"
    )
except:
    print("Error inserting values into account_holder table")
try:
    mycursor.execute("INSERT INTO account_balance(account_number, balance) VALUES "
                     "('87151766626366737611', 100000),"
                     "('92120805165080483546', 990000),"
                     "('11458183925071153386', 10000)")
except:
    print("Error inserting values into account_balance table")

try:
    mycursor.execute(
        "INSERT INTO account_history(account_number, payment_type, balance_before, balance_afterwards, comments) values "
        "('87151766626366737611', 'deposit', 0, 100000, 'Deposit made on account opening'),"
        "('92120805165080483546', 'deposit', 0, 990000, 'Deposit made on account opening'),"
        "('11458183925071153386', 'deposit', 0, 10000, 'Deposit made on account opening')")
except:
    print("Error inserting values into account_history")

print("Commands successfull")

mydb.commit()
mycursor.close()
mydb.close()
