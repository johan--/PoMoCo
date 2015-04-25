import time

hexy.neck.set(0)

time.sleep(0.5)
hexy.RM.knee(-20)
time.sleep(0.5)
hexy.RM.knee(-40)
time.sleep(0.5)
hexy.RM.knee(-60)

time.sleep(1.5)

hexy.RM.ankle(60)
time.sleep(0.5)
hexy.RM.ankle(40)
time.sleep(0.5)
hexy.RM.ankle(20)
time.sleep(0.5)
hexy.RM.ankle(0)
time.sleep(0.5)
hexy.RM.ankle(-20)
time.sleep(0.5)
hexy.RM.ankle(-40)
time.sleep(0.5)
hexy.RM.ankle(-60)

time.sleep(1.5)

hexy.RM.hip(-45)
time.sleep(0.2)
hexy.RM.hip(-30)
time.sleep(0.2)
hexy.RM.hip(-15)

time.sleep(0.2)
hexy.RM.hip(0)
time.sleep(0.2)
hexy.RM.hip(15)
time.sleep(0.2)
hexy.RM.hip(30)
time.sleep(0.2)
hexy.RM.hip(45)

time.sleep(1.0)

hexy.RM.hip(0)
hexy.RM.ankle(0)
hexy.RM.knee(0)

for servo in hexy.con.servos:
    hexy.con.servos[servo].setPos(deg=0)

#kill all servos
for servo in hexy.con.servos:
    hexy.con.servos[servo].kill()





