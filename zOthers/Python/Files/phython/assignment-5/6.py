s = "Welcome to USA. usa awesome, isn't it?"
s=s.lower()
print(s)
for idx in range(s.count("usa")):
     idx=s.rindex("usa")
     s=s[:idx]
     print(idx)
