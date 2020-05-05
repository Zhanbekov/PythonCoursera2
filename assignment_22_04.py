name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts = dict()
for line in handle:
    line = line.rstrip()
    if line.startswith('From:'):continue
    if line.startswith('From'):
        fline = line.split()
        email = fline[1]
        print(fline)
        counts[email] = counts.get(email, 0) +1
print(counts)


bigcount = None
bigword = None
for word, count in counts.items(): 
    if bigcount is None or count>bigcount: 
        bigword = word
        bigcount = count
print(bigword, bigcount)

