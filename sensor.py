import random
import time

def generate_data(callback, depth):
    callback(depth+random.random()*0.5-0.25)
