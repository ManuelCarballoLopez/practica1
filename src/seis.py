#!/usr/bin/env python

import rospy

from std_msgs.msg import Int32

num=Int32()      

rospy.init_node('publicador_seis')        # Inicializamos el nodo

pub=rospy.Publisher('/mensaje_teclado',Int32,queue_size=1) 

 

while not rospy.is_shutdown():      # Bucle
    num.data=Int32(input("Introduce un numero entero: "))
    pub.publish(num.data)
 