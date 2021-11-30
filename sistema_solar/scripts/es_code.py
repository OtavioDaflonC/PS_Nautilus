#!/usr/bin/env python3

import rospy
from geometry_msgs.msg import TransformStamped

import tf2_ros
import math

class RandomTransform:
    def __init__(self,plt):
        rospy.init_node('es_code', anonymous=True)
        
        self.raio = plt['distancia']
        #Acessa o parâmetro de distância que cada planeta possui da referencia.
        self.tf = TransformStamped()
        self.tf.header.frame_id = "Referencia"
        self.tf.child_frame_id = plt['nome']
        self.tf.header.stamp = rospy.Time.now()
        self.tf.transform.rotation.w = 1
        self.broadcaster = tf2_ros.TransformBroadcaster()

    def broadcast(self):
       
        ang = rospy.Time.now().to_sec() 
        #esta contagem de tempo será a referência de ângulo. Será calibrado
        #periodicamente pelo fator de pi aplicando trigonometria.
        
        
      
        self.tf.transform.translation.x = (math.cos(ang)*self.raio)
        self.tf.transform.translation.y = (math.sin(ang)*self.raio)
        self.tf.transform.translation.z = 0
        self.tf.header.stamp = rospy.Time.now()
        self.broadcaster.sendTransform(self.tf)


 

if __name__ == '__main__':
    rndtf = [RandomTransform(plt) for plt in rospy.get_param('lista').values()]
    #uma lista de elementos dentro do dicionário 'lista' para indexar cada planeta.
    
    

    rate = rospy.Rate(200) # 200hz
    # a frequência afeta a resolução do movimento sendo que controla o numero de atualizações da posi
    #ção po segundo.
    while not rospy.is_shutdown():
        
        for rndtransform in rndtf:
            rndtransform.broadcast()

            
        rate.sleep()

    try:
        t= RandomTransform()
        t.start()

    except rospy.ROSInterruptException:
        pass