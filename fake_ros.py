import sensor
from collections import deque
Float = 0.0

    
class Publisher:
    def __init__(self, ros: ros, topic: str):
        self.ros = ros
        self.topic = topic
    
    def publish(self, value):
        """In ros, the value needs to be the appropriate type for the topic"""
        self.ros.topic_updated(self.topic, value)

class ros:
    def __init__(self):
        self.subscribers = {}

    def Subscriber(self, topic, type, callback):
        if topic in self.subscribers.keys():
            self.subscribers[topic].append(callback)
        else:
            self.subscribers[topic] = [callback]

    def Publisher(self, topic, type, *, queue_size=None):
        return Publisher(self, topic)

    # def update(self, depth):
    #     if self.connected:
    #         sensor.generate_data(self.callback, depth)

    def topic_updated(self, topic, value):
        if topic in self.subscribers.keys():
            for callback in self.subscribers[topic]:
                callback(value)

rospy = ros()