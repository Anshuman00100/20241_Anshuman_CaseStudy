import mysql.connector

mydb = mysql.connector.connect(
        host='localhost',
        user='root',
        password='akpans.27',
        database='casestudy'
)

mycursor = mydb.cursor()
mycursor.execute("CREATE TABLE user (user_id INT, user_name VARCHAR(20),phone VARCHAR(20), role VARCHAR(20), dob VARCHAR(20), created_on  VARCHAR(20), modified_on VARCHAR(20), Email VARCHAR(50))")