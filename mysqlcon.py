import mysql.connector

def mydefsql(sorgu):
    mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="1234",
    database = "world"
)

    mycursor = mydb.cursor()
    mycursor.execute(sorgu)
    output=[]
    for i in mycursor:
        output.append(i)
    return output[0:5]

