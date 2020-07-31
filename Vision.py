#!/usr/bin/python
import cv2 as cv
import numpy as np

cap = cv.VideoCapture(0)
cv.namedWindow("window")
bounds = ['Lower', 'Upper']
attributes = ['Hue','Sat','Val']
scope = [np.array([0,0,0]), np.array([255,255,255])]

def Hue(bound): return cv.getTrackbarPos(f'{bound}: Hue', 'window')
def Sat(bound): return cv.getTrackbarPos(f'{bound}: Sat', 'window')
def Val(bound): return cv.getTrackbarPos(f'{bound}: Val', 'window')

def scope(h1, s1, v1, h2, s2, v2):
    return [ np.array([h1 ,s1, v1]), np.array([h2 ,s2 ,v2]) ]

cv.createTrackbar('Lower: Hue', 'window', 0, 255, lambda x: Hue("Lower"))
cv.createTrackbar('Lower: Sat', 'window', 0, 255, lambda x: Sat("Lower"))
cv.createTrackbar('Lower: Val', 'window', 0, 255, lambda x: Val("Lower"))
cv.createTrackbar('Upper: Hue', 'window', 0, 255, lambda x: Hue("Upper"))
cv.createTrackbar('Upper: Sat', 'window', 0, 255, lambda x: Sat("Upper"))
cv.createTrackbar('Upper: Val', 'window', 0, 255, lambda x: Val("Upper"))

while (1):
    _, frame = cap.read()
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)
    _scope = scope( Hue(bounds[0]),Sat(bounds[0]),Val(bounds[0]),
                    Hue(bounds[1]),Sat(bounds[1]),Val(bounds[1]))
    mask = cv.inRange(hsv, _scope[0], _scope[1])
    res = cv.bitwise_and(frame,frame, mask= mask)
    cv.imshow("window", res)
    key = cv.waitKey(1)  # milliseconds/update (fps), grabs keyboard
    if key == 113: break # 'q' is 113 on my machine; use print(key)

cv.destroyAllWindows()
