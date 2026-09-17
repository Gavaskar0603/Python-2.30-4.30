#list functions
l=["sanjay","sanjay","sadhana",24,10.9]
print(l)
l.append(90)
print("l",l)
#l.clear()
#print(l)
s=l.copy()
print("s new list",s)
print(l.count("sanjay"))
b=[2,4,5,6]
l.extend(b)
print(l)

print(l.index("sanjay"))
l.insert(2,"logesh")
print(l)
l.pop()
print(l)
l.remove("sanjay")
print(l)

l.reverse()
print(l)

e=[5,2,78,3]
e.sort()
print(e)

    
