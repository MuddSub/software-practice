import PIDcontrol, sensor
from fake_ros import rospy
import time, random

depth = 0.0
velocity = -1.0

control = PIDcontrol.Control()

last_time = time.time()

while True:
    delay = random.random() * 0.5
    time.sleep(0.02)
    velocity += (control.get_power()-1200)/1200 + random.random() * 0.1 - 0.05
    depth += velocity
    if time.time() - last_time > delay:
        rospy.update(depth)
    
