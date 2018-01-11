"""
Created on Tue Jan  9 14:32:47 2018

@author: Trent Torakr
"""
import cv2
import urllib.request as urlreq
import time
import numpy as np
import random


def url_to_image(url):
    # download the image, convert it to a NumPy array, and then read
    # it into OpenCV format
    resp = urlreq.urlopen(url)
    image = np.asarray(bytearray(resp.read()), dtype="uint8")
    image = cv2.imdecode(image, cv2.IMREAD_COLOR)
 
    # return the image
    return image

def readCamera(cam, auth):
    snap = "/snapshot.cgi?"
    url_shot = cam+snap+auth
    image = url_to_image(url_shot)
    print(url_shot)
    return image

def getCameraParams(cam, auth):
    param = "/get_camera_params.cgi?"
    url_params = cam+param+auth
    params = url_to_image(url_params)
    return params
    
def moveCamera(cam, auth, direction):
    # 0 == Up, 4 == Left, 2 == Down, 6 == Right
    direction = str(direction)
    moveURL = cam + "/decoder_control.cgi?command=" + direction + auth
    urlreq.urlopen(moveURL)
    print(moveURL)
    
def gotoCode(cam, auth, code):
    goto = '/decoder_control.cgi?command=' + code
    url_goto = cam + goto + auth
    urlreq.urlopen(url_goto)

import securityDetails
w_IP = securityDetails.w_IP
w_PORT = securityDetails.w_PORT
w_USER = securityDetails.w_USER
w_PASS = securityDetails.w_PASS
#TenvisVideo( securityDetails.w_IP , securityDetails.w_PORT , securityDetails.w_USER , securityDetails.w_PASS )
cam = "http://" + w_IP + ":" + w_PORT 
auth = "&user=" + w_USER + "&pwd=" + w_PASS
readCamera(cam, auth)
actions = [0,2,4,6]
while True:
#    moveCamera(cam, auth, random.choice(actions))
    image = readCamera(cam, auth)
    cv2.imshow('image',image)
    
    
    
    
    k = cv2.waitKey(1)
    if k == 27:         # wait for ESC key to exit
        cv2.destroyAllWindows()
        break
