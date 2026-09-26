from fake_ros import rospy, Float


class Control:
    def __init__(self, desired_depth):
        """Assume you have a node called drivers/depth that publishes the sensors depth value"""
        pass

    def get_power(self):
        """1200 is the default (no power, neutrally bouyant)
        higher numbers make it go up (less depth)"""
        return 1200

