from fake_ros import rospy, Float


class Control:
    def __init__(self, desired_depth):
        pass

    def get_power(self):
        """1200 is the default (no power, neutrally bouyant)
        higher numbers make it go up (less depth)"""
        return 1200