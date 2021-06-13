#!/usr/bin/python3

"""
Display the image captured from the camera. Used as a test program to verify if OpenCV has been properly installed.

YunFei Robotics Labrotary
Twitter: @yfrobotics
Website: https://www.yfrl.org
"""

import cv2

# 160 x 120
# 320 x 240
# 640 x 480 (480p)
# 1280 x 720 (720p)
# 1920 x 1080 (1080p; make sure your camera supports this high resolution.)

CAMERA_DEVICE_ID = 0
IMAGE_WIDTH = 640
IMAGE_HEIGHT = 480


if __name__ == "__main__":
    try:
        # create video capture
        cap = cv2.VideoCapture(CAMERA_DEVICE_ID)

        # set resolution to 320x240 to reduce latency 
        cap.set(3, IMAGE_WIDTH)
        cap.set(4, IMAGE_HEIGHT)

        # Loop to continuously get images
        while True:
            # Read the frames from a camera
            _, frame = cap.read()

            # show image
            cv2.imshow('frame', frame)

            # if key pressed is 'Esc' then exit the loop
            if cv2.waitKey(33) == 27:
                break
    except Exception as e:
        print(e)
    finally:
        # Clean up and exit the program
        cv2.destroyAllWindows()
        cap.release()
