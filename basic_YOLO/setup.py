import os
import subprocess
import fnmatch

def find(pattern, path):
    result = []
    for root, dirs, files in os.walk(path):
        for name in files:
            if fnmatch.fnmatch(name, pattern):
                result.append(os.path.join(root, name))
    return result


os.system("mkdir model")
print("Changing dir to ./model")
os.chdir("model")

links = [
    "https://raw.githubusercontent.com/pjreddie/darknet/master/cfg/yolov3.cfg",
    "https://pjreddie.com/media/files/yolov3.weights",
    "https://raw.githubusercontent.com/pjreddie/darknet/master/data/coco.names"
]

prog=1
progt=len(links)

for link in links:
    print("["+str(prog)+"/"+str(progt)+"]"+" Downloading "+link[link.rindex('/')+1:])
    os.system("wget "+str(link)+" 2>/dev/null")
    prog+=1

print("DONE!!!")
