import numpy as np
import cv2
import argparse

#--------------------------------------------------
#                     Arguments
#--------------------------------------------------

all_args = argparse.ArgumentParser()
all_args.add_argument("-n", "--name", required=True,
   help="video name")
all_args.add_argument("-w", "--width", required=True,
   help="frame width")
all_args.add_argument("-l", "--height", required=True,
   help="frame height")
all_args.add_argument("-f", "--fps", required=True,
   help="frames per second")
all_args.add_argument("-o", "--outdir", required=True,
   help="output dir")
args = vars(all_args.parse_args())

#--------------------------------------------------
#            Capture and Export Video
#--------------------------------------------------

c = cv2.VideoCapture(0)
codec = cv2.VideoWriter_fourcc(*'MP4V')

outd = str(args['outdir'])
n = str(args['name'])
outf = outd+n+".mp4"
w, h = int(args['width']), int(args['height'])
f = int(args['fps'])

output = cv2.VideoWriter(outf, codec, f, (w,h))
print("Exporting video to "+outf)
print("Hold 'Esc' for 1-3 seconds to stop capture...")
while(c.isOpened()):
    ret, frame =  c.read()
    if ret == True:
        output.write(frame)
        cv2.imshow("frame", frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break
c.release()
cv2.destroyAllWindows()