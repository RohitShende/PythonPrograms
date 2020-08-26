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

cursor.execute("SELECT id, duration from suites")

data = cursor.fetchall()
# print(data)
print("Total Rows in Table - ", len(data))
date_format = '%m/%d/%y %H:%M:%S'

count = 0
for row in data:
    if "hours" in row[1]:
        print("Type 1")
        # print(row)
        # x = row[1].split(' ')
        # new_duration = x[0] + "h " + x[2] + "m " + x[4] + "s"
        # print(new_duration)
        # query = "UPDATE suites SET duration = '{0}' WHERE id = {1};".format(new_duration, row[0])
        # print(query)
        # cursor.execute(query)
        # print("{} rows affected".format(cursor.rowcount))
        # db.commit()
        pass
    elif ":" in row[1]:
        print("Type 2")
        print(row)
        x = row[1].split('-')
        d1 = datetime.datetime.strptime(x[0].strip(), date_format)
        d2 = datetime.datetime.strptime(x[1].strip(), date_format)
        # print(d1, d2)
        diff = d2 - d1
        seconds = diff.seconds
        hours = seconds // 3600
        seconds = seconds % 3600
        mins = seconds // 60
        seconds = seconds % 60
        new_duration = '{0}h {1}m {2}s'.format(hours, mins, seconds)
        print(new_duration)
        query = "UPDATE suites SET duration = '{0}' WHERE id = {1};".format(new_duration, row[0])
        print(query)
        cursor.execute(query)
        print("{} rows affected".format(cursor.rowcount))
        db.commit()
        pass
    else:
        x = row[1].split(' ')
        if len(x) == 6:
            print("Type 3")
            # print(row)
            # new_duration = x[0]+"h "+x[2]+"m "+x[4]+"s"
            # print(new_duration)
            # query = "UPDATE suites SET duration = '{0}' WHERE id = {1};".format(new_duration, row[0])
            # print(query)
            # cursor.execute(query)
            # print("{} rows affected".format(cursor.rowcount))
            # db.commit()
        else:
            print("Type OK")
            count += 1
            # print(row)

print("OK", count)
# disconnect from server
db.close()
