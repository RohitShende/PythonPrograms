marks = int(input("Enter marks from 0 to 100 :"))

if marks > 100 or marks < 0:
    print("The marks entered are invalid")
else:
    if marks < 35:
        print("FAILED ! Study hard next time")
    elif marks < 50:
        print("you have PASSED in Second Class")
    elif marks < 75:
        print("you have PASSED in First Class")
    elif marks < 90:
        print("you have PASSED with Distinction")
    else:
        print("You are a MERIT student")
