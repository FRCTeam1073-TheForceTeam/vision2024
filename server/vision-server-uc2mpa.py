#!/usr/bin/env python3

import numpy as np
import cv2
import math
from apriltag import apriltag
from networktables import NetworkTables
import sys
import time

if len(sys.argv)<5:
    print("Server {videoDevice} {NetworkTable} {DestinationIP} {DestinationPort}")
    exit()

captureDevice=sys.argv[1]
networkTable=sys.argv[2]
destinationIP=sys.argv[3]
destinationPort=sys.argv[4]

# Capture Video and set resolution from gstreamer pipeline
capture_pipeline = "v4l2src device=%s ! video/x-raw,format=(string)YUYV,width=(int)640,height=(int)480,framerate=30/1 ! videoconvert ! video/x-raw,format=(string)BGR ! appsink emit-signals=True drop=true"%(captureDevice)
print(capture_pipeline)
capture = cv2.VideoCapture(capture_pipeline)
print("Created Video Capture for %s"%(captureDevice))

# Video output streaming to gstreamer pipeline
output_pipeline = "appsrc ! video/x-raw,format=BGR,width=(int)640,height=(int)480,framerate=30/1 ! queue max-size-buffers=2 ! videoconvert ! vaapih264enc ! video/x-h264,framerate=30/1,stream-format=(string)byte-stream,bitrate=(int)900,rate-control=(int)6,profile=(string)main ! rtph264pay config-interval=1 ! udpsink host=%s port=%s"%(destinationIP, destinationPort)

output = cv2.VideoWriter(output_pipeline, cv2.CAP_GSTREAMER, 30, (640, 480))
print("Created Video Output sending to %s"%(destinationIP))

print("OpenCV Version " + cv2.__version__)

if capture.isOpened():
    print("Capture input pipeline created successfully...")
else:
    print("Capture input pipeline creation failed!")

if output.isOpened():
    print("Video output pipeline created successfully...")
else:
    print("Video output pipeline creation failed!")

detector = apriltag("tag16h5")

# Default network table server address is the robo-rio
networkTableIP = "10.10.73.2"

# init network tables and "points" it at the robot:
NetworkTables.initialize(server=networkTableIP)

# Create network table with given table name:
table = NetworkTables.getTable(networkTable)


# Main vision loop:
while(True):

    # Capture frame-by-frame:
    ret, frame = capture.read()

    # Convert frame to a greyscale image for tag detector:
    image = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Run april-tag detector and get back tags:
    tags = detector.detect(image);

    if len(tags) > 0:
        print("{} total tags detected".format(len(tags)))

    # Python list of data output data we're going to send over network tables.
    tagOutput = []

    # Parse the tags we get back into our output format:
    for tag in tags:
        # print(tag)
        (ptA, ptB, ptC, ptD) = (tag['lb-rb-rt-lt'][0], tag['lb-rb-rt-lt'][1], tag['lb-rb-rt-lt'][2], tag['lb-rb-rt-lt'][3]);
        height = abs(ptA[1] - ptC[1])
        width =  abs(ptA[0] - ptC[0])
        if height > 10 and width > 10:
            ptB = (int(ptB[0]), int(ptB[1]))
            ptC = (int(ptC[0]), int(ptC[1]))
            ptD = (int(ptD[0]), int(ptD[1]))
            ptA = (int(ptA[0]), int(ptA[1]))

            # Draw detection lines over the video.
            cv2.line(frame, ptA, ptB, (0,0,250), 2)
            cv2.line(frame, ptB, ptC, (0,0,250), 2)
            cv2.line(frame, ptC, ptD, (0,0,250), 2)
            cv2.line(frame, ptD, ptA, (0,0,250), 2)

            (cX, cY) = (int(tag['center'][0]), int(tag['center'][1]))
            cv2.circle(frame, (cX,cY), 5, (0,0,255), -1)

            tagId = "{}".format(tag['id'])

            cv2.putText(frame, tagId, (ptA[0], ptA[1]-15),
                        cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,255,0), 2)

            tagOutput+= [tag['id'], tag['hamming'],tag['margin'],
            tag['center'][0], tag['center'][1],
            ptA[0], ptA[1],
            ptB[0], ptB[1],
            ptC[0], ptC[1],
            ptD[0], ptD[1]]


   #connects with Network Tables, grabs number of tags found
    table.putNumberArray("Tags1", tagOutput)
    output.write(frame);

# When everything done, release the capture
capture.release()
output.release()
