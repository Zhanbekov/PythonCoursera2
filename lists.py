for i in [1,2,3,4,5,6]:
    print(i)
print('Blasstofff!')
###########
friends=['Argun', 'Kaharman', 'Niyaz', 'Sanzhar', 'Almas']
for friend in friends :
    print('Hello my friend:', friend)
print(friends[3])
print(range(len(friends)))
###########
loto = [1,56,34,2,3234,332,234,43]
loto[2]= 2222
print(loto)
print(len(loto))
############
print(range(4))
############
friends=['Argun', 'Kaharman', 'Niyaz', 'Sanzhar', 'Almas']
for i in range(len(friends)):
    friend = friends[i]
    print('Huppy new year:', friend)
##########
stuff = list() #creating an empty list
stuff.append('volvo') # ADDS new element
stuff.append('99')
print(stuff)
#########
some = [1,2,3,4,5,7,8,9] #should retern TRUE FALSE operators
5 in some
print(len(some)) #koli4estvo elementov in list
print(sum(some))
print(max(some))
print(min(some))
print(sum(some)/len(some))
#########
friends=['Argun', 'Kaharman', 'Niyaz', 'Sanzhar', 'Almas']
friends.sort()
print(friends)
print(friends[1])
########
numlit = list()
while True :
    inp = input('Enter a number: ')
    if inp == 'done' : break
    value = float(inp)
    numlit.append(value)

average = sum(numlit)/len(numlit)
print('Average:', average )
########
abc= 'With three words'
stuff = abc.split() #breaks a string into parts and produces a list of strings
print(stuff)
print(len(stuff))
print(stuff[0])
for w in stuff:
    print(w)
#########
line = ['stephen.maquard@uct@uct.ac.za']
words = line.split()
email = words[1]
pieces = email.split('@')
print(pieces[1])
