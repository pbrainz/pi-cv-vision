# Example usage: python3 vidcap.py -n lol -wt 1344 -ht 756 -nf 90 -fps 30 -o /home/pi/out/
import cv2
import argparse
import numpy as np

all_args = argparse.ArgumentParser()
all_args.add_argument("-n", "--name", required=True,
   help="video name")
all_args.add_argument("-wt", "--width", required=True,
   help="frame width")
all_args.add_argument("-ht", "--height", required=True,
   help="frame height")
#all_args.add_argument("-nf", "--num_fr", required=True,
#   help="number of frames")
#all_args.add_argument("-fps", "--fps", required=True,
#   help="frames per second")
all_args.add_argument("-o", "--outdir", required=True,
   help="output dir")

args = vars(all_args.parse_args())
outd = str(args['outdir'])
name = str(args['name'])
outf = outd+name+".mp4"
# 1344, 756, 90, 30 results in 90 frames, resolution 1344x756, and 25 fps
w, h = int(args['width']), int(args['height'])
#nf, fps = int(args['num_fr']), int(args['fps'])
cap=cv2.VideoCapture(0)
#width=int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
#height=int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
writer= cv2.VideoWriter(outf, cv2.VideoWriter_fourcc(*'DIVX'), 20, (w,h))
while True:
    ret,frame= cap.read()
    writer.write(frame)
    cv2.imshow('frame', frame)
    if cv2.waitKey(1) & 0xFF == 27:
        break
cap.release()
writer.release()
cv2.destroyAllWindows()

# Example usage: python3 vidcap.py -n lol -wt 1344 -ht 756 -o /home/pi/out/