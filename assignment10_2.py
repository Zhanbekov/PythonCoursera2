
name = input("Enter file:")
if len(name) < 1 : name = "mbox-short.txt"
handle = open(name)
counts = dict()
for line in handle:
    line = line.rstrip()
    if line.startswith('From '):
        fline = line.split()
        lline = fline[5]
        pline = lline.split(':')
        dline = pline[0]
        counts[dline] = counts.get(dline, 0) +1

t = sorted(counts.items())
for k, v in sorted(counts.items()):
    print(k,v)

