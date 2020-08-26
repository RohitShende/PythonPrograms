print("Python interprets any non-zero value as True. None and 0 are interpreted as False.")

while 20:
    print("Works with int")
    break


while "string":
    print("Works with string")
    break


a = None
while a:
    print("Works with None")
else:
    print("Does not Work with None")


while 0:
    print("Works with 0")
else:
    print("Does not Work with 0")

print("\nA while loop's else part runs if no break occurs. even if condition is false always")

print("\n\n")
counter = 0
while counter < 3:
    print("Inside loop")
    counter = counter + 1
else:
    print("Inside else")
