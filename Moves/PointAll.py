import time

deg = -30

# Move: Point RF
hexy.neck.set(0)
time.sleep(0.5)
hexy.neck.set(30)
time.sleep(0.5)
hexy.RF.knee(-60)
hexy.RF.ankle(-60)
time.sleep(0.2)
hexy.RF.hip(45)
hexy.neck.set(0)

# Move: Point LF
hexy.LF.knee(-60)
hexy.LF.ankle(-60)
time.sleep(0.2)
hexy.LF.hip(45)
hexy.neck.set(0)


