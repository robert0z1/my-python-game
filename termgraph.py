from os import system
from time import sleep

import sys
from termcolor import colored, cprint
import readchar

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



system("cd ~/py")
maxworldwidth = 30
worldindex = 0
ccl = [1,1]
passablecharisthere = False
charact = False
iswrong = False
drop = False
defcharlook = "🁢"
charlook = defcharlook
charlook = colored(charlook, attrs=['blink'])
thingloc = [[]]
charfill = " "
canvaswidth = maxworldwidth
canvasheight = 6
whatprints = [canvas(canvaswidth, canvasheight, charfill)]
CanGoThru = []
CanGoThru.append(charfill)
gothruwalls = False
goback = False
manual = False
highlightcolor = False
worldheight = 3
howfarx = 0
for x in whatprints[0][worldheight]:
	thingloc[worldindex].append([howfarx, worldheight, "#", "green"])
	howfarx += 1
howfarx = 0
howfary = 0
for y in whatprints[0]:
	if howfary > worldheight:
		for x in whatprints[0][worldheight]:
			thingloc[worldindex].append([howfarx, howfary, "#", "green"])
			howfarx += 1
		howfarx = 0
	howfary += 1
howfary = 0

gchar_x = 0
gchar_y = 0
curloc = [gchar_x, gchar_y]
prevloc = [gchar_x - 1, gchar_y - 1]
redraw = input("do you want cool graphic visuals? (y/n) :")
gravity = True
while True:
	if charact == "d":
		prevloc = [gchar_x, gchar_y]
		gchar_x = gchar_x + 1
	#if past right edge
		if gchar_x == len(whatprints[worldindex][0]):
			gchar_x = gchar_x - 1
			iswrong = True
			if len(whatprints[worldindex]) < gchar_y + 1:
					whatprints[worldindex] = canvas(canvaswidth, gchar_y + 1, charfill)
			if canvaswidth != maxworldwidth:
				canvaswidth += 1
		#for adding new world
			if canvaswidth == maxworldwidth and gchar_x + 1 == maxworldwidth:
				gchar_x = 0
				worldindex += 1
				if worldindex + 1 > len(whatprints):
					whatprints.append(canvas(canvaswidth, canvasheight, charfill))
					thingloc.append([])
					for x in whatprints[0][worldheight]:
						thingloc[worldindex].append([howfarx, worldheight, "#", "green"])
						howfarx += 1
					howfarx = 0
					howfary = 0
					for y in whatprints[0]:
						if howfary > worldheight:
							for x in whatprints[0][worldheight]:
								thingloc[worldindex].append([howfarx, howfary, "#", "green"])
								howfarx += 1
							howfarx = 0
						howfary += 1
					howfary = 0

			for stuff in whatprints[worldindex]:
				stuff.append(charfill)
		for c in CanGoThru:
			if whatprints[worldindex][gchar_y][gchar_x] == c:
					passablecharisthere = True
			if whatprints[worldindex][gchar_y][gchar_x] != c:
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
			if worldindex != 0:
				worldindex -= 1
				gchar_x = len(whatprints[worldindex][0]) - 1
				if len(whatprints[worldindex]) < gchar_y + 1:
					whatprints[worldindex] = canvas(canvaswidth, gchar_y + 1, charfill)
			iswrong = True
		for c in CanGoThru:
			if whatprints[worldindex][gchar_y][gchar_x] == c:
				passablecharisthere = True			
			if whatprints[worldindex][gchar_y][gchar_x] != c:
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
		if gravity == True:
			gchar_y = gchar_y - 2
		else:
			gchar_y = gchar_y - 1
		if gchar_y == -1:
			gchar_y = gchar_y + 1
			iswrong = True
		for c in CanGoThru:
			if whatprints[worldindex][gchar_y][gchar_x] == c:
				passablecharisthere = True			
			if whatprints[worldindex][gchar_y][gchar_x] != c:
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
		if gchar_y == len(whatprints[worldindex]):
			gchar_y = gchar_y - 1
			iswrong = True
			canvasheight += 1
			for x in whatprints[0][worldheight]:
				thingloc[worldindex].append([howfarx, gchar_y + 1, "#", "green"])
				howfarx += 1
			howfarx = 0
		for c in CanGoThru:
			if whatprints[worldindex][gchar_y][gchar_x] == c:
					passablecharisthere = True			
			if whatprints[worldindex][gchar_y][gchar_x] != c:
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

	if gravity == True:
		gchar_y += 1
		for c in CanGoThru:
			if whatprints[worldindex][gchar_y][gchar_x] == c:
				pass		
			else:
				gchar_y -= 1


	#drop is enabled
	if charact == "P":
		gravity = False
		if drop == False:
			drop = True
		hilightcheck = input("do you want it to be highlighted?")
		if hilightcheck == "y":
			highlightcolor = input("which color (grey, red, green, yellow, blue, magenta, cyan, white)")
			charlook = colored(input("which char: "), highlightcolor)
		else:
			charlook = input("which char: ")
	#drop is disabled
	if charact == "p":
		if drop == True:
			drop = False
		charlook = colored(defcharlook, attrs=['blink'])

	if charact == "T":
		gothruwalls = True
		gravity = False
	if charact == "t":
		gothruwalls = False
		gravity = True

	if charact == "c":
		gothruinput = input("which char should you be able to go through: ")
		CanGoThru.append(gothruinput)

	if charact == "m":
		manual = True
	if charact == "next world":
		worldindex += 1

	if drop == True:
		if hilightcheck == "y":
			thingloc[worldindex].append([gchar_x, gchar_y, charlook, highlightcolor])
		else:
			thingloc[worldindex].append([gchar_x, gchar_y, charlook])

	whatprints[worldindex] = canvas(canvaswidth, canvasheight, charfill)
#places stuff onto the world
	for s in thingloc[worldindex]:
		if len(s) == 4:
			whatprints[worldindex][s[1]][s[0]] = colored(s[2], s[3])
		if len(s) == 3:
			whatprints[worldindex][s[1]][s[0]] = s[2]
		whatprints[worldindex][gchar_y][gchar_x] = charlook
		if redraw == "y":
			system("clear")
			print("")
			print(" worldindex: ", worldindex)
			print("char psition: ",gchar_x, gchar_y)
			printcan(whatprints[worldindex])
			sleeplen = .1 / len(thingloc[worldindex])
	whatprints[worldindex][gchar_y][gchar_x] = colored(charlook, attrs=['blink'])


	system("clear")
	print("")
	print(" worldindex: ", worldindex)
	print("char position: ",gchar_x, gchar_y)
	printcan(whatprints[worldindex])
	if manual == True:
		print("wasd for moving")
		print("go to the bottom of the map to make it bigger and the right most side to explore more of the map")
		print("P for placing specified char with specified color as you move")
		print("p to dissable specified char as you move")
		print("G to go through walls")
		print("g to dissable going through walls")
		print("'can' to go through specified char perminantly")
		manual = False

	if iswrong == True:
		iswrong = False
	charact = print("(type 'man' for manual)action? ")
	charact = readchar.readchar()
	

















