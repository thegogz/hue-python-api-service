#!/usr/bin/python

from phue import Bridge
import math

_bridge = Bridge('192.168.0.81')

# If the app is not registered and the button is not pressed, press the button and call connect() (this only needs to be run a single time)
_bridge.connect()

lights = _bridge.get_light_objects('name')
corner_light = lights['Corner Light']


def rgb_to_hsv(r, g, b):
    r, g, b = r/255.0, g/255.0, b/255.0
    mx = max(r, g, b)
    mn = min(r, g, b)
    df = mx-mn
    h = 0
    if mx == mn:
        h = 0
    elif mx == r:
        h = (60 * ((g-b)/df) + 360) % 360
    elif mx == g:
        h = (60 * ((b-r)/df) + 120) % 360
    elif mx == b:
        h = (60 * ((r-g)/df) + 240) % 360
    if mx == 0:
        s = 0
    else:
        s = (df/mx)
    v = mx
    return h, s, v

def degree_to_value(degree):
    return degree * (65535/360)

def convert_to_255(value):
    return math.floor(value * 255)

def set_corner_light_to(r, g, b):

    # Turn on the light if off
    corner_light.on = True
    hsv = rgb_to_hsv(r, g, b)

    corner_light.hue = degree_to_value(hsv[0])
    corner_light.saturation = convert_to_255(hsv[1])
    corner_light.brightness = convert_to_255(hsv[2])

def get_corner_light():
    return corner_light