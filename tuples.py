x = ('Glenn', 'Sally', 'Joseph')
print(x[2])
y = (1, 2, 3, 4)
print(max(y))
for num in y:
    print(num)
#####
(x,y) = (9, 'Fred')
print(x)
####
d= dict()
d['cwen'] = 2
d['csev'] = 4
for (k,v) in d.items():
    print(k,v)
tups = d.items()
print(tups)
####
(0,1,2,3) < (0,1,3,4,5)#true or false also it works with Strings
#####
d = {'a':10, 'c':1, 'b':22}
t = sorted(d.items())
print(t)
for k, v in sorted(d.items()):
    print(k,v)
#####
d = {'a':10, 'c':1, 'b':22}
tmp  = list()
for k,v in d.items() : 
    tmp.append((v,k))
print(tmp)
tmp = sorted(tmp, reverse=False)
print(tmp)
########
Fhand = open('mbox-short.txt')
counts = dict() 
for line in Fhand:
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

lst = list()
for key, val in counts.item():
    newtup  = (val, key)
    lst.append(newtup)
lst = sorted(lst, reverse=True)
for val, key in lst[:10] :
    print(key, val)
