import pyautogui
from PIL import ImageGrab, Image
from time import sleep
from thecolorapi import color

path = 'C:/Users/User/Downloads/'
pyautogui.hotkey('shift', 'win', 's')
sleep(10)
img = ImageGrab.grabclipboard()
img.save(path + 'color.png', 'PNG')
color_rgb = Image.open(path + 'color.png').convert("RGB").getcolors()
rgb = color_rgb[0][1]
list = []
for i in rgb:
    list.append(int(i))
color = color(rgb=(list[0], list[1], list[2]))
color_name = color.name
print(color_name)
