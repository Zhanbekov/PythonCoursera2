fname = input("Enter file name: ")
count = 0
if len(fname) < 1 : fname = "mbox-short.txt"
fn = open(fname)
for line in fn:
    line = line.rstrip()
    if line.startswith('From:'):continue
    if line.startswith('From'):
        count+=1
        spl = line.split()
        print(spl[1])
    

print("There were", count, "lines in the file with From as the first word")

