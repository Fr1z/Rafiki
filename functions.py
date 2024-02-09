from inputVars import *
import argparse
import dearpygui.dearpygui as dpg
from PIL import ImageGrab
import math


def toggle_layer1(sender):
    show_value = dpg.get_value(sender)
    dpg.configure_item("planet 1, moon node", show=show_value)
    dpg.configure_item("moon1 orbit", show=show_value)

def stepAngles():
    global planet1_angle, planet1_rev_speed, planet1_moon1angle, planet1_moon1_rev_speed

    planet1_angle += planet1_rev_speed
    if planet1_angle > 360 : planet1_angle -= 360
    planet1_moon1angle += planet1_moon1_rev_speed
    if planet1_moon1angle > 360 : planet1_moon1angle -= 360

    return {'p1': planet1_angle, 'm1': planet1_moon1angle}

def screenShot(sender):
        return
        """with sdpg.window("Main Window"):
            dpg.set_main_window_size(800, 800)
            dpg.set_main_window_title("Pixel selector")

            dpg.add_drawing('drawing', width=400, height=350)

            img = ImageGrab.grab(bbox=[0, 0, 100, 100])

            dpg_image = []
            for i in range(0, img.height):
                for j in range(0, img.width):
                    pixel = img.getpixel((j, i))
                    dpg_image.append(pixel[0])
                    dpg_image.append(pixel[1])
                    dpg_image.append(pixel[2])
                    dpg_image.append(255)

            # something like this would be great
            dpg.add_texture("texture id", dpg_image, img.width, img.height)
            dpg.draw_image('drawing', "texture id", [0, 0], [100, 100]) """
