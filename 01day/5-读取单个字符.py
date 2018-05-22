f = open('100.txt','r')

#content = f.read(100)
#line = f.readline()

for i in f.readlines():
	print(i)

#print(line)
f.close()
