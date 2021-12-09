from Pico_ePaper import Eink
import framebuf
from utime import sleep_ms
from machine import RTC


rtc = RTC()

epd = Eink(rotation=0)

epd.text("Black", 28, 10)
epd.fill_rect(0, 19, 96, 10, epd.lightgray)
epd.text("Dark gray", 12, 20, epd.darkgray)
epd.fill_rect(0, 29, 96, 10, epd.darkgray)
epd.text("Light gray", 8, 30, epd.lightgray)
epd.fill_rect(0, 39, 96, 10)
epd.text("White", 28, 40, epd.white)
epd.show()

epd.partial_mode_on()
epd.text("Partial update test:", 60, 70)
epd.show()

for i in range(10):
    epd.fill_rect(108, 90, 172, 100, epd.white)
    time = rtc.datetime()
    epd.text(f"{time[4]:02d}:{time[5]:02d}:{time[6]:02d}", 108, 90)
    epd.show()
    sleep_ms(100)
epd.partial_mode_off()