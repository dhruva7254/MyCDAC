t={1,2,3,4}
for idx in range(len(t)):
 i=int(input("item to be removed or 0 to quit: "))
 if i!="q":
  t.discard(i)
 if i==0:
  break
print(t)