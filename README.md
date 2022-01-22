# !WORK IN PROGRESS!
It should work as is, but YMMV.

---

# Pico_ePaper

<div align="center">

![HelloThere](img/hello.jpg)

</div>

This module is a basic driver for Waveshare [Pico e-Paper 3.7 display](https://www.waveshare.com/wiki/Pico-ePaper-3.7).
It supports grayscale mode and allows setting screen rotation. Drawing routines are compatible with
[MicroPython FrameBuffer](https://docs.micropython.org/en/latest/library/framebuf.html) class, which means the same
method names and arguments they require (**blit()** being a slight exception - see below for details).

This branch implements experimental differential (partial) updates support.

---

## Note
**show()** method takes considerably longer for rotations 90 and 270, than 0 and 180 (~700 ms vs 80 ms). This is normal and
is a result of additional data processing required before sending buffers to the screen in landscape mode.
Currently, I have no solution to this problem.

Updates in partial mode are twice as fast as in normal mode.

---
## Constructor
**Eink(rotation=0, spi=None, cs_pin=None, dc_pin=None, reset_pin=None, busy_pin=None)**

Constructor for this class takes multiple optional arguments that allow setting desired rotation as well as custom
SPI and Pin objects.

Accepted values for rotation are: 0, 90, 180 and 270. Supplying unaccepted value will result in an error. The default
value is 0, i.e. screen is horizontal with USB connector facing upwards.

By default, the SPI and Pins setup reflects usage of the e-Paper display as a shield for Raspberry Pi Pico, but the user
can supply custom configuration for use with different boards and microcontrollers (tested with ESP-WROOM-32).

Default pin assignments:

<div align="center">

| Signal      | Pin  |
| :---------- | :--- |
| SCK         | GP10 |
| MOSI        | GP11 |
| CS          | GP9  |
| DC          | GP8  |
| RST (reset) | GP12 |
| BUSY        | GP13 |

</div>

---

## Public methods

### blit(fbuf, x, y, key=-1, palette=None, ram=RAM_RBW)
**blit()** method takes one additional keyword argument compared to the one found in FrameBuffer class - **ram** - that
specifies the target buffer (and consequently RAM) the source will be drawn into. There are three possible values:
1. RAM_BW - black pixels from source will be rendered in light gray on screen.
2. RAM_RED - black pixels from source will be rendered in dark gray on screen.
3. RAM_RBW - black pixels from source will be rendered in black on screen.

(For RAM_BW and RAM_RED respective pixels in the other buffer are assumed to be white.)

---
