# Demo for using Writer class to render text in fonts not directly supported by FrameBuffer class.

# This example relies on micropython-font-to-py utility and Writer class by Peter Hinch:
# https://github.com/peterhinch/micropython-font-to-py. For details on usage please refer to documentation provided
# in that repository.
# To use this example make sure files writer.py and freesans20.py are present on flash along example file.

from Pico_ePaper import Eink
import framebuf
from writer import Writer

import freesans20

text = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Ut in ligula aliquam, efficitur dui sed," \
       "vulputate nisi. Curabitur rhoncus a est id faucibus. Praesent auctor, nisi vitae ornare commodo," \
       "risus lectus sagittis nibh, in fermentum neque lorem sit amet orci. Aliquam non orci vitae eros " \
       "scelerisque euismod. Mauris sollicitudin mauris in dolor bibendum aliquam. Phasellus laoreet facilisis massa," \
       "eu sollicitudin purus consequat et. Suspendisse dictum sit amet sem nec tempus. Ut placerat tortor diam," \
       "eu faucibus arcu lacinia vel. Nullam id massa eleifend velit venenatis suscipit. Nullam vehicula risus vitae" \
       "turpis convallis dictum. Class aptent taciti sociosqu ad litora torquent per conubia nostra," \
       "per inceptos himenaeos. Aenean vel justo dolor. "


class DummyDevice(framebuf.FrameBuffer):
    def __init__(self, width, height, buf_format):
        self.width = width
        self.height = height
        self._buf = bytearray(self.width * self.height // 8)
        super().__init__(self._buf, self.width, self.height, buf_format)
        self.fill(1)


epd = Eink(rotation=270)

# Create DummyDevice object with the same dimensions as the display.
dummy = DummyDevice(epd.width, epd.height, framebuf.MONO_HLSB)
# Create Writer instance using dummy as device and freesans20 font.
wri = Writer(dummy, freesans20)
# Setup Writer (refer to documentation for details).
Writer.set_textpos(dummy, 0, 0)
wri.set_clip(row_clip=True, col_clip=True, wrap=True)
# Add some text.
wri.printstring(text, invert=True)

# Blit text from dummy device to screen.
# Make sure to use key=1 to add only text,
# otherwise whole screen buffer will be overwritten.
epd.blit(dummy, 0, 0, key=1)
epd.show()
epd.sleep()
