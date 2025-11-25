from collections import defaultdict
import sys
d=defaultdict(lambda:False)
f_name=sys.argv[1]
f1=open(f_name)
for i in f1:
    d[i.strip()]=True
f1.close()

for j in sys.stdin:
    m=j.strip().split("\t")[1]
    if d[m]==True:
        print(j,end="")
    else:
        continue

