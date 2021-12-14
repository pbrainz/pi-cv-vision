import cv2
import time
import argparse
from tqdm import tqdm

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
print("Setting up...")
num_fr = int(vc.get(cv2.CAP_PROP_FRAME_COUNT))
print("Starting Render...")
#--------------------------------------------------
#                 Export Frames
#--------------------------------------------------
check, img = vc.read()
for fn in tqdm(range(0, num_fr), desc ="Rendering Frames"):
  cv2.imwrite(outd+"%d.jpg" % fn, img)  
  check, img = vc.read()
  fn += 1

vc.release()
cv2.destroyAllWindows()