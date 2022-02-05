# Getting Started With Computer Vision on an Rpi

### Setup
> on the raspberry pi

- before power on, plug in pi camera with blue strip facing forward
- power on, and make sure camera is enabled 
- go to web browser download the zip file by going to this repo and to *clone > download zip*
- (close out of web browser to save RAM)
- go to downloadeds folder in file explorer
- right click the zip file and choose *extract here*
- right click newly created folder, and select open in terminal
- run the following command (this will take a very long time):
- in addition, answer "y" to the update prompt

```
sudo su && bash setup.sh
```

### Intro to OpenCV on an RPI

- shutdown the raspberry pi (top right > logout > reboot)
- this is a good place to stop if limited on time
- power on the pi, go to downloads folder

**Testing Setup**

- right click *pi-cv-vision-main* folder and open in terminal
- run the following command:
```
cd testing_scripts && ls
```
- to run any of the python scripts, run the following command
```
python3 [insert python script name].py
```

### Collecting Data for Furture Use

- go to file explorer, open *pi-cv-vision-main* in terminal
- run the following command:
```
cd tools && ls
```

**vidcap.py** - template for capturing video from a pi camera and exporting to mp4

Example Usage: 
```
python3 vid-cap.py -n test_vid -w 640 -l 480 -f 25 -o /home/pi/out/
```

Press 'Esc' to stop the cature.

Example will result in: 

/home/pi/out/test_vid.mp4

640x480 resolution
25 fps



**get-frames.py** - template for extracting individual frames from a video file

```
Example Usage:

python3 get-frames.py -v /home/pi/out/test_vid.mp4 -o /home/pi/out/
```
