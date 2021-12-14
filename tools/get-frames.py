import cv2
import time
import argparse

#--------------------------------------------------
#                     Arguments
#--------------------------------------------------

all_args = argparse.ArgumentParser()
all_args.add_argument("-v", "--video", required=True,
   help="video file")
all_args.add_argument("-o", "--outdir", required=True,
   help="output dir")
args = vars(all_args.parse_args())

v = str(args['video'])
outd = str(args['outdir'])

#--------------------------------------------------
#                 Export Frames
#--------------------------------------------------

time.sleep(3)
vc = cv2.VideoCapture(v)
success,image = vc.read()
i = 0
while success:
  cv2.imwrite(outd+"%d.jpg" % str(i), image)  
  success,image = vc.read()
  print('Rendered Frame: '+str(i), success)
  i += 1

vc.release()
cv2.destroyAllWindows()