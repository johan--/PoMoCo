import time

hexy.neck.set(0)

time.sleep(0.5)
hexy.LM.knee(-20)
time.sleep(0.5)
hexy.LM.knee(-40)
time.sleep(0.5)
hexy.LM.knee(-60)

time.sleep(1.5)

hexy.LM.ankle(60)
time.sleep(0.5)
hexy.LM.ankle(40)
time.sleep(0.5)
hexy.LM.ankle(20)
time.sleep(0.5)
hexy.LM.ankle(0)
time.sleep(0.5)
hexy.LM.ankle(-20)
time.sleep(0.5)
hexy.LM.ankle(-40)
time.sleep(0.5)
hexy.LM.ankle(-60)

time.sleep(1.5)

hexy.LM.hip(-45)
time.sleep(0.2)
hexy.LM.hip(-30)
time.sleep(0.2)
hexy.LM.hip(-15)

time.sleep(0.2)
hexy.LM.hip(0)
time.sleep(0.2)
hexy.LM.hip(15)
time.sleep(0.2)
hexy.LM.hip(30)
time.sleep(0.2)
hexy.LM.hip(45)

time.sleep(1.0)

hexy.LM.hip(0)
hexy.LM.ankle(0)
hexy.LM.knee(0)

for servo in hexy.con.servos:
    hexy.con.servos[servo].setPos(deg=0)

#kill all servos
for servo in hexy.con.servos:
    hexy.con.servos[servo].kill()




