"""
machine has N cores
tasks has requirement of X cores and W weight
problem : current load 8 cores can be sufficient for T number of tasks
when we change the configuration of the system from 8 to 16 cores
assignment of the number of cores per task should be automatic

Service 1 - 1 core
Service 2 - 2 cores

Min Wastage of cores

T = 5 # number of tasks
each task can have random weight
T1 - weight 1 * 256  # weight 1 equal to 1 core
T2 - weight 1 * 256
T3 - weight 2 * 256
T4 - weight 3 * 256
T5 - weight 3 * 256

input :
8   # N - cores

output :
[1, 1, 2, 3, 3], wastage = 6

units available = 8192
units needed = 10 * 1024 = 10240
1 core = 1024 units


Time 1 : t1, t2, t3, t4, t5 # each has 1024 units
Time 2 : -,  -,  t3, t4, t5

if units needed < units available:
    equal distribution
else
    time_array = [8 * 1024, 8 * 256]

"""




"""
string = a-zA-Z characters
min length substring if string that contains all characters from the input string atleast once

input - 
ababcdab
ababcdabe
abxabcdabe

output - 
abcd
cdabe
xabcdabe


"""

"""
min_length = 
min_substring = 
  abxabcdabex
i 0
j           11

if len(substring) < min_length:
    min_length = len(substring)
    min_substring = substring

2 indexes
i , j

{
'a': 3,
'b': 3,
'c': 1,
'd': 1, 
}

j = 4
{
'a': 1,
'b': 1,
'c': 0,
'd': 0, 
}

i = 2
{
'a': 3,
'b': 1,
'c': 0,
'd': 0, 
}

1) get all unique characters
2) store indexes of each unique character

"""

"""
current = off
thread1 - turn on    - if already on then it will burst
thread2 - turn off   - if already off then it will burst
"""

# current_state = "On"
# flag = True
# c1 = on
# c2 = off
#
# def turn_off():
#     wait(c2):
#         change_current_state(False)
#     notify(c1)
#
# def turn_on():
#     wait(c1):
#         change_current_state(True)
#     notify(c2)
#
#
# def change_current_state(new_state):
#     current_state = new_state
#     flag = not flag
#
# def execute_therad(thread):
#     if flag:
#         thread 2
#     else:
#         thread 1
#     wait()
