import time

hexy.neck.set(0)

time.sleep(0.5)
hexy.LF.knee(-20)
time.sleep(0.5)
hexy.LF.knee(-40)
time.sleep(0.5)
hexy.LF.knee(-60)

time.sleep(1.5)

hexy.LF.ankle(60)
time.sleep(0.5)
hexy.LF.ankle(40)
time.sleep(0.5)
hexy.LF.ankle(20)
time.sleep(0.5)
hexy.LF.ankle(0)
time.sleep(0.5)
hexy.LF.ankle(-20)
time.sleep(0.5)
hexy.LF.ankle(-40)
time.sleep(0.5)
hexy.LF.ankle(-60)

time.sleep(1.5)

hexy.LF.hip(-45)
time.sleep(0.2)
hexy.LF.hip(-30)
time.sleep(0.2)
hexy.LF.hip(-15)

time.sleep(0.2)
hexy.LF.hip(0)
time.sleep(0.2)
hexy.LF.hip(15)
time.sleep(0.2)
hexy.LF.hip(30)
time.sleep(0.2)
hexy.LF.hip(45)

time.sleep(1.0)

hexy.LF.hip(0)
hexy.LF.ankle(0)
hexy.LF.knee(0)

for servo in hexy.con.servos:
    hexy.con.servos[servo].setPos(deg=0)

#kill all servos
for servo in hexy.con.servos:
    hexy.con.servos[servo].kill()





