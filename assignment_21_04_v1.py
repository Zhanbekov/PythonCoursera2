file = input('Enter a file name:')
fn = open(file)
nlist = list()
seen = set()
for line in fn:
    line = line.rstrip()
    spl = line.split()
    for list2 in spl:
        if list2 not in seen:
            seen.add(list2)
            nlist.append(list2)
    nlist.sort()
print(nlist)