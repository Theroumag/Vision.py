import cv2
import numpy as np

#Captures first frame
cap = cv2.VideoCapture(0)

#cap.read returns 2 outputs, a bool if the capture was succesful
#and the read frame
err, src = cap.read()

#Used to erode small white bits
kernel = np.ones((10,10), np.uint8)

#upper color limit
up = np.array([255, 255, 255])
#lower color limit
down = np.array([0, 0, 0])

#functions for sliders (adjusts color to slider value)
def upH(hue):
    up[0] = hue

def upV(hue):
    up[1] = hue

def upS(hue):
    up[2] = hue

def downH(hue):
    down[0] = hue
    
def downS(hue):
    down[1] = hue

def downV(hue):
    down[0] = hue


erode_times = 0
def erode(value):
    global erode_times
    erode_times += 1
    print(erode_times)
    
#creates empty window with sliders
window = cv2.namedWindow("Slider Page")
#0, 255 are upper and lower slider values the last parameter is the fuction called when slider moved
cv2.createTrackbar("Up_Hue", "Slider Page", 0, 255, upH)
cv2.createTrackbar("Up_Sat", "Slider Page", 0, 255, upS)
cv2.createTrackbar("Up_Val", "Slider Page", 0, 255, upV)
cv2.createTrackbar("Down_Hue", "Slider Page", 0, 255, downH)
cv2.createTrackbar("Down_Sat", "Slider Page", 0, 255, downS)
cv2.createTrackbar("Down_Val", "Slider Page", 0, 255, downV)
cv2.createTrackbar("To Erode", "Slider Page", 0, 1, erode)

#displays constant stream of frames (i.e. Video)
while True:
    #src = cv2.erode(src, kernel)
    #erode(src)
    #src = src1
    err, src = cap.read()
    src = cv2.flip(src, 1)
    #converts RGB color scheme to HSV. In RBG the diffrence between
    #red and blue is a little nudge, and in HSV it's clearly seperated
    src = cv2.cvtColor(src, cv2.COLOR_BGR2HSV)
    #Colors in range if upper bounds and lower bounds
    src = cv2.inRange(src, down, up)
    for time in range((erode_times+1)):
        src = cv2.erode(src, kernel)
    cv2.imshow(window, src)
    #fps
    cv2.waitKey(20)

with open("colorFile.txt", "w") as colorFile:
    colorFile.write(up, down)
