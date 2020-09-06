import time
from flyt_python import api

#creating the instance
quadcopter = api.navigation(timeout=120000)
time.sleep(3)

print("ARMING & TAKEOFF")
time.sleep(1)
quadcopter.take_off(5.0)

print("APPROACHING WAYPOINT 1")
time.sleep(1)
quadcopter.position_set(6.5, 0, 0, relative=True)
time.sleep(1)
print("WAYPOINT 1 REACHED")
time.sleep(1)

print("APPROACHING WAYPOINT 2")
time.sleep(1)
quadcopter.position_set(0, 6.5, 0, relative=True)
time.sleep(1)
print("WAYPOINT 2 REACHED")
time.sleep(1)

print("APPROACHING WAYPOINT 3")
time.sleep(1)
quadcopter.position_set(-6.5, 0, 0, relative=True)
time.sleep(1)
print("WAYPOINT 3 REACHED")
time.sleep(1)

print("APPROACHING WAYPOINT 4")
time.sleep(1)
quadcopter.position_set(0, -6.5, 0, relative=True)
time.sleep(1)
print("WAYPOINT 4 REACHED")
time.sleep(1)

print("APPROACH LANDING")
time.sleep(1)
quadcopter.land(async=True)

quadcopter.disconnect()

