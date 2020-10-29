import re

invalid_mobile_number_count = 0
while True:
    s = input()
    if s == 'Q' or s == 'q':
        break
    pattern = '^\d{10}$'
    if not re.match(pattern, s):
        invalid_mobile_number_count += 1
print(invalid_mobile_number_count)
