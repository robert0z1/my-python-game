from os import system
from time import sleep

import sys
#from termcolor import colored, cprint

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
maxworldwidth = 10
worldindex = 0
ccl = [1,1]
charact = False
iswrong = False
drop = False
defcharlook = "🁢"
charlook = defcharlook
#charlook = colored(charlook, attrs=['blink'])
thingloc = [[]]
charfill = ":"
canvaswidth = 3
canvasheight = 3
whatprints = [canvas(canvaswidth, canvasheight, charfill)]
CanGoThru = []
CanGoThru.append(charfill)
gothruwalls = False
goback = False
manual = False
highlightcolor = False


gchar_x = 0
gchar_y = 0
curloc = [gchar_x, gchar_y]
prevloc = [gchar_x - 1, gchar_y - 1]

while True:
    print(prevloc, 5)
    if charact == "d":
        prevloc = [gchar_x, gchar_y]
        gchar_x = gchar_x + 1
        if gchar_x == len(whatprints[worldindex][0]):
            gchar_x = gchar_x - 1
            iswrong = True
            if canvaswidth != maxworldwidth:
                canvaswidth += 1
            if canvaswidth == maxworldwidth and gchar_x + 1 == maxworldwidth:
                gchar_x = 0
                worldindex += 1
                if worldindex + 1 > len(whatprints):
                    whatprints.append(canvas(canvaswidth, canvasheight, charfill))
                    thingloc.append([])

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



    #drop is enabled
    if charact == "P":
        if drop == False:
            drop = True
        hilightcheck = input("do you want it to be highlighted?")
        if hilightcheck == "y":
            highlightcolor = input("which color")
            #charlook = colored(input("which char: "), highlightcolor)
            charlook = input("which char: ")
        else:
            charlook = input("which char: ")
    #drop is disabled
    if charact == "p":
        if drop == True:
            drop = False
        charlook = defcharlook

    if charact == "G":
        gothruwalls = True
    if charact == "g":
        gothruwalls = False

    if charact == "can":
        gothruinput = input("which char should you be able to go through: ")
        CanGoThru.append(gothruinput)

    if charact == "man":
        manual = True

    if charact == "next world":
        worldindex += 1

    if drop == True:
        thingloc[worldindex].append([gchar_x, gchar_y, charlook, highlightcolor])

    whatprints[worldindex] = canvas(canvaswidth, canvasheight, charfill)

    for s in thingloc[worldindex]:
        whatprints[worldindex][s[1]][s[0]] = s[2]
        system("clear")
        whatprints[worldindex][gchar_y][gchar_x] = charlook
        print("")
        print("  ",gchar_x, gchar_y)
        printcan(whatprints[worldindex])
        sleeplen = .1 / len(thingloc[worldindex])
        sleep(sleeplen)
    whatprints[worldindex][gchar_y][gchar_x] = charlook


    system("clear")
    print("")
    print(" worldindex: ", worldindex)
    print("char psition: ",gchar_x, gchar_y)
    printcan(whatprints[worldindex])
    if manual == True:
        print("wasd for moving")
        print("P for placing specified char as you move")
        print("p to dissable specified char as you move")
        print("G to go through walls")
        print("g to dissable going through walls")
        print("'can' to go through specified char perminantly")
        manual = False

    if iswrong == True:
        iswrong = False
    charact = input("(type 'man' for manual)action? ")
    