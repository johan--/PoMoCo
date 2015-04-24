import time

deg = -30

hexy.neck.set(0)

time.sleep(0.2)
hexy.neck.set(-20)
time.sleep(0.2)
hexy.neck.set(-40)
time.sleep(0.5)
hexy.neck.set(-60)

time.sleep(0.2)
hexy.neck.set(0)

time.sleep(0.2)
hexy.neck.set(20)
time.sleep(0.2)
hexy.neck.set(40)
time.sleep(0.5)
hexy.neck.set(60)

time.sleep(1.0)

time.sleep(0.5)
hexy.RB.knee(-20)
time.sleep(0.5)
hexy.RB.knee(-40)
time.sleep(0.5)
hexy.RB.knee(-60)

time.sleep(0.5)
hexy.RB.ankle(60)
time.sleep(0.5)
hexy.RB.ankle(40)
time.sleep(0.5)
hexy.RB.ankle(20)
time.sleep(0.5)
hexy.RB.ankle(0)
time.sleep(0.5)
hexy.RB.ankle(-20)
time.sleep(0.5)
hexy.RB.ankle(-40)
time.sleep(0.5)
hexy.RB.ankle(-60)


time.sleep(0.2)
hexy.RB.hip(15)
time.sleep(0.2)
hexy.RB.hip(30)
time.sleep(0.2)
hexy.RB.hip(45)

#kill all servos
for servo in hexy.con.servos:
    hexy.con.servos[servo].kill()




