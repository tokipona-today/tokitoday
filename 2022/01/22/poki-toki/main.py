import random
from time import sleep
from machine import Pin, I2C
from ssd1306 import SSD1306_I2C

sda=machine.Pin(0)
scl=machine.Pin(1)
i2c=machine.I2C(0,sda=sda, scl=scl, freq=200000)
oled = SSD1306_I2C(128, 32, i2c)

f = open('toki.csv')
filesize = 16543

def splitLines(nimi, lang):
    s = nimi[lang].strip()
    n = 15
    words = iter(s.split())
    lines, current = [], next(words)
    for word in words:
        if len(current) + 1 + len(word) > n:
            lines.append(current)
            current = word
        else:
            current += " " + word
    lines.append(current)

    for x in range(4):
        lines.append(" ") # just in case
    show(lines)

def show(lines):
    oled.fill(0)
    oled.text(lines[0], 0, 0)
    oled.text(lines[1], 0, 10)
    oled.text(lines[2], 0, 20)
    oled.text(lines[3], 0, 30)
    oled.show()

while True:

    offset = random.randrange(filesize)
    f.seek(offset)
    f.readline()
    random_line = f.readline()
    if len(random_line) == 0:
        f.seek(0)
        random_line = f.readline()
    nimi = random_line.split(";")

    for i in [1,0]:
        splitLines(nimi,i)
        sleep(10)
