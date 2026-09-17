'''
a= "apple",25
print(a)
print(type(a))
'''
'''
#List

a=[10,20,30,40,50,60]

print(type(a))
print(a[3])     #Return Value
print(a.index(40))      #Return Index Position

a.append(70)
print(a)

a.extend([80,90,100])
print(a)

a.insert(20,25)
print(a)

print(a.index(25))


a.extend([10,90,10])
print(a)

print(a.count(10))

a.pop()     #Last Element
print(a)

a.pop(7)    #Particular Element
print(a)

a.remove(90)
print(a)

a.reverse()
print(a)

a.sort()
print(a)
print(a[::-1])

print(len(a))

b=a.copy()
print(b)

b.clear()
print(b)

#Tuple
c=(10,20,30,40,50)
print(c.index(30))
'''
#Set

a={2,4,9,6,1,3,7,8,9,10,6,9}
print(a)
b={5,7,8,10}
print(a.union(b))
print(b.intersection(a))

print(b.symmetric_difference(a))

a.add(90)
print(a)

a.update({20,30,40})
print(a)
'''
a={1,2,3,4}
b={3,4,5,6,7}
print(a.difference(b))
'''
'''
a.discard(90)
print(a)

a.pop()
print(a)


a={1,2,3,4,5}
b={3,4,5}
print(a.isdisjoint(b))

print(b.issuperset(a))
print(b.issubset(a))

print(a.symmetric_difference(b))
print(a)

a.symmetric_difference_update(b)
print(a)
'''
d={"Name":"SivaKrishnan",
   "Course":"AI Developer"}
print(d)

print(d.keys())
print(d.values())
print(d.get("Age","Key not available"))

print(d.items())


d1={"Age":20,
    "Gender":"Male"}
d.update(d1)
print(d)

d2={"Name":["Sridhar","Prabhakaran","Gokul"],
    "Course":["Python","AI"]}
print(d2)


