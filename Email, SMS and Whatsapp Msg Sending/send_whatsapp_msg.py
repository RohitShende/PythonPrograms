import pywhatkit as whatsapp
import datetime

curr_time = datetime.datetime.now()
print(curr_time.hour, curr_time.minute)
minutes = datetime.timedelta(minutes=1)
future_time = curr_time + minutes
print(future_time.hour, future_time.minute)
whatsapp.sendwhatmsg("+918983306076", "Hi, from pywhatkit", future_time.hour, future_time.minute, wait_time=10,
                     print_waitTime=True)
