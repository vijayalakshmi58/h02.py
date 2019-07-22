# h02.py
c=input()
d=input()
d=d.split()
d.sort(reverse = True)
e=""
for i in d:
	e+=i
print(int(e))
