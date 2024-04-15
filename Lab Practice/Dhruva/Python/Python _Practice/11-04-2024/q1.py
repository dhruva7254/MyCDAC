print(type(0))
print(type(0.0))
print(type('A'))
print(type(print))
print(type(3+3j))
print(type(True))

print(isinstance(10,int))
print(isinstance(10,float))
print(isinstance(1,bool))
print(isinstance(0,bool))
print(isinstance(78.8,int))
print(isinstance(78.8,float))
print(isinstance(78.8,complex))
print(isinstance(True,bool))

rol=int(input("Enter Roll No.: "))
permar=float(input("Enter % Marks: "))
comnum=complex(input("Enter Complex Num: "))
namstu=str(input("Enter Name of Student: "))
print(rol)
print(permar)
print(comnum)
print(namstu)

a=int(input("Enter integer value: "))
b=bin(a)  #0b10111
c=oct(a)  #0o27
d=hex(a)  #0x17
print(b)
print(c)
print(d)

e=input("Enter binary string: ")
f=int(e,2)
print(f)

g=input("Enter octal string: ")
h=int(g,8)
print(h)

k=input("Enter Hexadecimal string: ")
l=int(k,16)
print(l)

numa=int(input("Enter a num: "))
numb=bin(numa)
print(numb)
print(abs(numb))

