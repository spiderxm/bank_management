import mysql.connector
from datetime import datetime

mydb = mysql.connector.connect(
    host="database.ct1ikgzgdh96.us-east-1.rds.amazonaws.com",
    user="admin",
    passwd="mrigank52"
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
    print("DROP TABLE IF EXISTS account_holder")
except:
    print("Error")
try:
    print("DROP TABLE IF EXISTS account_balance")
except:
    print("Error")
try:
    mycursor.execute("CREATE TABLE if NOT EXISTS account_holder("
                     "account_holder varchar(255), "
                     "email varchar(30), "
                     "address varchar(255), "
                     "phone_number varchar(20), "
                     "account_number varchar(20) primary key, "
                     "account_type varchar(20), "
                     "amount decimal(30,5),"
                     "account_creation_time datetime NOT NULL)")
except:
    print("Error")
try:
    print("CREATE TABLE if NOT EXISTS account_balance("
          "account_number int primary key, "
          "balance decimal(30,5), "
          "foreign key(account_number) references account_holder(account_number))")
except:
    print("Error")
try:
    print("CREATE TABLE if NOT EXISTS balance_tranfer("
          "from varchar(20), "
          "to varchar(20), "
          " amount decimal(30,5), "
          "foreign key (from,to) references account_holder(account_number))")
except:
    print("Error")
try:
    print("CREATE TABLE if NOT EXISTS account_history("
          "account_number varchar(20) NOT NULL , "
          "payment_type varchar(10) NOT NULL, "
          "balance_before decimal(30,5) NOT NULL, "
          "balance_afterwards decimal(30,5)) NOT NULL, "
          "transaction_time datetime NOT NULL)")
except:
    print("Error")
try:
    time1 = datetime.today()
    time2 = datetime.today()
    time3 = datetime.today()
    time = time1, time2, time3
    mycursor.execute("INSERT INTO account_holder VALUES "
                     "('mrigank anand', 'mrigank@nith.ac.in', 'kailash boys hostel nith', '9999888877', '87151766626366737611', 'elite', 100000, %s), "
                     "('aman chauhan', 'aman-d-1-n-only@nith.ac.in', 'kailash boys hostel nith', '9876543211', '92120805165080483546',' lite', 990000, %s ), "
                     "('shekhar motiyan', 'shekhar@nith.ac.in', 'kailash boys hostel nith', '9999999999', '11458183925071153386', 'executive', 10000, %s),"
                     , time)
except:
    print("Error")
try:
    print("INSERT INTO account_balance VALUES "
          "('87151766626366737611', 100000),"
          "('92120805165080483546', 990000),"
          "('11458183925071153386', 10000)")
except:
    print("Error")
try:
    print("INSERT INTO account_history ")
except:
    print("Error")
# try:
#     print("INSERT INTO ")
# except:
#     print("Error")
