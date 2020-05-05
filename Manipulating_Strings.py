greet = 'Hello World'
zap = greet.lower()
print(zap)

#####

print('hi there' .lower())

###

fruit = 'banana'
pos = fruit.find('na')
print(pos)

#####

greet = 'Hello Bob'
nstr = greet.replace('Bob', 'Jane')
print(nstr)

nstr = greet.replace('o', 'X')
print(nstr)

######

data = 'from stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
atpos = data.find('@')
print(atpos)

sppos = data.find(' ', atpos)
print(sppos)

host = data[atpos+1: sppos]
print(host)
