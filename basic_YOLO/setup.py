import os
import subprocess
import fnmatch
from tqdm import tqdm
import sys
from pathlib import Path
import requests

urls = [
    "https://raw.githubusercontent.com/pjreddie/darknet/master/cfg/yolov3.cfg",
    "https://pjreddie.com/media/files/yolov3.weights",
    "https://raw.githubusercontent.com/pjreddie/darknet/master/data/coco.names"
]

def find(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result

RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[0;33m'
BLUE='\033[0;34m'
NC='\033[0m'

prog=1
progt=len(urls)

sub_path = "model"
os.makedirs(sub_path, exist_ok=True)

chunk_size = 1024
for url in urls:
    print(NC+"\n["+str(prog)+"/"+str(progt)+"]"+GREEN+" Downloading "+url[url.rindex('/')+1:]+BLUE)
    filesize = int(requests.head(url).headers["Content-Length"])
    filename = os.path.basename(url)
    dl_path = os.path.join(sub_path, filename)
    chunk_size = 1024

    with requests.get(url, stream=True) as r, open(dl_path, "wb") as f, tqdm(
        unit="B", 
        unit_scale=True,
        unit_divisor=1024,
        total=filesize,
        file=sys.stdout,
        desc=filename
    ) as progress:
        for chunk in r.iter_content(chunk_size=chunk_size):
            datasize = f.write(chunk)
            progress.update(datasize)
    prog+=1

print(GREEN+"\nDONE!!!")
