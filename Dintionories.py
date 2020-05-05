purse = dict()
purse['money'] = 12
purse['candy'] = 3
purse['tissues'] = 75
print(purse)
print(purse['candy'])
purse['candy'] = purse['candy'] + 2
print(purse['candy'])
##########
#counts = dict()
#names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
#for name in names:
#    if name not in names:
#       counts[name]=1
#    else:
#        counts[name] = counts[name] + 1
#print(counts)
##########
#counts = dict()
#names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
#if name in counts:
#    x = counts[name]
#else:
#    x=0
#x = counts.get(name, 0)
#print(x)
#######
counts = dict()
names = ['csev', 'cwen', 'csev', 'zqian', 'cwen']
for name in names : 
    counts[name] = counts.get(name, 0) + 1
print(counts)
#######
counts = dict()
print('Enter a line of text:')
line = input('')
words = line.split()
print('words:', words)
print('Counting...')
for word in words:
    counts[word] = counts.get(word,0)+1
print('counts', counts)
######
counts = {'chuck' : 1 , 'Fred' : 42 , 'Jan' : 100}
for key in counts:
    print(key, counts[key])
######
counts = {'chuck' : 1 , 'Fred' : 42 , 'Jan' : 100}
print(list(counts))   #Превращает в лист
print(counts.keys())
print(counts.values())
print(counts.items())   #all this a list
#####
jjj = {'chuck' : 1, 'Fred': 42, 'Jan': 100}
for aaa,bbb in jjj.items():
    print(aaa, bbb)

#####
name = input('Enter file:')
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)

counts = dict()
for line in handle:  #reads each line
    words = line.split() #split lines to separate words
    for word in words: # reads each word
        counts[word] = counts.get(word,0) +1 #Считает количество повторений и записывает их

bigcount = None
bigword = None
for word, count in counts.items(): #Reads word and count in the dictionary
    if bigcount is None or count>bigcount: #Сравнение
        bigword = word
        bigcount = count
print(bigword, bigcount)