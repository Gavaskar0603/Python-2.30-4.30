# Strings
a='''the internship is all about doing a  daily task
and also we work on  a real time project'''
print(a)
b=a.replace('a','t')
print(b)

c="      iejrv  rie   "
print(c)
v=c.strip()
print(v)


#core datatypes/data structures

#list-->mutable,allows duplicates,ordered


l=["dhanushiya","jananishree"]
print(l,type(l))
l.append("manju")
print(l)
l.append("manju")
print(l)
l.remove("dhanushiya")
print(l)

#tuple-->IMMUTABLE,allows duplictaes,ordered
t=("dhanushiya","jananishree","jananishree")
print(t,type(t))
#t.append("elavarasi")
print(t)

#set -->mutable,not allow duplicates,unordered
s={"dhanushiya","jananishree","jananishree"}
print(s,type(s))
s.add("jananishree")
print(s)
s.add("jananishree")
print(s)

#dictionary-->mutable,values duplictes allowed,key not allow duplicates,ordered
d={1:"dhanushiya",2:"jananishree",3:"jananishree"}
print(d,type(d))
d.update({1:"priyanka"})
print(d)



















