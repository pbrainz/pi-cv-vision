# Example usage: python3 vidcap.py -n lol -wi 1344 -hi 756 -nf 90 -fps 30 -o /home/pi/out/

from picamera.array import PiRGBArray
from picamera import PiCamera
import time
import datetime
import cv2
import argparse
from imutils.video import VideoStream
import sys
import os

all_args = argparse.ArgumentParser()
all_args.add_argument("-n", "--name", required=True,
   help="video name")
all_args.add_argument("-wi", "--widthin", required=True,
   help="frame width capture")
all_args.add_argument("-hi", "--heightin", required=True,
   help="frame height capture")
all_args.add_argument("-wo", "--widthout", required=True,
   help="frame width out")
all_args.add_argument("-ho", "--heightout", required=True,
   help="frame height out")
all_args.add_argument("-fps", "--fps", required=True,
   help="frames per second")
all_args.add_argument("-o", "--outdir", required=True,
   help="output dir")

args = vars(all_args.parse_args())
outd = str(args['outdir'])
name = str(args['name'])
outf = outd+name+".mp4"
wi, hi = int(args['widthin']), int(args['heightin'])
wo, ho = int(args['widthout']), int(args['heightout'])
fps = int(args['fps'])

c = PiCamera()
c.resolution = (wi, hi)
c.framerate = fps
rawCapture = PiRGBArray(c, size=(wi, hi))
codec = cv2.VideoWriter_fourcc(*'MP4V')

outv = cv2.VideoWriter(outf, codec, fps, (wo, ho))

def main():
    # capture frames from the camera
    time.sleep(0.1)
    x = 0
    for f in c.capture_continuous(rawCapture, format="bgr", use_video_port=True):
        i = f.array
        #cv2.imshow("Frame", image)
        key = cv2.waitKey(1) & 0xFF
        outv.write(i)
        rawCapture.truncate(0)
        print(x)
        x += 1
        if cv2.waitKey(1) & 0xFF == 27:
            break
# python3 3.py -n dev -wi 1920 -hi 1080 -wo 300 -ho 300 -fps 25 -o /home/pi/out/
try:
    main()
except KeyboardInterrupt:
    print('Exiting...')
    try:
        sys.exit(0)
    except SystemExit:
        os._exit(0)