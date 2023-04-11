import pymysql

# Database connection settings
connection = pymysql.connect(
    host="127.0.0.1",
    user="root",
    password="some_pass",
    database="test",
    port=3306
)

# Query the 'people' table
with connection.cursor() as cursor:
    sql = "SELECT * FROM people"
    cursor.execute(sql)
    result = cursor.fetchall()

connection.close()

# Print the table headers
print("ID\tName\t\tSurname")

# Print the table content
for row in result:
    print(row)

