num = int(input("Value"))
sq = int(num**0.5)
if sq*sq == num:
    print("perf")
    numstr = str(num)
    firstsq = int(numstr[:2])**0.5
    lastsq = int(numstr[-2:])**0.5
    if firstsq*firstsq == int(numstr[:2]) and lastsq*lastsq == int(numstr[-2:]):
        print("BOth equal")
    else:
        print("NOt")
else:
    print('not')
