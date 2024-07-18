from robot import Robot
from dynamixel import Dynamixel
from vr_controller import VRController
import numpy as np

try:
    follower = Robot(device_name='/dev/ttyACM1', servo_ids=[1, 2, 3, 4, 5])
except:
    follower = Robot(device_name='/dev/ttyACM0', servo_ids=[1, 2, 3, 4, 5])
        
leader = VRController()
leader.start()
while True:
    target_pos = leader.read_position()
    follower.set_goal_pos(target_pos)