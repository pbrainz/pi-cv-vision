# Getting Started With Computer Vision on an Rpi
> This repo just holds some sandboxed src code for messing around with opencv, torchvision, and tensorflow. 

**vidcap.py** - template for capturing video from a pi camera and exporting to mp4

```
Example Usage: 

python3 vid-cap.py -n test_vid -w 640 -l 480 -f 25 -o /home/pi/out/


Press 'Esc' to stop the cature.

Example will result in: 

/home/pi/out/test_vid.mp4
640x480 resolution
25 fps
```

**get-frames.py** - template for extracting individual frames from a video file

```
Example Usage:

python3 get-frames.py -v /home/pi/out/test_vid.mp4 -o /home/pi/out/
```


### Using Models
*You will need to consider making changes to the model in order for it to function properly*

### Data
1. Make sure to change change the data directory.
 - This is defined in the model *here*

### Circuits
2. Make sure to follow the circuit diagrams, or
   you can define your own GPIO layout
 - The GPIO variables are located *here*
