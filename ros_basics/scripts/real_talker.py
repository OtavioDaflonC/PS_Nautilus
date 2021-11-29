#!/usr/bin/env python3
# license removed for brevity
import rospy
from geometry_msgs.msg import Vector3
import random

class talker:
    def __init__(self):
        rospy.init_node('talker', anonymous=True)
        self.pub = rospy.Publisher('nome_do_publisher', Vector3, queue_size=10)
        self.lista=list(range(20))
    
    def start(self):
        rate = rospy.Rate(10) # 10hz
        while not rospy.is_shutdown():
            v= Vector3()
            #temos aqui a representação de movimento através de um vetor
            #velocidade em espaço tridimencional, formado por números aleatórios
            # de 0 a 20, sem representar assim qualquer dinâmica de movimento
            # real.
            v.x=random.choice(self.lista)
            v.y=random.choice(self.lista)
            v.z=random.choice(self.lista)
            rospy.loginfo(v)
            self.pub.publish(v)
            rate.sleep()
 

if __name__ == '__main__':
     try:
         t= talker()
         t.start()

     except rospy.ROSInterruptException:
         pass