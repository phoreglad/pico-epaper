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

from machine import Pin
import framebuf
from utime import ticks_ms, ticks_diff, sleep_ms
from ustruct import pack
import gc
import micropython


def profile(func):
    def wrapper(*args, **kwargs):
        gc.collect()
        start_mem = gc.mem_free()
        start_t = ticks_ms()
        func(*args, **kwargs)
        fin_t = ticks_ms()
        fin_mem = gc.mem_free()
        print(f'{func.__name__} took: {ticks_diff(fin_t, start_t)} ms to finish')
        print(f'{func.__name__} used around {start_mem - fin_mem} B of memory')

    return wrapper


class EinkBase:
    black = 0b00
    white = 0b11
    darkgray = 0b01
    lightgray = 0b10

    RAM_BW = 0b01
    RAM_RED = 0b10
    RAM_RBW = 0b11

    def __init__(self, rotation=0, cs_pin=None, dc_pin=None, reset_pin=None, busy_pin=None, use_partial_buffer=False):
        if rotation == 0 or rotation == 180:
            self.width = 280
            self.height = 480
            buf_format = framebuf.MONO_HLSB
            self._horizontal = False
        elif rotation == 90 or rotation == 270:
            self.width = 480
            self.height = 280
            buf_format = framebuf.MONO_VLSB
            self._horizontal = True
        else:
            raise ValueError(
                f"Incorrect rotation selected ({rotation}). Valid values: 0, 90, 180 and 270.")

        self._rotation = rotation

        if reset_pin is None:
            self._rst = Pin(12, Pin.OUT, value=0)
        else:
            self._rst = reset_pin
            self._rst.init(Pin.OUT, value=0)

        if dc_pin is None:
            self._dc = Pin(8, Pin.OUT, value=0)
        else:
            self._dc = dc_pin
            self._dc.init(Pin.OUT, value=0)

        if cs_pin is None:
            self._cs = Pin(9, Pin.OUT, value=1)
        else:
            self._cs = cs_pin
            self._cs.init(Pin.OUT, value=1)

        if busy_pin is None:
            self._busy = Pin(13, Pin.IN, Pin.PULL_UP)
        else:
            self._busy = busy_pin
            self._busy.init(Pin.IN)

        self._luts = {0: EPD_3IN7_lut_4Gray_GC,
                      1: EPD_3IN7_lut_1Gray_GC,
                      2: EPD_3IN7_lut_1Gray_DU,
                      3: EPD_3IN7_lut_1Gray_A2}

        self._buffer_bw_actual = bytearray(self.width * self.height // 8)
        self._buffer_red = bytearray(self.width * self.height // 8)
        self._bw_actual = framebuf.FrameBuffer(self._buffer_bw_actual, self.width, self.height, buf_format)
        self._red = framebuf.FrameBuffer(self._buffer_red, self.width, self.height, buf_format)

        # Don't start in partial mode.
        self._partial = False
        self._use_partial_buffer = use_partial_buffer

        # Use separate buffer for partial updates only if user wants it, use bw buffer otherwise.
        if use_partial_buffer:
            self._buffer_partial = bytearray(self.width * self.height // 8)
            self._part = framebuf.FrameBuffer(self._buffer_partial, self.width, self.height, buf_format)

        # Alias buffer and FrameBuffer to indicate which buffer should be treated as BW RAM buffer.
        self._buffer_bw = self._buffer_bw_actual
        self._bw = self._bw_actual

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
        raise NotImplementedError

    def _send_data(self, data):
        raise NotImplementedError

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

    def reinit(self):
        """Public method for screen reinitialisation."""
        self._init_disp()

    def partial_mode_on(self):
        self._send(0x37, pack("10B", 0x00, 0xff, 0xff, 0xff, 0xff, 0x4f, 0xff, 0xff, 0xff, 0xff))
        self._clear_ram()
        if self._use_partial_buffer:
            self._buffer_bw = self._buffer_partial
            self._bw = self._part
        self._part.fill(1)
        self._partial = True

    def partial_mode_off(self):
        self._send(0x37, pack("10B", 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00, 0x00))
        self._clear_ram()
        if self._use_partial_buffer:
            self._buffer_bw = self._buffer_bw_actual
            self._bw = self._bw_actual
        self._partial = False

    def show(self, lut=0):
        if self._rotation == 0:
            self._set_cursor(0, 0)
        elif self._rotation == 180:
            self._set_cursor(self.width - 1, self.height - 1)
        elif self._rotation == 90:
            self._set_cursor(self.height - 1, 0)
        else:
            self._set_cursor(0, self.width - 1)

    def sleep(self):
        self._send(0x10, 0x03)

    # --------------------------------------------------------
    # Drawing routines (wrappers for FrameBuffer methods).
    # --------------------------------------------------------

    def fill(self, c=white):
        self._bw.fill(c & 1)
        if not self._partial:
            self._red.fill(c >> 1)

    def pixel(self, x, y, c=black):
        self._bw.pixel(x, y, c & 1)
        if not self._partial:
            self._red.pixel(x, y, c >> 1)

    def hline(self, x, y, w, c=black):
        self._bw.hline(x, y, w, c & 1)
        if not self._partial:
            self._red.hline(x, y, w, c >> 1)

    def vline(self, x, y, h, c=black):
        self._bw.vline(x, y, h, c & 1)
        if not self._partial:
            self._red.vline(x, y, h, c >> 1)

    def line(self, x1, y1, x2, y2, c=black):
        self._bw.line(x1, y1, x2, y2, c & 1)
        if not self._partial:
            self._red.line(x1, y1, x2, y2, c >> 1)

    def rect(self, x, y, w, h, c=black, f=False):
        self._bw.rect(x, y, w, h, c & 1, f)
        if not self._partial:
            self._red.rect(x, y, w, h, c >> 1, f)

    def ellipse(self, x, y, xr, yr, c=black, f=False, m=15):
        self._bw.ellipse(x, y, xr, yr, c & 1, f, m)
        if not self._partial:
            self._red.ellipse(x, y, xr, yr, c >> 1, f, m)

    def poly(self, x, y, coords, c=black, f=False):
        self._bw.poly(x, y, coords, c & 1, f)
        if not self._partial:
            self._red.poly(x, y, coords, c >> 1, f)

    def text(self, text, x, y, c=black):
        self._bw.text(text, x, y, c & 1)
        if not self._partial:
            self._red.text(text, x, y, c >> 1)

    def blit(self, fbuf, x, y, key=-1, palette=None, ram=RAM_RBW):
        if ram & 1 == 1 or self._partial:
            self._bw.blit(fbuf, x, y, key, palette)
        if (ram >> 1) & 1 == 1:
            self._red.blit(fbuf, x, y, key, palette)


class Eink(EinkBase):
    from machine import SPI

    def __init__(self, spi=None, *args, **kwargs):
        if spi is None:
            self._spi = self.SPI(1, baudrate=20_000_000)
        else:
            self._spi = spi
        super(Eink, self).__init__(*args, **kwargs)

    def _send_command(self, command):
        self._dc(0)
        self._cs(0)
        if isinstance(command, int):
            self._spi.write(bytes([command]))
        elif isinstance(command, (bytes, bytearray)):
            self._spi.write(command)
        else:
            raise ValueError  # For now
        self._cs(1)

    def _send_data(self, data):
        self._dc(1)
        self._cs(0)
        if isinstance(data, int):
            self._spi.write(bytes([data]))
        elif isinstance(data, (bytes, bytearray)):
            self._spi.write(data)
        else:
            raise ValueError  # For now
        self._cs(1)

    @micropython.viper
    def _reverse_bits(self, num: int) -> int:
        result = 0
        for i in range(8):
            result = (result << 1) | ((num >> i) & 1)
        return result

    def _send_buffer(self, buffer):
        if self._horizontal:
            self._send_data(bytes(map(self._reverse_bits, buffer)))
        else:
            self._send_data(buffer)

    # --------------------------------------------------------
    # Public methods.
    # --------------------------------------------------------

    # @profile
    def show(self, lut=0):
        super().show()

        self._send_command(0x24)
        self._send_buffer(self._buffer_bw)
        if self._partial:
            self._load_LUT(2)
        else:
            self._send_command(0x26)
            self._send_buffer(self._buffer_red)
            self._load_LUT(lut)

        self._send_command(0x20)
        self._read_busy()


class EinkPIO(EinkBase):
    from machine import mem32

    def __init__(self, sm_num=0, dma=5, *args, **kwargs):
        self._sm_num = sm_num
        self._dma = int(dma * 0x40 + 0x50000030)
        self._sm = None
        self._sm_shiftctrl = (0x502000d0 + 0x100000 * (self._sm_num // 4)
                              + 0x18 * (self._sm_num % 4))
        self._dma_write_addr = (0x50200010 + 0x100000 * (self._sm_num // 4)
                                + 0x4 * (self._sm_num % 4))
        dreq = self._sm_num % 4 + 8 * (self._sm_num // 4)
        self._dma_ctrl = dreq << 15 | 1 << 4 | 1
        self._pio_setup()
        super(EinkPIO, self).__init__(*args, **kwargs)

    def _pio_setup(self):
        from rp2 import asm_pio, PIO, StateMachine

        @asm_pio(out_init=PIO.OUT_LOW,
                 sideset_init=PIO.OUT_LOW,
                 autopull=True,
                 pull_thresh=8,
                 out_shiftdir=PIO.SHIFT_LEFT)
        def pio_serial_tx():
            out(pins, 1).side(0)
            nop().side(1)

        self._sm = StateMachine(self._sm_num, pio_serial_tx, freq=40_000_000,
                                sideset_base=Pin(10), out_base=Pin(11))
        self._sm.active(1)

    def _reversed_output(self):
        self.mem32[self._sm_shiftctrl + 0x2000] = 1 << 19

    def _normal_output(self):
        self.mem32[self._sm_shiftctrl + 0x3000] = 1 << 19

    def _send_command(self, command):
        self._dc(0)
        self._cs(0)
        if isinstance(command, int):
            self._sm.put(command, 24)
        elif isinstance(command, (bytes, bytearray)):
            for cmd in command:
                self._sm.put(cmd, 24)
        else:
            raise ValueError
        self._cs(1)

    def _send_data(self, data):
        self._dc(1)
        self._cs(0)
        if isinstance(data, int):
            self._sm.put(data, 24)
        elif isinstance(data, (bytes, bytearray)):
            for cmd in data:
                self._sm.put(cmd, 24)
        else:
            raise ValueError
        self._cs(1)

    @micropython.viper
    def _dma_start(self, buffer):
        dma_ptr = ptr32(self._dma)
        dma_ptr[0] = int(self._dma_ctrl)
        dma_ptr[1] = int(self._dma_write_addr)
        dma_ptr[2] = int(len(buffer))
        dma_ptr[3] = int(ptr32(buffer))

    @micropython.viper
    def _check_dma_busy(self, a: ptr32) -> int:
        return (a[0] >> 24) & 1

    def _send_buffer(self, buffer):
        if self._horizontal:
            self._reversed_output()

        self._dc(1)
        self._cs(0)

        self._dma_start(buffer)
        dma_ctrl = self._dma

        start = ticks_ms()
        while self._check_dma_busy(dma_ctrl) and ticks_diff(ticks_ms(), start) < 5000:
            pass
        self._cs(1)
        if ticks_diff(ticks_ms(), start) >= 5000:
            print('loading data took too long')

        if self._horizontal:
            self._normal_output()

    # --------------------------------------------------------
    # Public methods.
    # --------------------------------------------------------

    # @profile
    def show(self, lut=0):
        super().show()
        self._send_command(0x24)
        self._send_buffer(self._buffer_bw)
        if self._partial:
            self._load_LUT(2)
        else:
            self._send_command(0x26)
            self._send_buffer(self._buffer_red)
            self._load_LUT(lut)

        self._send_command(0x20)
        self._read_busy()


if __name__ == "__main__":
    from uarray import array
    from time import sleep

    epd = EinkPIO(rotation=270, use_partial_buffer=True)
    epd.fill()

    epd.text("test", 10, 10)
    epd.rect(0, 19, 52, 10, epd.lightgray, f=True)
    epd.text("test", 10, 20, epd.darkgray)
    epd.rect(0, 29, 52, 10, epd.darkgray, f=True)
    epd.text("test", 10, 30, epd.lightgray)
    epd.rect(0, 39, 52, 10, f=True)
    epd.text("test", 10, 40, epd.white)
    epd.rect(0, 8, 52, 41)

    epd.hline(5, 60, 50)
    epd.hline(5, 160, 50)
    epd.vline(5, 60, 100)
    epd.vline(55, 60, 100)
    epd.line(5, 60, 55, 160)
    epd.line(55, 60, 5, 160)

    epd.rect(65, 20, 50, 50, f=True)
    epd.rect(65, 70, 50, 50, epd.darkgray, f=True)
    epd.rect(65, 120, 50, 50, epd.lightgray, f=True)
    epd.rect(65, 170, 50, 50, f=True)
    epd.rect(65, 20, 50, 200)

    epd.ellipse(150, 120, 25, 100, epd.lightgray, f=True, m=0b1010)
    epd.ellipse(150, 120, 25, 100, epd.darkgray, f=True, m=0b0101)
    epd.ellipse(150, 120, 25, 25, f=True)
    epd.ellipse(150, 120, 10, 10, epd.white, f=True)

    epd.show()

    epd.sleep()
    sleep(5)
    # To use the screen after putting it to sleep, the reinitialisation is required.
    epd.reinit()
    bestagon = array('h', [0, 0, 50, 0, 75, 43, 50, 86, 0, 86, -25, 43])
    epd.poly(205, 77, bestagon, c=epd.darkgray, f=True)

    epd.show()

    epd.partial_mode_on()

    for i in range(10):
        epd.text(str(i), 10, 200)
        epd.show()
        epd.text(str(i), 10, 200, epd.white)

    epd.partial_mode_off()

    epd.sleep()
