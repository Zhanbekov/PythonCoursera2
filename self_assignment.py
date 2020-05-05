
fname = input("Enter file name: ")
fh = open(fname)
count = 0
thesu = 0
for line in fh:
    line = line.rstrip()
    if line.startswith("X-DSPAM-Confidence:") :
        count = count + 1
        data = line.find(' ')
        host = line[data+1: data + 7]
        host = float(host)
        thesu = thesu+host
        result = thesu/count
print('Average spam confidence:', result)

