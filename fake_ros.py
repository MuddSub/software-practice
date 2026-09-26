import sensor
Float = 0.0

    


class ros:
    def __init__(self):
        self.connected = False
        self.callback = None

    def Subscriber(self, node, type, callback):
        self.callback = callback
        if node == "drivers/depth":
            self.connected = True

    def update(self, depth):
        if self.connected:
            sensor.generate_data(self.callback, depth)

rospy = ros()