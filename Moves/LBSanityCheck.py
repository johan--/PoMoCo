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
hexy.LB.knee(-20)
time.sleep(0.5)
hexy.LB.knee(-40)
time.sleep(0.5)
hexy.LB.knee(-60)

time.sleep(0.5)
hexy.LB.ankle(60)
time.sleep(0.5)
hexy.LB.ankle(40)
time.sleep(0.5)
hexy.LB.ankle(20)
time.sleep(0.5)
hexy.LB.ankle(0)
time.sleep(0.5)
hexy.LB.ankle(-20)
time.sleep(0.5)
hexy.LB.ankle(-40)
time.sleep(0.5)
hexy.LB.ankle(-60)


time.sleep(0.2)
hexy.LB.hip(15)
time.sleep(0.2)
hexy.LB.hip(30)
time.sleep(0.2)
hexy.LB.hip(45)

#kill all servos
for servo in hexy.con.servos:
    hexy.con.servos[servo].kill()




