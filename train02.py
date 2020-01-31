import math

deg, min, sec = 32, 13, 49

fm = sec/60
fd = (min + fm)/60
ang = deg + fd

rad = 180/math.pi
arad = ang / rad
arad = ang * math.pi/180
print(deg,min,sec,"=",arad)


angle = 32
angleToRad = angle * (math.pi / 180)
rad = 1.8375
radToAngle = rad * (180 / math.pi)

def convertToD_H_M_S():
    if angle:
        minuteAngle = angle * 60
        minute = minuteAngle
        minutes = minute // 1
        secondes = minute % 60
 
        print(angle,"degret(s) is equal to",angleToRad,"rad(s) and",int(minutes),"minute(s)",int(secondes),"seconde(s)")

    if rad:
        minuteRad = rad * (60 * 180) / math.pi
        minute = minuteRad
        minutes = minute // 1
        secondes = minute % 60
 
        print(rad,"rad(s) is equal to",int(radToAngle),"degret(s) and",int(minutes),"minute(s)",int(secondes),"seconde(s)")

convertToD_H_M_S()