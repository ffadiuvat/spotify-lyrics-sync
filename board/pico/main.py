import sys
from time import sleep

from gpio_lcd import GpioLcd
from machine import Pin

# Create the LCD object
lcd = GpioLcd(rs_pin=Pin(0),
              enable_pin=Pin(1),
              d4_pin=Pin(2),
              d5_pin=Pin(3),
              d6_pin=Pin(4),
              d7_pin=Pin(5),
              num_lines=2, num_columns=16)

max_position = 32
text = 'none_input'
while True:
    input = sys.stdin.readline().strip()
    text = input
    text_len = len(text)
    offset = 0
    i = 0
    while text_len != 0:
        if offset > len(text):
            break
        lcd.clear()
        start_ptr = i+offset
        end_ptr = start_ptr+max_position
        slice = text[i+offset:i+offset+max_position]
        lcd.putstr(slice)
        sleep(1)
        offset += max_position-1
        i+=1

