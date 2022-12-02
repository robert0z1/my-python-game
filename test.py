#changing vars from inside function

def functionz(mainValue, gravityVar, var2):
    theReturnList = []
    mainValue = int(mainValue) + 1
    if mainValue == 2:
        gravityVar = False
    theReturnList.append(mainValue)
    theReturnList.append(gravityVar)
    theReturnList.append(var2)
    return theReturnList

mainValue = "1"
gravityVar = True
var2 = "7"

funck = functionz(mainValue, gravityVar, var2)


#change the vars
forLoopCount = 0
for vars in funck:
    if forLoopCount == 0:
        mainValue = vars
    if forLoopCount == 1:
        gravityVar = vars
    if forLoopCount == 2:
        var2 = vars
    forLoopCount += 1
forLoopCount = 0

print(funck)


