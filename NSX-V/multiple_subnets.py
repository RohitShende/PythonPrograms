s = '.0.0.1/32</subnet>'
s1 = '.0.0.1/32'

for i in range(1, 201):
    print("<subnet>"+str(10+i)+s)

for i in range(1, 201):
    print(str(10+i)+s1, end=',')
