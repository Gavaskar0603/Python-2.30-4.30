#core data  list        tuple        set                dict
# brac       []         ()            {}                 {}
# order  order(index)  order(index) unorder(noindex)
#mutable    mu          unmu         mu
#empty data  []         ()          set()                {}
#duplicate  al          al          not al
#oneelement t=[1]    t=(1,)        t={1}                 t={"name":"keerthi"}


#list buildin function
'''a=[1,2,3,4,5,6,7]
print(a)
a.append(90)
print(a)
print(a.copy())
b=a.copy()
print(b)
add=0
for i in b:
    add=add+i
print(add)
print(b)
n=0
for j in b:
    if(j%5==0):
        n=n+j
        print(n)
a=[1,2,3,1,4,5,6,7,1]
print(a.count(11))
print(b.extend(a))#add two list
print(b)
print(a.index(3))#position
print(a.insert(3,78))#index position add
print(a)
print(a.pop())#last element delete
print(a.pop(3))#index elemnt delete
print(a)
print(a.remove(7))#element delete
print(a)
a=[23,45,2,67,1,90,5]
print(a.sort())
print(a)
print(a.reverse())
print(a)'''
a="kasivishwanathan"
print(a)
'''t=[]
for i in a:
    t.append(i)
print(t.sort())
print(t)

a="hello"
b=""
for i in a:
    if i not  in b:
        b=b+i
        print(b)
        
a=[1,2,3,4,1,2,6,7,7,3,6]
b=[]
for i in a:
    if i not  in b:
        b.append(i)
        print(b)

t=[1]
print(t)
print(type(t))
t=(1,)
print(t)
print(type(t))
t={1}
print(t)
print(type(t))
t={"name":"keerthi"}
print(t)
print(type(t))'''

a=(1,2,3,4,2,3,4,"hello",34.34)
print(a)
print(a.count(2))
print(a.index("hello"))







