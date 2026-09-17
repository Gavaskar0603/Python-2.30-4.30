#n=int(input("Enter the number:"))
'''
for i in range(n,0,-1):
    print(i)


for i in range(1,10):
    if i==5:
        break
    print(i)


'''
'''
while n>0:
    print(n)
    n-=1
'''
'''
while n<=10:
    print(n)
    n+=1
'''
'''
a=121
b=0
t=a

while t>0:
    d=t%10
    b=(b*10)+d
    t=t//10
print(b)
'''
'''
for i in range(1,10):
    if i==6:
        break
    else:
        print(i)
'''
'''
for i in range(1,10):
    if i==6:
        continue
    else:
        print(i)
'''
'''
a="Student"
print(a.capitalize())
print(a.isupper())
print(a.islower())
print(a.isalpha())
print(a.isdigit())
print(a.isalnum())
print(len(a))
print(a.count("t"))
print(a.index("e"))
print(a.split("t"))
print(a.strip())
print(a.rstrip())
print(a.isascii())
print(a.center(10,"*"))
print(a.replace("S","C"))

print(a[5])
print(a[1:5])
print(a[::-1])
print(a[:-1])


l=[1,2,3,4,5]
print(type(l))

print(l[4])
l.append(8)
print(l)
l.extend([6,7,8,9,10])
print(l)
print(l.count(5))
print(l.index(5))
l.insert(10,11)
print(l)
print(l.index(11))
l.pop()
print(l)
l.remove(8)
print(l)
import pywhatkit as pk
#print(pk.sendwhatmsg("+918056374412","Hiii",12,43))
#print(pk.sendwhatmsg_instantly("+918056374412","Hiii"))
#print(pk.playonyt("Ben10"))
#print(pk.search("Ben10"))
print(pk.info("London",lines=10))'''


#pandas
import pandas as pd
a=pd.Series([1,3,4,5,6,7])
print(a)

















