a = int(input("Enter A value:"))
if a>10:
    print("The given number is grater than 10")

'''
#odd vs Even

if a%2==0:
    print("even")
else:
    print("Odd")

#elif
mark = int(input("Enter the mark:"))
if mark>90 and mark<=100:
    print("Grade A")
elif mark>70 and mark<=90:
    print("Grade B")
else:
    print("Fail")



person = int(input("Enter your age:"))

if person>20:
    invite = input("Enter a invite status yes / no:")
    if invite=="yes":
        print("You are allowed to this party")
    else:
        print("Get your invite")
else:
    print("You are not allowed to this party")
'''
'''
#positive number negative number:
n = int(input("Enter n value:"))
if n>0:
    print("Positive")
elif n<0:
    print("Negative")
else:
    print("Zero")


#forloop:

for i in range (1,50):
    print(i)

#multiples of three
for j in range (1,50):
    if j%3==0:
        print(j)
'''

for i in range(6,0,-1):
    print(i)

#No.of times print
a="python"
for i in range(1,6):
    print(a)

#horizontal
'''
for i in a:
    print(i,end="")
'''
# reverse a string
r=""
for i in a:
    r=i+r
print(r)


for i in range(1,5):
    for j in range(i):
        print("*",end="")
    print()

for i in range(3):
    for j in range(3):
        print("*",end="")
    print()


print("\npython"*5)

for i in range(5,0,-1):
    for j in range(i):
        print("*",end="")
    print()


for i in range(1,5):
    for j in range(1,i+1):
        print(j,end="")
    print()

for i in range(65,70):
    for j in range(65,i+1):
        print(chr(j),end="")
    print()


a=int(input("Enter a values:"))
while a<=10:
    print(a)
    a+=1

b=int(input("Enter b values:"))
while b>0:
    print(b)
    
