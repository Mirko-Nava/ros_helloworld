#!/usr/bin/env python

import rospy
from std_msgs.msg import String


class HelloworldSub:

    def __init__(self):
        """Initialization."""

        # initialize the node

        # create string subscriber

        # set node update frequency in Hz

    def greet(self, data):
        """Greets the person."""

    def wait_for_termination(self):
        """Waits until the node is terminated."""


if __name__ == '__main__':
    subscriber = HelloworldSub()

    subscriber.wait_for_termination()
