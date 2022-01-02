from Pico_ePaper import Eink
import framebuf
from utime import ticks_ms, ticks_diff

# Import image files
import img.IMG_0182_bw as img1
import img.IMG_0182_bw_d as img2
import img.IMG_0182_gs as img3
import img.IMG_0182_gs_d as img4

epd = Eink(rotation=270)

# Black and white image.
# Load image to temporary framebuffer.
img_tmp = framebuf.FrameBuffer(img1.img_bw, img1.width, img1.height, framebuf.MONO_HLSB)
# Blit image to BW and RED RAM (default).
epd.blit(img_tmp, 0, 0)

# Black and white image with dithering.
img_tmp = framebuf.FrameBuffer(img2.img_bw, img2.width, img2.height, framebuf.MONO_HLSB)
epd.blit(img_tmp, 296, 0)

# Grayscale image.
# Load img_bw to temporary framebuffer.
img_tmp = framebuf.FrameBuffer(img3.img_bw, img3.width, img3.height, framebuf.MONO_HLSB)
# Blit img_bw to BW RAM.
epd.blit(img_tmp, 0, 145, ram=epd.RAM_BW)
# Reuse img_tmp to load img_red.
img_tmp = framebuf.FrameBuffer(img3.img_red, img3.width, img3.height, framebuf.MONO_HLSB)
# And blit it to RED RAM at the same position as previous blit.
epd.blit(img_tmp, 0, 145, ram=epd.RAM_RED)

# Grayscale image with dithering.
img_tmp = framebuf.FrameBuffer(img4.img_bw, img4.width, img4.height, framebuf.MONO_HLSB)
epd.blit(img_tmp, 296, 145, ram=epd.RAM_BW)
img_tmp = framebuf.FrameBuffer(img4.img_red, img4.width, img4.height, framebuf.MONO_HLSB)
epd.blit(img_tmp, 296, 145, ram=epd.RAM_RED)

# Show images and put display controller to sleep.
epd.show()
epd.sleep()

