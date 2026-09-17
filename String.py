'''a="MONISH"
print(a.capitalize())#1st -capital
b="Krithick"
print(b.lower())
print(b.upper())
print(b.swapcase())
print(b.center(10,'*'))
print(b.count('i'))
print(b.casefold())#lowercase
print(a.encode('utf-16'))
#ENDSWITH
print(a.endswith('H'))
print(a.endswith('e'))
#STARTSWITH
print(b.startswith('K'))
print(b.startswith('k'))
#Expandtab
c="HelloWorld"
print(c.expandtabs())

#find-indexing position
print(c.find('r'))
print(c.find('z'))
#index
print(c.index('e'))
print(c.index('z'))
#Checking
c="     Muni123      "
print(c.isalnum())#alpha+num
print(c.isdigit())#num only
print(c.isascii())
print(c.istitle())
#title
d="monish is a good boy"
print(d.title())
#
print(c.ljust(10,'*'))
print(c.rjust(10,'*'))
print(c.zfill(10))
#Removes extra spacing
print(c.strip())
print(c.lstrip())
print(c.rstrip())'''

#format
'''a="Hiii"
print(f"{a},This is Python")

print(max(20,30,40))
print(min(20,30,40))
print(len("Hello "))

#Lambda
c=lambda a,b:a**b
print(c(2,5))

c=lambda a,b:a*b
print(c(2,5))

c=lambda a,b,d:a+b*d
print(c(2,5,3))

#Maximum
c=lambda a,b:a if a>b else b
print(c(2,5))
#Minimum
c=lambda a,b:a if a<b else b
print(c(2,5))

#Even or odd
c=lambda a:"Even" if a%2==0 else "Odd"
print(c(2))
print(c(25))

c=lambda a:len(a)
print(c("Python"))

#filter+mapping
a=[1,2,3,4,5,6]
b=list(map(lambda x:x*x,filter(lambda x:x%2==0,a)))
print(b)
'''





















