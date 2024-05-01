import os
import psutil
import socket
import time
import subprocess
import signal
import sys
from luma.core.interface.serial import i2c
from luma.oled.device import ssd1306
from PIL import Image, ImageDraw, ImageFont

# Setup OLED display
serial = i2c(port=1, address=0x3C)
disp = ssd1306(serial, rotate=0)

# Load font
#font = ImageFont.truetype('PixelOperator.ttf', 16)
font = ImageFont.load_default()

# Function to handle shutdown signal
def handle_shutdown(signum, frame):
    # Clear the OLED display
    device.clear()
    device.hide()
    sys.exit(0)

# Register the signal handler for SIGTERM (shutdown signal)
signal.signal(signal.SIGTERM, handle_shutdown)

# Create blank image for drawing
width = disp.width
height = disp.height
image = Image.new("1", (width, height))
draw = ImageDraw.Draw(image)

while True:

    # Draw a black filled box to clear the image.
    draw.rectangle((0, 0, width, height), outline=0, fill=0)

    # Shell scripts for system monitoring from here : https://unix.stackexchange.com/questions/119126/command-to-display-memory-usage-disk-usage-and-cpu-load
    cmd = "hostname -I | cut -d\' \' -f1"
    IP = subprocess.check_output(cmd, shell = True )
    cmd = "top -bn1 | grep load | awk '{printf \"CPU: %.2f\", $(NF-2)}'"
    CPU = subprocess.check_output(cmd, shell = True )
    cmd = "free -m | awk 'NR==2{printf \"Mem: %s/%sMB %.0f%%\", $3,$2,$3*100/$2 }'"
    MemUsage = subprocess.check_output(cmd, shell = True )
    cmd = "df -h | grep '/dev/md0' | awk '{printf \"Disk: %s/%s %s\", $3,$2,$5}'"
    # exchange /dev/md0 with your path and disk you want to monitor 
    Disk = subprocess.check_output(cmd, shell = True )
    cmd = "vcgencmd measure_temp |cut -f 2 -d '='"
    Temp = subprocess.check_output(cmd, shell = True )

    # Pi Stats Display
    draw.text((0, 0), "IP: " + str(IP,'utf-8'), font=font, fill=255)
    draw.text((0, 18), str(CPU,'utf-8') + "%", font=font, fill=255)
    draw.text((80, 18), str(Temp,'utf-8') , font=font, fill=255)
    draw.text((0, 36), str(MemUsage,'utf-8'), font=font, fill=255)
    draw.text((0, 54), str(Disk,'utf-8'), font=font, fill=255)
  
    # Display image
    disp.display(image)
    time.sleep(2)
