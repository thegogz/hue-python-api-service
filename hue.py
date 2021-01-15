#!/usr/bin/python

from phue import Bridge
import utils
from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')

_bridge = Bridge(config.get('bridge', 'ip'))

# If the app is not registered and the button is not pressed, press the button and call connect() (this only needs to be run a single time)
_bridge.connect()

lights = _bridge.get_light_objects('name')
corner_light = lights['Corner Light']


def set_corner_light_to(r, g, b):

    # Turn on the light if off
    corner_light.on = True
    hsv = utils.rgb_to_hsv(r, g, b)

    corner_light.hue = utils.degree_to_value(hsv[0])
    corner_light.saturation = utils.convert_to_255(hsv[1])
    corner_light.brightness = utils.convert_to_255(hsv[2])

def get_corner_light():
    return corner_light