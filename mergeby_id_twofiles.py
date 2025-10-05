from collections import defaultdict
import sys

#usage cat f1|python mergeby_id_twofiles.py f2 > f3 
f_open=sys.argv[1]
f=open(f_open)
d=defaultdict(lambda:"NA")


for i in f:
    k,v=i.strip().split("\t")
    d[k]=v
f.close()

for j in sys.stdin:
    match=j.strip().split("\t")[0]
    print(j.strip()+"\t"+d[match])



