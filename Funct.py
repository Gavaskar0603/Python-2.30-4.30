'''
name=input("Enter your name:")
def greet(name):    #parameter
    print(f"Hello {name}")
greet(name)     #Argument



names=["A","B","C","D"]
def persons(names):
    for i in names:
        if i=="B":
            continue
        else:
            print(f"Hello {i}")

persons(names)

def add():
    a=int(input("enter the range"))
    b=[]
    for i in range (0,a):
        c=input("enter the values")
        b.append(c)
    print(b)

add()
add()
'''
'''
name=input("Enter your name:")
courses= input("Enter your Course:")
def course(name, courses):
    print(f"Hello I'm {name} and I studied {courses}")
course(courses,name)



def course1(name, courses):
    print(f"Hello I'm {name} and I studied {courses}")
course(courses="Python",name="GK")



def course(name="GK", courses="Python"):
    print(f"Hello I'm {name} and I studied {courses}")
course()
course("Bharth","AI")

'''
'''
def var(*num):
    total=1
    for i in num:
        total*=i
    print(f"Total :{total}")
var(10,52,81,49)

def fact(n):
    if n>0:
        return n*fact(n-1)
    else:
        return 1
print(fact(5))
'''
'''
add=lambda a,b : a+b
print(add(45,26))


a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
even = list(filter(lambda x:x%2==0,a))
print(even)


a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
even = list(map(lambda x:x*2,a))
print(even)
'''
a=10
b=20
def add():
    
    print(a+b)
add()
print(a)
