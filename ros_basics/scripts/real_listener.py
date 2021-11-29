#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float64
from geometry_msgs.msg import Point


class listener:
    def __init__ (self):
        rospy.init_node('listener', anonymous=True)
        rospy.Subscriber('nome_do_publisher', Point, self.callback)
        self.pub = rospy.Publisher('resultado', Float64,queue_size=10)

    def callback(self,msg):
        #o calculo do módulo velocdade é feito aqui:
        x,y,z = msg.x,msg.y,msg.z
        norma = (x**2 + y**2 + z**2)**(1/2)
        f = Float64()
        f.data= norma
        self.pub.publish(f)


if __name__ == '__main__':
    l= listener()
    rospy.spin()