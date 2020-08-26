from datetime import datetime

birth_date_time = input("Enter you DOB in format dd/mm/yyyy hr:min:sec  -")
birth_date_time = datetime.strptime(birth_date_time, "%d/%m/%Y %H:%M:%S")

current_date_time = datetime.now()

# print("Current Date Time -", current_date_time)
# print("Birth Date Time -", birth_date_time)

time_delta = current_date_time - birth_date_time

days = time_delta.days

year = days // 365
days = days % 365

month = days // 30
days = days % 30

print("You have lived for  -  {0} years, {1} months, {2} days , {3}".format(year, month,
                                                                            days, str(time_delta).split(',')[1]))
