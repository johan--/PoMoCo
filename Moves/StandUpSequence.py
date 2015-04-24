import time

deg = -30

#put all the feet centered and on the floor.

hexy.LF.hip(-deg)
hexy.RM.hip(1)
hexy.LB.hip(deg)

hexy.RF.hip(deg)
hexy.LM.hip(1)
hexy.RB.hip(-deg)

time.sleep(0.5)

