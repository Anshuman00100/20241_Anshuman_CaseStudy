import mysql.connector

mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='akpans.27',
        database='case'
)


mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE task (user_id INTEGER(10), user_name VARCHAR(20), phone INTEGER(15), role VARCHAR(20), dob VARCHAR(20), created_on VARCHAR(20), modified_on VARCHAR(20))")
