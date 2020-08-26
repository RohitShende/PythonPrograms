import pymysql
import datetime

# Open database connection
db = pymysql.connect("10.173.190.3", "vkharge", "vkharge", "nsxt_jenkins")

# prepare a cursor object using cursor() method
cursor = db.cursor()

# execute SQL query using execute() method.
cursor.execute("SELECT VERSION()")

# Fetch a single row using fetchone() method.
data = cursor.fetchone()
print("Database version : %s " % data)

cursor.execute("SELECT id, status from testcases")

data = cursor.fetchall()
# print(data)
print("Total Rows in Table - ", len(data))

count = 0
for row in data:
    if row[1] == "PASS":
        print("Type 1")
        print(row)
        query = "UPDATE testcases SET status = '{0}' WHERE id = {1};".format("PASSED", row[0])
        print(query)
        cursor.execute(query)
        print("{} rows affected".format(cursor.rowcount))
        db.commit()
        pass
        count += 1

    elif row[1] == "FAIL":
        print("Type 2")
        print(row)
        query = "UPDATE testcases SET status = '{0}' WHERE id = {1};".format("FAILED", row[0])
        print(query)
        cursor.execute(query)
        print("{} rows affected".format(cursor.rowcount))
        db.commit()
        count += 1

print("OK", count)
# disconnect from server
db.close()
