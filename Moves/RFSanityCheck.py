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
hexy.RF.knee(-20)
time.sleep(0.5)
hexy.RF.knee(-40)
time.sleep(0.5)
hexy.RF.knee(-60)

time.sleep(0.5)
hexy.RF.ankle(60)
time.sleep(0.5)
hexy.RF.ankle(40)
time.sleep(0.5)
hexy.RF.ankle(20)
time.sleep(0.5)
hexy.RF.ankle(0)
time.sleep(0.5)
hexy.RF.ankle(-20)
time.sleep(0.5)
hexy.RF.ankle(-40)
time.sleep(0.5)
hexy.RF.ankle(-60)


time.sleep(0.2)
hexy.RF.hip(15)
time.sleep(0.2)
hexy.RF.hip(30)
time.sleep(0.2)
hexy.RF.hip(45)

#kill all servos
for servo in hexy.con.servos:
    hexy.con.servos[servo].kill()




