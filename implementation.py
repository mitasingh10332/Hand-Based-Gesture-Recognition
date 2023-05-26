import cv2 as cv
from cvzone.HandTrackingModule import HandDetector
import pyautogui as p
import time as t
# p.FAILSAFE = False
width,height = 1000,900

# capture camera
cap = cv.VideoCapture(0)
cap.set(3,width)
cap.set(4,height)

# Hand detection
detector = HandDetector(detectionCon=0.8,maxHands=1)


# parameters

gestureThreshold = 320
   
while True:
    _,frame = cap.read()
    frame = cv.flip(frame,1) # 0 means fliop in vertical 1 means flip in horizontal
    

    # Hand detection code
    hands,frame = detector.findHands(frame)
    cv.line(frame,(0,gestureThreshold),(width,gestureThreshold),(0,255,0),4)

    if hands:
        hand = hands[0] # hand is a dictionary that is an element of list in python
        # print(hand['type'])
        # debugging changing hand type || after finding solution i add it in my module library
        # if hand['type'] == 'Right':
        #     hand['type'] = 'Left'
            # print(hand['type']) it printed right but the cvzone imwrite functionallity print it wrong
        # elif hand['type'] == 'Left':
        #     hand['type'] = 'Right'
            # print(hand['type'])

        fingers = detector.fingersUp(hand) # it returns a list
        cx,cy = hand['center']
        print(fingers)

        if cy<=gestureThreshold: # if gesture performed at face height 
            if hand['type'] == "Left":
                if fingers == [0,0,0,0,0]: # gesture for alt + f4
                    print("close")
                    print(fingers)
                    p.hotkey('fn','alt','f4')
                    t.sleep(2)
                elif fingers == [0,1,0,0,0]: # gesture for print
                    print("Print")
                    print(fingers)
                    p.hotkey('ctrl','p')
                    t.sleep(1)
                    p.press('enter')
                    t.sleep(1)
                    p.hotkey('winleft','h')
                    t.sleep(6)
                    p.press('enter')
                elif fingers == [0,1,1,0,0]: # gesture for save
                    print("Save")
                    print(fingers)
                    p.hotkey('ctrl','s')
                    t.sleep(1)
                    p.hotkey('winleft','h')
                    t.sleep(6)
                    p.press('enter')
                    t.sleep(1)
                elif fingers == [1,0,0,0,0]: # gesture for sleep
                    print("sleep mode")
                    print(fingers)
                    p.hotkey('winleft')
                    t.sleep(1)
                    # Navigate to the Power button
                    p.press('up')
                    p.press('right')
                    p.press('enter')
                    # Wait for the Power options to appear
                    t.sleep(1)
                    # Select the Shutdown option
                    p.press('down')
                    # p.press('down')
                    p.press('enter')
                    # Wait for the confirmation dialog to appear
                    t.sleep(1)
                    # p.hotkey('winleft','l')
                    # p.moveTo(0,p.size().height)
                    # Click the mouse
                    # p.click()
                    # Lock the screen using the appropriate keyboard shortcut
                    # p.hotkey('winleft', 'l')  # for Windows
                    # pyautogui.hotkey('control', 'shift', 'power')  # for Mac
                elif fingers == [0,1,0,0,1]: # gesture for direct shut down
                    print("Direct Shut Down")
                    print(fingers)
                    p.hotkey('winleft')
                    t.sleep(1)
                    # Navigate to the Power button
                    p.press('up')
                    p.press('right')
                    p.press('enter')
                    # wait for power option
                    t.sleep(1)
                    # Select the Shutdown option
                    p.press('down')
                    p.press('down')
                    p.press('enter')
                
            # Controlling vlc media player
            if hand['type'] == 'Right':
                print(fingers)
                if (fingers == [1,0,0,1,1]) or (fingers == [1,0,0,0,0])  or (fingers == [1,0,0,0,1]):
                    p.press('right') # forward the play (point left hand index finger in right direction)

                elif (fingers == [0,0,0,0,0]):
                    p.press('left') # backward play (left hand thumb in left direct)

                elif (fingers == [0,1,0,0,0]):
                    p.press('up') # volume up (left hand index finger up)
                
                elif (fingers == [0,1,1,0,0]):
                    p.press('down') # volume down (left hand peace sign)

                elif (fingers == [1,1,1,1,1]):
                    p.press('space') # play pause (open left palm)
                    t.sleep(1)
                


    # showing image
    cv.imshow("Image = ",frame)

    key = cv.waitKey(1)
    if key == ord('q'):
        break
