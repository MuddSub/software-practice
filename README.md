# software-practice
This is the first practice for ROS, it focuses on understanding subscribers and callbacks. Everything you need is in the PIDcontrol.py tab. To test your code, run sim.py. You should see the depth sensor readings eventually stablize around 1 (there will still be some random fluctuations, but it should stay near 1). Since this is not the full ROS library, you cannot run every ROS command. However, should you have everything necessary for the excercise. Please ask a software lead or someone else in the group if you need help!

Important commands for this exercise:
rospy.Subscriber(topic, message_type, callback)
This will subscribe you to a topic (passed as a string). Whenever a new message is published to the topic the callback will be called with that new message as the parameter. For this simulation, message_type is not actually used behind the scenes (use Float when you call it) but in real ROS it is important to give the correct type of message.