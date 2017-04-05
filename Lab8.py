"""
 Charlie Ang
 CSC 4800 Python Applications Programming
 Lab # 8 Analog Clock Tkinter Application
 Dr. Tindall
 March 13, 2017

 This is a Python Tkinter GUI application that draws a simple 12-hour analog
 clock with hands in the main window
"""

from tkinter import *
from datetime import datetime
from math import pi, sin, cos

centerX = 300
centerY = 300
lenHourHand = 150   # length of hour hand
lenMinHand = 180    # length of minutes hand
lenSecHand = 180    # length of seconds hand

# Updates the time on the clock
def timeupdate():
    # retrieve current time
    t = datetime.now().time()  # t.hour, t.minute, t.second

    canvas.delete("all")
    createClock()

    # OUTPUTTING HOURS HAND
    fHr = ((t.hour % 12) * 5) + (((t.minute) / 60.0) * 5)
    if(fHr <= 15.0):
        updateAngle = ((15 - fHr) / 15) * (pi / 2.0)
        updateTipX = cos(updateAngle) * lenHourHand
        updateTipY = sin(updateAngle) * lenHourHand
        canvas.create_line(centerX, centerY, centerX+updateTipX, centerY-updateTipY, width=5)  # hours hand
    elif (fHr > 15.0 and fHr <= 30.0):
        updateAngle = ((30 - fHr) / 30) * (pi)
        updateTipX = cos(updateAngle) * lenHourHand
        updateTipY = sin(updateAngle) * lenHourHand
        canvas.create_line(centerX, centerY, centerY+updateTipY, centerX+updateTipX, width=5)  # hours hand
    elif (fHr > 30.0 and fHr <= 45.0):
        updateAngle = ((45 - fHr) / 45) * (1.5 * pi)
        updateTipX = cos(updateAngle) * lenHourHand
        updateTipY = sin(updateAngle) * lenHourHand
        canvas.create_line(centerX, centerY, centerX-updateTipX, centerY+updateTipY, width=5)  # hours hand
    else:
        updateAngle = ((60 - fHr) / 60) * (2.0 * pi)
        updateTipX = cos(updateAngle) * lenHourHand
        updateTipY = sin(updateAngle) * lenHourHand
        canvas.create_line(centerX, centerY, centerY-updateTipY, centerX-updateTipX, width=5)  # hours hand


    # OUTPUTTING MINUTES HAND
    minuteAngle = ((60 - t.minute) / 60) * (2 * pi)
    XM = lenMinHand * sin(minuteAngle)
    YM = lenMinHand * cos(minuteAngle)
    tipXM = centerX - XM
    tipYM = centerY - YM
    canvas.create_line(centerX, centerY, tipXM, tipYM, width=3)

    # OUTPUTTING SECONDS HAND
    secondAngle = ((60 - t.second) / 60) * (2 * pi)
    XS = lenSecHand * sin(secondAngle)
    YS = lenSecHand * cos(secondAngle)
    tipXS = centerX - XS
    tipYS = centerY - YS
    canvas.create_line(centerX, centerY, tipXS, tipYS, width=1, fill="red")

    root.after(500, timeupdate)



def createClock():
    canvas.create_text(300, 20, text="Charlie's Analog Clock", font=('Times', 16))
    canvas.create_oval(100, 100, 500, 500)  # clock face

    # Printing out seconds ticks
    X = 0
    Y = 0
    tipX = 0
    tipY = 0
    for i in range(0, 60):
        angle = ((60 - i) / 60) * (2 * pi)
        X = 190 * sin(angle)
        Y = 190 * cos(angle)
        tipX = centerX - X
        tipY = centerY - Y
        if (i % 5 == 0):
            canvas.create_text(tipX, tipY, text=i, font=('Times', 12))
        else:
            canvas.create_text(tipX, tipY, text=".", font=('Times', 12))

    # Printing out 1 - 12 for minute/hour
    bigX = 0
    bigY = 0
    bigTipX = 0
    bigTipY = 0
    for i in range(1, 13):
        angle = ((12 - i) / 12) * (2 * pi)
        bigX = 220 * sin(angle)
        bigY = 220 * cos(angle)
        bigTipX = centerX - bigX
        bigTipY = centerY - bigY
        canvas.create_text(bigTipX, bigTipY, text=i, font=('Times', 36))

    canvas.create_oval(295, 295, 305, 305, fill="black")  # Center of clock


root = Tk()
# Creating the canvas
canvas = Canvas(root, height=600, width=600)
canvas.pack()

root.after(500, timeupdate)     # wait 500ms then call timeupdate function
mainloop()
