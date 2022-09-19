from pynput import keyboard
import rospy
import roslaunch
from geometry_msgs.msg import Twist
from turtlesim.srv import TeleportAbsolute, TeleportRelative
import termios, sys, os
from numpy import pi
from std_srvs.srv import Empty

rospy.init_node('TeleopKey', anonymous=True)

def pubVel(speed, angspeed, t):
    velpub = rospy.Publisher('/turtle1/cmd_vel', Twist, queue_size=10)
    velmsg = Twist()
    velmsg.linear.x = speed
    velmsg.angular.z = angspeed
    velpub.publish(velmsg)
    endTime = rospy.Time.now() + rospy.Duration(t)
    while rospy.Time.now() < endTime:
        velpub.publish(velmsg)

def on_press(key):
    return

def on_release(key):
    if key == keyboard.KeyCode.from_char('w'):
        pubVel(1, 0, 0.5)
    if key == keyboard.KeyCode.from_char('s'):
        pubVel(-1, 0, 0.5)
    if key == keyboard.KeyCode.from_char('a'):
        pubVel(0, -1, 0.5)
    if key == keyboard.KeyCode.from_char('d'):
        pubVel(0, 1, 0.5)
    if key == keyboard.Key.space:
         try:
                # Wait for the service to be available
                rospy.wait_for_service('/turtle1/teleport_relative')
                # Create handle to call the service
                giro = rospy.ServiceProxy('/turtle1/teleport_relative', TeleportRelative)
                giro(0, pi)
                rospy.loginfo('Turtle rotated')
         except rospy.ServiceException as e:  # If the service is not available, print a warning
                rospy.logwarn("Service teleport_relative call failed")
                
    if key == keyboard.KeyCode.from_char('r'):
         try:
                rospy.wait_for_service('/turtle1/teleport_absolute')
                teleportOrigen = rospy.ServiceProxy('/turtle1/teleport_absolute', TeleportAbsolute)
                Reset=teleportOrigen(5.5, 5.5, 0)

                rospy.wait_for_service('/clear')  # Clear the trajectory
                clearTrajec = rospy.ServiceProxy('/clear', Empty)
                Reset = clearTrajec()

                rospy.loginfo('Turtle reset')
         except rospy.ServiceException as e:
                    rospy.logwarn("Service teleport_absolute call failed")

with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()