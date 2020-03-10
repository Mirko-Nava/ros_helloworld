#!/usr/bin/env python

import rospy
from std_msgs.msg import String


class HelloworldPub:

    def __init__(self):
        """Initialization."""

        # initialize the node

        self.name = '<your_name_here>'

        # create string publisher

        # set node update frequency in Hz

    def publish(self):
        """Publishes a message."""


if __name__ == '__main__':
    publisher = HelloworldPub()

    publisher.publish()
