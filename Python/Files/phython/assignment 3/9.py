print("which input needs to be converted into int","\n","1. binary","\n","2. Octal","\n","3. Hex")
c=int(input("enter choice: "))
if c==1:
 b=input("enter binary no: ")
 print(f"integer of binary no {b}:{int(b,2)}")
if c==2:
 b=input("enter Octal no: ")
 print(f"integer of octal no {b}:{int(b,8)}")
if c==3:
 b=input("enter hexadecimal no: ")
 print(f"integer of hexadecimal no {b}:{int(b,16)}") 
if c!=1 & c!=2 & c!=3:
 print("invalid choice")