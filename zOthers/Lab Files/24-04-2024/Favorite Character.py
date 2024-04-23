
input_text = " Yashh kumar 3345"

p1_text = input_text.replace(" ", "")

p2_text = {}

for i in p1_text:
	if i in p2_text:
		p2_text[i] += 1
	else:
		p2_text[i] = 1

print(str(p2_text))

max_text = max(p2_text.values())

#print(max_text)

l=list(p2_text.values())

print(l.count(max(l)))
