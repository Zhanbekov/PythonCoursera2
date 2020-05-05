import re

hand = open('mbox-short.txt')
for line in hand:
    line = line.rstrip()
    if re.search('From:', line) :
        print(line)
#####
hand = open('mbox-short.txt')
for line in hand:
   line = line.rstrip()
    if re.search('^From:', line) :#^ - этот знак означчает, что F должна начинатся с новой строки, только тогда она выведется
        print(line)
############
x = 'My two favorite numbers are 19 and 42 '
y = re.findall('[0-9]+',x)
print(y)
############
x = 'From stephen.maquard@uct.ac.za Sat Jan 5 dfd 88989 665'
y = re.findall('\S+@\S+',x)
print(y)
OUTPUT: ['stephen.maquard@uct.ac.za']

y = re.findall('^From (\S+@\S+)',x) #Здесь учитывается то что адрес должен начинаться с From
print(y)
OUTPUT: ['stephen.maquard@uct.ac.za']
########
lin = 'From stephen.maquard@uct.ac.za Sat Jan 5 dfd 88989 665'
y = re.findall('@([^ ]*)', lin)
print(y)