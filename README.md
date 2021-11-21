# !WORK IN PROGRESS!
It should work as is, but YMMV.

# pico-eink
This module is a basic driver for Waveshare [Pico e-Paper 3.7 display](https://www.waveshare.com/wiki/Pico-ePaper-3.7). It supports grayscale mode and allows setting screen rotation. Drawing routines are compatible with [MicroPython FrameBuffer](https://docs.micropython.org/en/latest/library/framebuf.html) class, which means the same method names and arguments they require.

## Note
**show()** method takes considerably longer for rotations 90 and 270, than 0 and 180 (~7 s vs 80 ms). This is normal and is a result of additional data processing required before sending buffers to the screen in landscape mode. Currently I have no solution to this problem.
