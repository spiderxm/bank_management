import mysql.connector
mydb = mysql.connector.connect(
    host = "database.ct1ikgzgdh96.us-east-1.rds.amazonaws.com",
    user = "admin",
    passwd = "mrigank52"
)
mycursor = mydb.cursor()

# mycursor.execute("CREATE DATABASE BANK ")

mycursor.execute("USE BANK")

mycursor.execute("create table if not exists account_holder( account_holder varchar(255), address varchar(255),  phone_number varchar(20), account_number varchar(20) primary key, account_type varchar(20)")
# try:
#     mycursor.execute("SHOW TABLES")
# except:
#     print("")
#
# for x in mycursor:
#     print(x)

mycursor.close()

mydb.close()