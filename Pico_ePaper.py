# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#
# LUTs have been copied from original example for Waveshare Pico e-Paper 3.7,
# which can be found here:
# https://github.com/waveshare/Pico_ePaper_Code/blob/main/python/Pico-ePaper-3.7.py
#
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


EPD_3IN7_lut_4Gray_GC = bytes([
    0x2A, 0x06, 0x15, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,  # 1
    0x28, 0x06, 0x14, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,  # 2
    0x20, 0x06, 0x10, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,  # 3
    0x14, 0x06, 0x28, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,  # 4
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,  # 5
    0x00, 0x02, 0x02, 0x0A, 0x00, 0x00, 0x00, 0x08, 0x08, 0x02,  # 6
    0x00, 0x02, 0x02, 0x0A, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,  # 7
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,  # 8
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,  # 9
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,  # 10
    0x22, 0x22, 0x22, 0x22, 0x22
])

EPD_3IN7_lut_1Gray_GC = bytes([
    0x2A, 0x05, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,  # 1
    0x05, 0x2A, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,  # 2
    0x2A, 0x15, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,  # 3
    0x05, 0x0A, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,  # 4
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,  # 5
    0x00, 0x02, 0x03, 0x0A, 0x00, 0x02, 0x06, 0x0A, 0x05, 0x00,  # 6
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,  # 7
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,  # 8
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,  # 9
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,  # 10
    0x22, 0x22, 0x22, 0x22, 0x22
])

EPD_3IN7_lut_1Gray_DU = bytes([
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,  # 1
    0x01, 0x2A, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x0A, 0x55, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,  # 3
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,  # 5
    0x00, 0x00, 0x05, 0x05, 0x00, 0x05, 0x03, 0x05, 0x05, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,  # 7
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,  # 9
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,
    0x22, 0x22, 0x22, 0x22, 0x22
])

EPD_3IN7_lut_1Gray_A2 = bytes([
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,  # 1
    0x0A, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,  # 2
    0x05, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,  # 3
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,  # 4
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,  # 5
    0x00, 0x00, 0x03, 0x05, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,  # 6
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,  # 7
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,  # 8
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,  # 9
    0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00,  # 10
    0x22, 0x22, 0x22, 0x22, 0x22
])
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

from machine import Pin, SPI
import framebuf
from utime import ticks_ms, ticks_diff, sleep_ms
from ustruct import pack


REVERSE_LUT = {0: 0, 1: 128, 2: 64, 3: 192, 4: 32, 5: 160, 6: 96, 7: 224, 8: 16, 9: 144, 10: 80, 11: 208, 12: 48,
               13: 176, 14: 112, 15: 240, 16: 8, 17: 136, 18: 72, 19: 200, 20: 40, 21: 168, 22: 104, 23: 232, 24: 24,
               25: 152, 26: 88, 27: 216, 28: 56, 29: 184, 30: 120, 31: 248, 32: 4, 33: 132, 34: 68, 35: 196, 36: 36,
               37: 164, 38: 100, 39: 228, 40: 20, 41: 148, 42: 84, 43: 212, 44: 52, 45: 180, 46: 116, 47: 244, 48: 12,
               49: 140, 50: 76, 51: 204, 52: 44, 53: 172, 54: 108, 55: 236, 56: 28, 57: 156, 58: 92, 59: 220, 60: 60,
               61: 188, 62: 124, 63: 252, 64: 2, 65: 130, 66: 66, 67: 194, 68: 34, 69: 162, 70: 98, 71: 226, 72: 18,
               73: 146, 74: 82, 75: 210, 76: 50, 77: 178, 78: 114, 79: 242, 80: 10, 81: 138, 82: 74, 83: 202, 84: 42,
               85: 170, 86: 106, 87: 234, 88: 26, 89: 154, 90: 90, 91: 218, 92: 58, 93: 186, 94: 122, 95: 250, 96: 6,
               97: 134, 98: 70, 99: 198, 100: 38, 101: 166, 102: 102, 103: 230, 104: 22, 105: 150, 106: 86, 107: 214,
               108: 54, 109: 182, 110: 118, 111: 246, 112: 14, 113: 142, 114: 78, 115: 206, 116: 46, 117: 174, 118: 110,
               119: 238, 120: 30, 121: 158, 122: 94, 123: 222, 124: 62, 125: 190, 126: 126, 127: 254, 128: 1, 129: 129,
               130: 65, 131: 193, 132: 33, 133: 161, 134: 97, 135: 225, 136: 17, 137: 145, 138: 81, 139: 209, 140: 49,
               141: 177, 142: 113, 143: 241, 144: 9, 145: 137, 146: 73, 147: 201, 148: 41, 149: 169, 150: 105, 151: 233,
               152: 25, 153: 153, 154: 89, 155: 217, 156: 57, 157: 185, 158: 121, 159: 249, 160: 5, 161: 133, 162: 69,
               163: 197, 164: 37, 165: 165, 166: 101, 167: 229, 168: 21, 169: 149, 170: 85, 171: 213, 172: 53, 173: 181,
               174: 117, 175: 245, 176: 13, 177: 141, 178: 77, 179: 205, 180: 45, 181: 173, 182: 109, 183: 237, 184: 29,
               185: 157, 186: 93, 187: 221, 188: 61, 189: 189, 190: 125, 191: 253, 192: 3, 193: 131, 194: 67, 195: 195,
               196: 35, 197: 163, 198: 99, 199: 227, 200: 19, 201: 147, 202: 83, 203: 211, 204: 51, 205: 179, 206: 115,
               207: 243, 208: 11, 209: 139, 210: 75, 211: 203, 212: 43, 213: 171, 214: 107, 215: 235, 216: 27, 217: 155,
               218: 91, 219: 219, 220: 59, 221: 187, 222: 123, 223: 251, 224: 7, 225: 135, 226: 71, 227: 199, 228: 39,
               229: 167, 230: 103, 231: 231, 232: 23, 233: 151, 234: 87, 235: 215, 236: 55, 237: 183, 238: 119,
               239: 247, 240: 15, 241: 143, 242: 79, 243: 207, 244: 47, 245: 175, 246: 111, 247: 239, 248: 31, 249: 159,
               250: 95, 251: 223, 252: 63, 253: 191, 254: 127, 255: 255}


class Eink:
    black = 0b00
    white = 0b11
    darkgray = 0b01
    lightgray = 0b10

    RAM_BW = 0b01
    RAM_RED = 0b10
    RAM_RBW = 0b11

    def __init__(self, rotation=0):
        if rotation == 0 or rotation == 180:
            self.width = 280
            self.height = 480
            buf_format = framebuf.MONO_HLSB
        elif rotation == 90 or rotation == 270:
            self.width = 480
            self.height = 280
            buf_format = framebuf.MONO_VLSB
        else:
            raise ValueError(f"Incorrect rotation selected ({rotation}). Valid values: 0, 90, 180 and 270.")

        self._rotation = rotation

        self._spi = SPI(1)
        self._spi.init(baudrate=4_000_000)

        self._rst = Pin(12, Pin.OUT, value=0)
        self._dc = Pin(8, Pin.OUT, value=0)
        self._cs = Pin(9, Pin.OUT, value=1)
        self._busy = Pin(13, Pin.IN, Pin.PULL_UP)

        self._luts = {0: EPD_3IN7_lut_4Gray_GC,
                      1: EPD_3IN7_lut_1Gray_GC,
                      2: EPD_3IN7_lut_1Gray_DU,
                      3: EPD_3IN7_lut_1Gray_A2}

        self._buffer_bw = bytearray(self.width * self.height // 8)
        self._buffer_red = bytearray(self.width * self.height // 8)
        self._bw = framebuf.FrameBuffer(self._buffer_bw, self.width, self.height, buf_format)
        self._red = framebuf.FrameBuffer(self._buffer_red, self.width, self.height, buf_format)

        self.fill()

        self._init_disp()
        sleep_ms(500)

    def _reset(self):
        self._rst(1)
        sleep_ms(30)
        self._rst(0)
        sleep_ms(3)
        self._rst(1)
        sleep_ms(30)

    def _send_command(self, command):
        self._dc(0)
        self._cs(0)
        if isinstance(command, int):
            self._spi.write(bytes([command]))
        elif isinstance(command, bytearray) or isinstance(command, bytes):
            self._spi.write(command)
        else:
            raise ValueError  # For now
        self._cs(1)

    def _send_data(self, data):
        self._dc(1)
        self._cs(0)
        if isinstance(data, int):
            self._spi.write(bytes([data]))
        elif isinstance(data, bytearray) or isinstance(data, bytes):
            self._spi.write(data)
        else:
            raise ValueError  # For now
        self._cs(1)

    def _send(self, command, data):
        self._send_command(command)
        self._send_data(data)

    def _read_busy(self):
        while self._busy.value() == 1:
            sleep_ms(10)
        sleep_ms(200)

    def _load_LUT(self, lut=0):
        self._send(0x32, self._luts[lut])

    def _set_cursor(self, x, y):
        self._send(0x4e, pack("h", x))
        self._send(0x4f, pack("h", y))

    def _set_window(self, start_x, end_x, start_y, end_y):
        self._send(0x44, pack("2h", start_x, end_x))
        self._send(0x45, pack("2h", start_y, end_y))

    def _clear_ram(self, bw=True, red=True):
        if red:
            self._send(0x46, 0xf7)
            self._read_busy()
        if bw:
            self._send(0x47, 0xf7)
            self._read_busy()

    def _init_disp(self):
        # HW reset.
        self._reset()

        # SW reset.
        self._send_command(0x12)
        sleep_ms(300)

        # Clear BW and RED RAMs.
        self._clear_ram()

        # Set gate number.
        self._send(0x01, pack("hB", 479, 0))

        # Set gate voltage.
        self._send(0x03, 0x00)

        # Set source voltage.
        self._send(0x04, pack("3B", 0x41, 0xa8, 0x32))

        # Set Data Entry mode.
        if self._rotation == 0:
            seq = 0x03
        elif self._rotation == 180:
            seq = 0x00
        elif self._rotation == 90:
            seq = 0x06
        elif self._rotation == 270:
            seq = 0x05
        else:
            raise ValueError(f"Incorrect rotation selected")

        self._send(0x11, seq)

        # Set border.
        self._send(0x3c, 0x03)

        # Booster Soft-start Control.
        self._send(0x0c, pack("5B", 0xae, 0xc7, 0xc3, 0xc0, 0xc0))

        # Internal sensor on.
        self._send(0x18, 0x80)

        # Set VCOM.
        self._send(0x2c, 0x44)

        # Set window.
        if self._rotation == 0:
            self._set_window(0, self.width - 1, 0, self.height - 1)
        elif self._rotation == 180:
            self._set_window(self.width - 1, 0, self.height - 1, 0)
        elif self._rotation == 90:
            self._set_window(self.height - 1, 0, 0, self.width - 1)
        elif self._rotation == 270:
            self._set_window(0, self.height - 1, self.width - 1, 0)
        else:
            raise ValueError(f"Incorrect rotation selected")

        # Set Display Update Control 2
        self._send(0x22, 0xcf)

    # --------------------------------------------------------
    # Public methods.
    # --------------------------------------------------------   

    def show(self, lut=0):
        start = ticks_ms()  # Testing only.
        if self._rotation == 0:
            self._set_cursor(0, 0)
        elif self._rotation == 180:
            self._set_cursor(self.width - 1, self.height - 1)
        elif self._rotation == 90:
            self._set_cursor(self.height - 1, 0)
        elif self._rotation == 270:
            self._set_cursor(0, self.width - 1)
        else:
            raise ValueError(f"Incorrect rotation selected")

        # Load BW buffer to BW RAM.
        self._send_command(0x24)
        self._dc(1)
        self._cs(0)
        if self._rotation == 0 or self._rotation == 180:
            self._spi.write(self._buffer_bw)
        else:
            for i in self._buffer_bw:
                self._spi.write(bytes([REVERSE_LUT[i]]))
        self._cs(1)

        # Load RED buffer to RED RAM.
        self._send_command(0x26)
        self._dc(1)
        self._cs(0)
        if self._rotation == 0 or self._rotation == 180:
            self._spi.write(self._buffer_red)
        else:
            for i in self._buffer_red:
                self._spi.write(bytes([REVERSE_LUT[i]]))
        self._cs(1)

        print(f"Data loading time: {ticks_diff(ticks_ms(), start)} ms")

        self._load_LUT(lut)
        self._send_command(0x20)
        self._read_busy()

    def sleep(self):
        self._send(0x10, 0x03)

    # --------------------------------------------------------
    # Drawing routines (wrappers for FrameBuffer methods).
    # -------------------------------------------------------- 

    def fill(self, c=white):
        self._bw.fill(c & 1)
        self._red.fill(c >> 1)

    def pixel(self, text, x, y, c=black):
        self._bw.pixel(x, y, c & 1)
        self._red.pixel(x, y, c >> 1)

    def hline(self, x, y, w, c=black):
        self._bw.hline(x, y, w, c & 1)
        self._red.hline(x, y, w, c >> 1)

    def vline(self, x, y, h, c=black):
        self._bw.vline(x, y, h, c & 1)
        self._red.vline(x, y, h, c >> 1)

    def line(self, x1, y1, x2, y2, c=black):
        self._bw.line(x1, y1, x2, y2, c & 1)
        self._red.line(x1, y1, x2, y2, c >> 1)

    def rect(self, x, y, w, h, c=black):
        self._bw.rect(x, y, w, h, c & 1)
        self._red.rect(x, y, w, h, c >> 1)

    def fill_rect(self, x, y, w, h, c=black):
        self._bw.fill_rect(x, y, w, h, c & 1)
        self._red.fill_rect(x, y, w, h, c >> 1)

    def text(self, text, x, y, colour=black):
        self._bw.text(text, x, y, colour & 1)
        self._red.text(text, x, y, colour >> 1)

    def blit(self, fbuf, x, y, key=-1, palette=None, ram=RAM_RBW):
        if ram & 1 == 1:
            self._bw.blit(fbuf, x, y, key, palette)
        if (ram >> 1) & 1 == 1:
            self._red.blit(fbuf, x, y, key, palette)


if __name__ == "__main__":
    epd = Eink(rotation=270)
    epd.fill()

    epd.text("test", 10, 10)
    epd.fill_rect(0, 19, 52, 10, epd.lightgray)
    epd.text("test", 10, 20, epd.darkgray)
    epd.fill_rect(0, 29, 52, 10, epd.darkgray)
    epd.text("test", 10, 30, epd.lightgray)
    epd.fill_rect(0, 39, 52, 10)
    epd.text("test", 10, 40, epd.white)
    epd.rect(0, 8, 52, 41)

    epd.hline(5, 60, 50)
    epd.hline(5, 160, 50)
    epd.vline(5, 60, 100)
    epd.vline(55, 60, 100)
    epd.line(5, 60, 55, 160)
    epd.line(55, 60, 5, 160)
    epd.show()

    sleep_ms(5000)

    epd.fill_rect(100, 20, 50, 50)
    epd.fill_rect(100, 70, 50, 50, epd.darkgray)
    epd.fill_rect(100, 120, 50, 50, epd.lightgray)
    epd.fill_rect(100, 170, 50, 50)
    epd.rect(100, 20, 50, 200)
    epd.show()

    epd.sleep()
