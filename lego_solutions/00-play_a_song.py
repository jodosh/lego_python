#!/usr/bin/env pybricks-micropython

from pybricks import ev3brick as brick
from pybricks.ev3devices import (Motor, TouchSensor, ColorSensor,
                                 InfraredSensor, UltrasonicSensor, GyroSensor)
from pybricks.parameters import (Port, Stop, Direction, Button, Color,
                                 SoundFile, ImageFile, Align)
from pybricks.tools import print, wait, StopWatch
from pybricks.robotics import DriveBase

# 1-up sound from Mario
quarter_note=266
eighth_note=133

#https://www.ninsheetmusic.org/download/pdf/1945
#http://pages.mtu.edu/~suits/notefreqs.html

notes={
    'c3':130.81,
    'd3':146.83,
    'e3':164.81,
    'f3':174.61,
    'g3':196.00,
    'a3':220.00,
    'b3':246.94,
    'c4':261.63,
    'd4':293.66,
    'e4':329.63,
    'f4':349.23,
    'g4':392.00,
    'a4':440.00,
    'b4':493.88,
    'c5':523.25,
    'd5':587.33,
    'e5':659.25,
    'f5':698.46,
    'g5':783.99,
    'a5':880.00,
    'b5':987.77,
    'c6':1046.50,
    'd6':1174.66,
    'e6':1318.51,
    'f6':1396.91,
    'g6':1567.98,
    'a6':1760.00,
    'b6':1975.53
}

brick.sound.beep(notes['e5'],eighth_note,5)
brick.sound.beep(notes['g5'],eighth_note,5)
brick.sound.beep(notes['e6'],eighth_note,5)
brick.sound.beep(notes['c6'],eighth_note,5)
brick.sound.beep(notes['d6'],eighth_note,5)
brick.sound.beep(notes['g6'],eighth_note,5)