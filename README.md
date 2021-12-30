# !WORK IN PROGRESS!
It should work as is, but YMMV.

# pico-eink
This module is a basic driver for Waveshare [Pico e-Paper 3.7 display](https://www.waveshare.com/wiki/Pico-ePaper-3.7). It supports grayscale mode and allows setting screen rotation. Drawing routines are compatible with [MicroPython FrameBuffer](https://docs.micropython.org/en/latest/library/framebuf.html) class, which means the same method names and arguments they require (**blit()** being a slight exception - see below for details).

## Note
**show()** method takes considerably longer for rotations 90 and 270, than 0 and 180 (~2 s vs 80 ms). This is normal and is a result of additional data processing required before sending buffers to the screen in landscape mode. Currently I have no solution to this problem.

## blit(fbuf, x, y, key=-1, palette=None, ram=RAM_RBW)
**blit()** method takes one additional keyword argument compared to the one found in FrameBuffer class - **ram** - that specifies the target buffer (and consequently RAM) the source will be drawn into. There are three possible values:
1. RAM_BW - black pixels from source will be rendered in light gray on screen.
2. RAM_RED - black pixels from source will be rendered in dark gray on screen.
3. RAM_RBW - black pixels from source will be rendered in black on screen.

(For RAM_BW and RAM_RED respective pixels in the other buffer are assumed to be white.)

