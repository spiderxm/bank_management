from random import randint
import mysql.connector
mydb = mysql.connector.connect(
    host = "database.ct1ikgzgdh96.us-east-1.rds.amazonaws.com",
    user = "admin",
    passwd = "mrigank52"
)
def create_user():
    account_holder = input("Enter your name : ")
    address = input("Enter your address : ")
    phone_number = input("Enter your phone number :")
    account_type = input("Choose account type between lite, elite, executive : ")
    account_number = str(randint(100 ** 9, (100 ** 10) - 1))
    print(account_holder, "your account number is ", account_number, "and keep it classified and safe")

print(mydb)
mycursor = mydb.cursor()
mycursor.execute("SHOW DATABASES")

create_user()