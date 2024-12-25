#!/usr/bin/env python3
import rospy
from sensor_msgs.msg import CompressedImage, Image
from cv_bridge import CvBridge
import cv2
import numpy as np

def image_callback(msg):
    bridge = CvBridge()
    try:
        # 解压缩图像
        np_arr = np.frombuffer(msg.data, np.uint8)
        cv_image = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)
        ros_image = bridge.cv2_to_imgmsg(cv_image, "bgr8")
        ros_image.header = msg.header
        image_pub.publish(ros_image)
    except Exception as e:
        rospy.logerr("Error converting image: %s", str(e))

if __name__ == '__main__':
    rospy.init_node('image_decompressor', anonymous=True)
    rospy.loginfo("Starting image decompressor node...")

    # 订阅压缩图像
    image_sub = rospy.Subscriber("/camera/color/image_raw/compressed", CompressedImage, image_callback)

    # 发布非压缩图像
    image_pub = rospy.Publisher("/camera/color/image_raw", Image, queue_size=10)

    rospy.spin()

