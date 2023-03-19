from random import randint
from time import time
print()
print()
print()
print()
print()

randintint = 0
loopamount = 5000000	
thelistamount = 100000
thelist = []
while thelistamount > 0:
	thelist.append(0)
	thelistamount -= 1


starttiming = time()
while randintint < loopamount:
	thelist[randint(0, len(thelist) - 1)] += 1
	randintint += 1
endtiming = time()


thelistindex = 0
for x in thelist:
	thelist[thelistindex] = x / loopamount
	thelist[thelistindex] = thelist[thelistindex] - 1/len(thelist)
	if thelist[thelistindex] < 0:
		thelist[thelistindex] = thelist[thelistindex] * -1
	thelist[thelistindex] = round(thelist[thelistindex], 6)
	thelistindex += 1
avrdist = 0
for x in thelist:
	avrdist += x
avrdist /= 3

print(thelist, end = "			")
print("it took:", end = " ")
print(str(round(endtiming - starttiming, 10)) + " seconds")
print("pecent distance away from " + str(round(1/len(thelist), 6)) + ": " + str(round(avrdist, 6)))