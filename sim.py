import PIDcontrol, sensor
from fake_ros import rospy, Float
import time, random

depth = 0.0
velocity = 1.0

control = PIDcontrol.Control(1.0)

last_time = time.time()

depth_sensor_publisher = rospy.Publisher("drivers/depth", Float, queue_size=1)

while True:
    delay = random.random() * 0.5
    time.sleep(0.02)
    velocity += (control.get_power()-1200)/1200 + random.random() * 0.01 - 0.005
    velocity *= 0.9
    depth += velocity
    if time.time() - last_time > delay:
        print(depth)
        depth_sensor_publisher.publish(sensor.generate_data(depth))
    
