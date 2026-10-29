"""Firmware globals for running super_mona/ under Pyodide in a browser.

The badge firmware provides badge, screen, image, color, font, vec2, rect,
run and the BUTTON_* constants as builtins, plus a badgeware module. This
module recreates them on top of shim.js and an HTML canvas.
"""

import builtins
import json
import os
import sys
import types

import js
from pyodide.ffi import create_proxy

E = js.SuperMonaShim

LORES = 1
HIRES = 2
VSYNC = 4

BUTTON_UP = 1
BUTTON_DOWN = 2
BUTTON_LEFT = 4
BUTTON_RIGHT = 8
BUTTON_SELECT = 16
BUTTON_BACK = 32
BUTTON_MENU = 64
BUTTON_HOME = 128


class vec2:
    __slots__ = ("x", "y")

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


class rect:
    __slots__ = ("x", "y", "w", "h")

    def __init__(self, x=0, y=0, w=0, h=0):
        self.x = x
        self.y = y
        self.w = w
        self.h = h


class color:
    @staticmethod
    def rgb(r, g, b, a=255):
        return "rgba(%d,%d,%d,%.4f)" % (r, g, b, a / 255)


class font:
    sins = "sins"
    absolute = "absolute"


class _Sheet:
    def __init__(self, img, cols, rows):
        self.img = img
        self.w = img.width // cols
        self.h = img.height // rows

    def sprite(self, col, row):
        return self.img.window(col * self.w, row * self.h, self.w, self.h)


class image:
    OFF = 0
    ON = 1
    X2 = 2
    X4 = 4
    NON_ZERO = 0
    EVEN_ODD = 1

    def __init__(self, width, height, _canvas=None, _ox=0, _oy=0):
        self.width = width
        self.height = height
        self._c = _canvas if _canvas is not None else E.newCanvas(width, height)
        self._ox = _ox
        self._oy = _oy
        self.pen = color.rgb(255, 255, 255)
        self.font = font.sins
        self.antialias = image.OFF
        self.fill_rule = image.NON_ZERO

    @staticmethod
    def load(path):
        c = E.loadedImage(path)
        return image(c.width, c.height, c)

    def window(self, x, y, w, h):
        return image(w, h, self._c, self._ox + x, self._oy + y)

    def spritesheet(self, cols, rows):
        return _Sheet(self, cols, rows)

    def clear(self):
        E.clear(self._c, self.pen, self._ox, self._oy, self.width, self.height)

    def rectangle(self, x, y, w, h):
        E.fillRect(self._c, self.pen, self._ox + x, self._oy + y, w, h)

    def blit(self, src, pos):
        if isinstance(pos, rect):
            w, h = pos.w, pos.h
        else:
            w, h = src.width, src.height
        E.blit(self._c, src._c, src._ox, src._oy, src.width, src.height,
               self._ox + pos.x, self._oy + pos.y, w, h)

    def text(self, msg, x, y):
        E.text(self._c, self.font, self.pen, str(msg), self._ox + x, self._oy + y)

    def measure_text(self, msg):
        return E.measureWidth(self.font, str(msg)), E.fontHeight(self.font)


class _Badge:
    def __init__(self):
        self.ticks = 0
        self.ticks_delta = 0
        self._held = 0
        self._pressed = 0
        self._released = 0

    def mode(self, flags):
        pass

    def held(self, button=None):
        return bool(self._held if button is None else self._held & button)

    def pressed(self, button=None):
        return bool(self._pressed if button is None else self._pressed & button)

    def released(self, button=None):
        return bool(self._released if button is None else self._released & button)


class State:
    @staticmethod
    def load(name, data):
        raw = js.localStorage.getItem("badgeware:" + name)
        if not raw:
            return False
        data.update(json.loads(raw))
        return True

    @staticmethod
    def save(name, data):
        js.localStorage.setItem("badgeware:" + name, json.dumps(data))


badge = _Badge()
screen = image(160, 120, js.document.getElementById("screen"))


def is_dir(path):
    return os.path.isdir(path)


def run(update):
    start = [None, None]

    def tick(now):
        if start[0] is None:
            start[0] = start[1] = now
        badge.ticks = int(now - start[0])
        badge.ticks_delta = int(now - start[1])
        start[1] = now
        E.beginFrame()
        badge._held = E.held
        badge._pressed = E.pressed
        badge._released = E.released
        update()

    E.start(create_proxy(tick))


badgeware = types.ModuleType("badgeware")
badgeware.State = State
sys.modules["badgeware"] = badgeware

for _name, _value in dict(
    badge=badge, screen=screen, image=image, color=color, font=font,
    vec2=vec2, rect=rect, run=run, is_dir=is_dir,
    LORES=LORES, HIRES=HIRES, VSYNC=VSYNC,
    BUTTON_UP=BUTTON_UP, BUTTON_DOWN=BUTTON_DOWN, BUTTON_LEFT=BUTTON_LEFT,
    BUTTON_RIGHT=BUTTON_RIGHT, BUTTON_SELECT=BUTTON_SELECT,
    BUTTON_BACK=BUTTON_BACK, BUTTON_MENU=BUTTON_MENU, BUTTON_HOME=BUTTON_HOME,
).items():
    setattr(builtins, _name, _value)
