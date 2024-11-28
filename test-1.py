import psycopg2 

# print('r')
connection = psycopg2.connect(database="dbtest1", user="postgres", password="123", host="localhost", port=5432) #,  options="-c client_encoding=UTF8")

cursor = connection.cursor()

cursor.execute('''SELECT "Code", "Age", "Name" 
               FROM cat;''')
 
# Fetch all rows from database
record = cursor.fetchall()

print("Data from Database: ", record)