#!/usr/bin/env python

import rospy
from std_msgs.msg import String


class HelloworldPub:

    def __init__(self):
        """Initialization."""

        # initialize the node
        rospy.init_node(
            'helloworld_pub'  # name of the node
        )

        self.name = '<your_name_here>'

        # create string publisher
        self.publisher = rospy.Publisher(
            '/helloworld',  # name of the topic
            String,  # message type
            queue_size=10  # queue size
        )

        # set node update frequency in Hz
        self.rate = rospy.Rate(10)

    def publish(self):
        """Publishes a message."""

        while not rospy.is_shutdown():

            # publish the message
            self.publisher.publish(self.name)

            # sleep until next step
            self.rate.sleep()


if __name__ == '__main__':
    publisher = HelloworldPub()

    try:
        publisher.publish()
    except rospy.ROSInterruptException as e:
        pass
