"""
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="myusername",
  password="mypassword"
)

# Cursor: A cursor is a database object that lets you fetch and process rows from a query result one at a time.
mycursor = mydb.cursor()   

# Execute Function: The execute() function runs SQL statements on the database.
mycursor.execute("create database Mydatabase") #create database = command line #Mydatabase = New database name
# print(mydb)

#If this page is executed with no error, you have successfully created a database.

"""

# import mysql.connector

# mydb = mysql.connector.connect(
#   host = "localhost",
#   user = "myusername",
#   password = "mypassword"
# )

# mycursor = mydb.cursor()

# mycursor.execute("show  databases")

# for x in mycursor:
#   print(x)

