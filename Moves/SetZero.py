# Move: Set Zero

for servo in hexy.con.servos:
    hexy.con.servos[servo].setPos(deg=0)

#kill all servos
for servo in hexy.con.servos:
    hexy.con.servos[servo].kill()
