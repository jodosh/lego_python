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

e4_note=659.25
g4_note=392.00
e5_note=659.25
c5_note=523.25
d5_note=587.33
g5_note=783.99

e5_note=659.25
g5_note=783.99
e6_note=1318.51
c6_note=1046.50
d6_note=1174.66
g6_note=1567.98



brick.sound.beep(e5_note,eighth_note,5)
brick.sound.beep(g5_note,eighth_note,5)
brick.sound.beep(e6_note,eighth_note,5)
brick.sound.beep(c6_note,eighth_note,5)
brick.sound.beep(d6_note,eighth_note,5)
brick.sound.beep(g6_note,eighth_note,5)