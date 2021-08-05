import os,re
def ping(host_id,ip=[],rtt=[]):
	for host_name in host_id:
		os.system("ping -c 2 {} > /home/alethea/python/pingdoc.txt".format(host_name))
		with open(r"/home/alethea/python/pingdoc.txt") as file:
			ip.append((re.findall("(\d{1,4}\.\d{1,4}\.\d{1,4}\.\d{1,4})",file.readlines()[0])[0],host_name))
			file.seek(0)
			rtt.append(([i.split("/")[1] for i in file.readlines()[-1].split("=") if i.strip()],host_name))
	print("the fastest is",sorted(rtt,key=lambda x:x[-1])[0])
	print("the slowest is",sorted(rtt,key=lambda x:x[-1])[-1])	
#host_id=["www.google.com","www.facebook.com","www.amazon.com","www.wikipedia.com","www.instagram.com","10.10.10.2"]
ping(["www.google.com","www.facebook.com","www.amazon.com","www.wikipedia.com","www.instagram.com","10.10.10.2"])





		

