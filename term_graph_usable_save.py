from os import system
from time import sleep

import sys
from termcolor import colored, cprint

system("python3 ~/py/termgraph.p")
ccl = [1,1]
charact = False
iswrong = False
drop = False
charlook = "♿︎"
charlook = colored(charlook, 'red', attrs=[ 'reverse', 'blink'])
thingloc = []
charfill = "▵▵"
CanGoThru = []
CanGoThru.append(charfill)
gothruwalls = False
goback = False
manual = False

def printcan(canvas):
	for y in canvas:
		for x in y:
			print(x, end = "")
		print("")


def canvas(width, height, charfill):
    canvas = []
    for y in range(height):
        row = []
        for x in range(width):
            row.append(charfill)
        canvas.append(row)
    return canvas


whatprints = canvas(10, 10, charfill)
gchar_x = 4
gchar_y = 4
curloc = [gchar_x, gchar_y]
prevloc = [gchar_x - 1, gchar_y - 1]

while True:
	print(prevloc, 5)
	if charact == "d":
		prevloc = [gchar_x, gchar_y]
		gchar_x = gchar_x + 1
		if gchar_x == len(whatprints[0]):
			gchar_x = gchar_x - 1
			iswrong = True
		for c in CanGoThru:
			if whatprints[gchar_y][gchar_x] == c:
					passablecharisthere = True
			if whatprints[gchar_y][gchar_x] != c:
				if gothruwalls == False:
					if drop == False:
						if iswrong == False:
							goback = True
		if passablecharisthere == True:
			goback = False
			passablecharisthere = False
		if goback == True:
			gchar_x = gchar_x - 1
			goback = False




	if charact == "a":
		prevloc = [gchar_x, gchar_y]
		gchar_x = gchar_x - 1
		if gchar_x == -1:
			gchar_x = gchar_x + 1
			iswrong = True
		for c in CanGoThru:
			if whatprints[gchar_y][gchar_x] == c:
				passablecharisthere = True			
			if whatprints[gchar_y][gchar_x] != c:
				if gothruwalls == False:
					if drop == False:
						if iswrong == False:
							goback = True
		if passablecharisthere == True:
			goback = False
			passablecharisthere = False
		if goback == True:
			gchar_x = gchar_x + 1
			goback = False



	if charact == "w":
		prevloc = [gchar_x, gchar_y]
		gchar_y = gchar_y - 1
		if gchar_y == -1:
			gchar_y = gchar_y + 1
			iswrong = True
		for c in CanGoThru:
			if whatprints[gchar_y][gchar_x] == c:
				passablecharisthere = True			
			if whatprints[gchar_y][gchar_x] != c:
				if gothruwalls == False:
					if drop == False:
						if iswrong == False:
							goback = True
		if passablecharisthere == True:
			goback = False
			passablecharisthere = False
		if goback == True:
			gchar_y = gchar_y + 1
			goback = False




	if charact == "s":
		prevloc = [gchar_x, gchar_y]
		gchar_y = gchar_y + 1
		if gchar_y == len(whatprints):
			gchar_y = gchar_y - 1
			iswrong = True
		for c in CanGoThru:
			if whatprints[gchar_y][gchar_x] == c:
					passablecharisthere = True			
			if whatprints[gchar_y][gchar_x] != c:
				if gothruwalls == False:
					if drop == False:
						if iswrong == False:
							goback = True
		if passablecharisthere == True:
			goback = False
			passablecharisthere = False
		if goback == True:
			gchar_y = gchar_y - 1
			goback = False



	#drop is enabled
	if charact == "P":
		if drop == False:
			drop = True
		charlook = charlook = colored(input("which char: "), 'red', attrs=[ 'reverse', 'blink'])
	#drop is disabled
	if charact == "p":
		if drop == True:
			drop = False
		charlook = "Ω"

	if charact == "G":
		gothruwalls = True
	if charact == "g":
		gothruwalls = False

	if charact == "can":
		gothruinput = input("which char should you be able to go through: ")
		CanGoThru.append(gothruinput)

	if charact == "man":
		manual = True

	if drop == True:
		thingloc.append([gchar_x, gchar_y, charlook])

	whatprints = canvas(10, 10, charfill)


	for s in thingloc:
		whatprints[s[1]][s[0]] = s[2]
		printcan(whatprints)
	
	whatprints[gchar_y][gchar_x] = charlook

	system("clear")
	print("")
	print(charlook)
	print("  ",gchar_x, gchar_y)
	printcan(whatprints)
	if manual == True:
		print("wasd for moving")
		print("P for placing specified char as you move")
		print("p to dissable specified char as you move")
		print("G to go through walls")
		print("g to dissable going through walls")
		print("'can' to go through specified char perminantly")
		manual = False

	if iswrong == True:
		print("can't do that.")
		iswrong = False
	charact = input("(type 'man' for manual)action? ")
	

















