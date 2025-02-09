
rospy.init_node('message_publisher')

pub = rospy.Publisher('complex', Complex)

rate = rospy.Rate(2)

while not rospy.is_shutdown():
    msg = Complex()
    msg.real = random()
    msg.imaginary = random()

    pub.publish(msg)
    rate.sleep()

