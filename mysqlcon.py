import mysql.connector

def mydefsql(sorgu):
    mydb = mysql.connector.connect(
    host="localhost",  #CHANGE THIS
    user="root",       #CHANGE THIS 
    passwd="1234",     #CHANGE THIS
    database = "world" #CHANGE THIS
)

    mycursor = mydb.cursor()
    mycursor.execute(sorgu)
    output=[]
    for i in mycursor:
        output.append(i)
    return output[0:5]

