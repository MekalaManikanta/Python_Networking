from collections import defaultdict
with open(r"/home/alethea/python/README.txt") as file:
   d=defaultdict(int)
   for line in file:
      if line.strip():
         words=line.split()
         for word in words:
            d[word]+=1
   res=sorted(d.items(),key=lambda x:x[-1])
   with open(r"/home/alethea/python/output.txt", "a") as output:
	for i in res:
		data=str(i[0]) + "\t" + str(i[1])
		output.write(data + "\n")			
			
