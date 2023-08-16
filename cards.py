def SpicificCardAttrabuteListMaker():
	llist = []
	ii = 0
	while ii < 12:

		i = 0
		while i < 4:
			values = ["w", "e", "r", "t"]
			llist.append(values[i])
			i+=1
		i = 0
		ii+=1
	return llist

#checks to see if each row in the "2d array" has the same amount of things in it
def DbCheck(llist):
	i = 1
	while i <= len(llist) -1:
		if len(llist[0]) != len(llist[i]):
			return False
		i+=1
	return True 



GlobalColumn = 0
Cards = ["A", "A", "2", "2", "2", "2", "3", "3", "3", "3", "4", "4", "4", "4", "5", "5", "5", "5", "6", "6", "6", "6", "7", "7", "7", "7", "8", "8", "8", "8", "9", "9", "9", "9", "10", "10", "10", "10", "J", "J", "J", "J", "Q", "Q", "Q", "Q", "K", "K", "K", "K", "A", "A"]
Suits = ['w', 'e', 'w', 'e', 'r', 't', 'w', 'e', 'r', 't', 'w', 'e', 'r', 't', 'w', 'e', 'r', 't', 'w', 'e', 'r', 't', 'w', 'e', 'r', 't', 'w', 'e', 'r', 't', 'w', 'e', 'r', 't', 'w', 'e', 'r', 't', 'w', 'e', 'r', 't', 'w', 'e', 'r', 't', 'w', 'e', 'r', 't', 'r', 't']
Value1= ['1', '1', '2', '2', '2', '2', '3', '3', '3', '3', '4', '4', '4', '4', '5', '5', '5', '5', '6', '6', '6', '6', '7', '7', '7', '7', '8', '8', '8', '8', '9', '9', '9', '9', '10', '10', '10', '10', '10', '10', '10', '10', '10', '10', '10', '10', '10', '10', '10', '10', '1', '1']
Value2= ['11', '11', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '11', '11']
print(DbCheck([Cards, Suits, Value1, Value2]))


#i = 0
#while True:
#	print(Cards[i])
#	Value1.append(input())
#	print()
#	print(Value1)
#	i+=1

