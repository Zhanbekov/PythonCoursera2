xfile = open('mbox.txt')
for cheese in xfile: #cheese будет читать каждую строку в в файйле
    print(cheese)

######
fhand = open('mbox.txt')
count = 0
for line in fhand:
    count = count + 1
print('Line Count:', count)

#####
fhand = open('mbox.txt')
inp= fhand.read()
print(len(inp)) #считает количество букв с помощью read()
print(inp[:44])

######
fhand = open('mbox.txt')
for line in fhand:
    line = line.rstrip()
    if line.startswith('From:') :
        print(line)

######

fname = input("Enter file name: ")
try:
    fh = open(fname)
except:
    print('Error, enter another file name')
    quit()
for i in fh:
    i=i.rstrip()
    print(i .upper())

