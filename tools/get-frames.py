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
vc = cv2.VideoCapture(v)

#--------------------------------------------------
#             Calculate Num of Frames
#--------------------------------------------------

num_fr = int(vc.get(cv2.CAP_PROP_FRAME_COUNT))

#--------------------------------------------------
#                 Export Frames
#--------------------------------------------------
time.sleep(3)
y,img = vc.read()
num_fr-=1
i = 0
while y:
  cv2.imwrite(outd+"%d.jpg" % i, img)  
  y,img = vc.read()
  print("Rendered: "+str(i)+" | Queued: "+str(num_fr))
  i += 1
  num_fr-=1

vc.release()
cv2.destroyAllWindows()