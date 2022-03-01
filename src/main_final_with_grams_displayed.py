from picamera import PiCamera
import time
import sys
import os
from imutils.video import VideoStream
import cv2
import numpy as np
import random
import imutils
import sqlite3
import RPi.GPIO as GPIO
from collections import OrderedDict
from pyzbar import pyzbar
from detectBarcodes import detect
from hx711_folder.hx711 import HX711
from thermalPrinter import printReceipt
import pygame
import subprocess
from pygame.locals import *   # for event MOUSE variables
from proj_Draw_display_grams import *
import copy

help_txt = {0:"start_state", 1:"scan", 2:"add_item_to_list", 3:"weigh", 4:"admin", 5:"edit_list", 6:"pay", 7:"print", 8:"finish"}
state = 0
save_button = 0
start_button = 0
back_to_scan_button = 0
# print_list = OrderedDict([('',''),('',''),('',''),('',''),('','')])
print_list = [['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', '']]
save_print_list = copy.deepcopy(print_list)
save_total_price = 0
checkout_button = 0
pay_done = 0
password = "439929"
quit_button = 0
print_button = 0
decline_pay_button = 0
admin_back_to_scan_button = 0
delete_cur_button = 0
admin_mode = 0
cur_idx = 4
input_pwd = ""
input_done = 0
start_state7 = 0
total_price = 0
#connect sql
conn = sqlite3.connect('itemsDB/itemLibrary.db')
c = conn.cursor()
#init 
vs = VideoStream(src=0).start()
time.sleep(2.0)
#init scale
referenceUnit = 101
hx = HX711(19, 13)
hx.set_reading_format("MSB", "MSB")
hx.set_reference_unit(referenceUnit)
hx.reset()
hx.tare()
threshold = 3
#print("Tare done! Add weight now...")



os.putenv('SDL_VIDEODRIVER', 'fbcon')   # Display on piTFT
os.putenv('SDL_FBDEV', '/dev/fb0')
os.putenv('SDL_MOUSEDRV', 'TSLIB')     # Track mouse clicks on piTFT
os.putenv('SDL_MOUSEDEV', '/dev/input/touchscreen')
WHITE = 255, 255, 255
BLACK = 0,0,0
RED = 255, 0, 0
GREEN = 0, 255, 0
pygame.init()
pygame.mouse.set_visible(False)
screen = pygame.display.set_mode((320,240))
my_font = pygame.font.Font(None,30)
    
#init GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)
def my_callback17 (channel):
    #quit the program
    global quit_button  
    quit_button = 1
    print("quit")
def my_callback22 (channel):
    #enter admin mode
    global admin_mode
    if not admin_mode:
        input_pwd = ""
        admin_mode = 1
def my_callback23 (channel):
    global cur_idx, admin_mode, state
   # print(cur_idx)
    if state == 5:
        if cur_idx == len(print_list) - 1:  #end of the item list, start from the top of the item list
            if len(print_list) != 5:  # if no item in the item list, len(print_list) equals to 5, dont change the cur_idx
                cur_idx = 5  
        else:
            cur_idx += 1
  #  print(cur_idx)
def my_callback27 (channel):
    global admin_mode, state, delete_cur_button
    if state == 5:
        delete_cur_button = 1
        
        
GPIO.add_event_detect(27, GPIO.FALLING, callback = my_callback27, bouncetime = 300)
GPIO.add_event_detect(23, GPIO.FALLING, callback = my_callback23, bouncetime = 300)
GPIO.add_event_detect(22, GPIO.FALLING, callback = my_callback22, bouncetime = 300)
GPIO.add_event_detect(17, GPIO.FALLING, callback = my_callback17, bouncetime = 300)



def getBc():
    global vs
    frame = vs.read()
#    cv2.imshow("Frame", frame)
#     print("waiting for barcodes")
    bc = detect(frame)
#     print("reading barcodes")
    time.sleep(0.1)
    if bc:
        print("got barcodes:", bc)
    return bc

def getWeight():
    global hx, threshold
    val = 0
    while hx.get_weight(5) < threshold:
        time.sleep(0.5)
    time.sleep(1)
    for i in range(3):
        val += hx.get_weight(5)
        print(val)
        hx.power_down()
        hx.power_up()
        time.sleep(0.1)
#     cleanAndExit()
    return val / 3

def recognizeItem(barcode):
    row = c.execute('SELECT * FROM products WHERE barcode = :bc', {'bc':barcode[0]}).fetchall()
    if not row:
        return "","",0,0
    #barcode,item_name,item_price,sold_by_gram = row[0]
    return row[0]
    
def deleteItem(print_list, cur_idx, total_price):
    n_total_price = total_price
    print_list[cur_idx][0] += "(delete)"
    n_total_price -= print_list[cur_idx][1]
    return n_total_price

drawWelcome(pygame,screen,my_font)
pygame.display.flip()



tmp = 1
while not quit_button:
    for event in pygame.event.get():
        if(event.type is MOUSEBUTTONDOWN):
            pos = pygame.mouse.get_pos()
        elif(event.type is MOUSEBUTTONUP):
            pos = pygame.mouse.get_pos()
            x,y = pos
            if state == 4:
                if y >= 40 and y < 80 and x < 106:
                    input_pwd += "1"
                elif y >= 40 and y < 80 and x >= 106 and x < 212:
                    input_pwd += "2"
                elif y >= 40 and y < 80 and x >= 212:
                    input_pwd += "3"
                elif y >= 80 and y < 120 and x < 106:
                    input_pwd += "4"
                elif y >= 80 and y < 120 and x >= 106 and x < 212:
                    input_pwd += "5"
                elif y >= 80 and y < 120 and x >= 212:
                    input_pwd += "6"
                elif y >= 120 and y < 160 and x < 106:
                    input_pwd += "7"
                elif y >= 120 and y < 160 and x >= 106 and x < 212:
                    input_pwd += "8"
                elif y >= 120 and y < 160 and x >= 212:
                    input_pwd += "9"
                elif y >= 160 and y < 200 and x >= 106 and x < 212:
                    input_pwd += "0"
                elif y >= 160 and y < 200 and x < 106:   #press delete
                    input_pwd = input_pwd[:-1]
                elif y >= 160 and y < 200 and x >= 212:  #press done
                    input_done = 1
                elif y > 200:
                    back_to_scan_button = 1
                    
            if y > 200:
                if state == 0:
                    start_button = 1
                elif state == 1 or state == 2 or state == 3:
                    checkout_button = 1
                elif state == 5:
                    if x < 160:
                        #save
                        save_button = 1
                    else:
                        #do not save
                        admin_back_to_scan_button = 1
                elif state == 6:
                    if x < 160:
                        #decline
                        decline_pay_button = 1
                    else:
                        #pay
                        pay_done = 1
                elif state == 7:
                    print_button = 1
    if admin_mode:
        state = 4
        
#     print(help_txt[state])
    
    if state == 0:
        drawWelcome(pygame,screen,my_font)
        pygame.display.flip()
#         print_list = OrderedDict([('',''),('',''),('',''),('',''),('','')])
#         print_list = OrderedDict( [('',''),('',''),('',''),('',''),('',''),('Phone',20.),('Brush',10.),('Phon1',20.),('Brus1',10.),('Phon2',20.)])
        print_list = [['', '', ''], ['', '', ''], ['', '', ''], ['', '', ''], ['', '', '']]
        total_price = 0
        if start_button:
            state = 1
            start_button = 0
    elif state == 1:
        drawScan(pygame,screen,my_font,print_list)
        pygame.display.flip()
        if checkout_button:
            state = 6
            checkout_button = 0
            continue
        barcode = getBc()
        #barcode = "654321"
        if barcode:
            barcode,item_name,item_price,sold_by_gram = recognizeItem(barcode);
            if item_name and sold_by_gram == 0:
                state = 2
            elif item_name:
                state = 3
            else:
                drawInvalid(pygame,screen,my_font)
                pygame.display.flip()
                time.sleep(2)
    elif state == 2:
        print_list.append([item_name, item_price, 1])
#         print_list.append([item_name, tmp])
        total_price += item_price
        tmp += item_price
        cur_idx += 1
#         total_price += item_price
        print(total_price)
        if checkout_button:
            state = 6
            checkout_button = 0
            continue
        time.sleep(1)
        state = 1
    elif state == 3:
        drawWeigh(screen,my_font)
        pygame.display.flip()
        gram = getWeight() / 5
#         print_list[item_name] = item_price * gram
        print_list.append([item_name, item_price * gram, gram])
        total_price += item_price * gram
        cur_idx += 1
        if checkout_button:
            state = 6
            checkout_button = 0
            continue
        state = 1
    elif state == 4:
        drawNumPad(screen,my_font,input_pwd)
        pygame.display.flip()
        if back_to_scan_button:
            state = 1
            input_pwd = ""
            back_to_scan_button = 0
            admin_mode = 0
            continue
#         print("input_done?  " ,input_done)
        time.sleep(0.2)
        if input_done:
            if input_pwd == password:
                save_print_list = copy.deepcopy(print_list)
                save_total_price = total_price
                input_pwd = ""
                state = 5
                input_done = 0
                admin_mode = 0
            else:
                print("into invalid state")
                drawNumPad(screen,my_font,"******")
                pygame.display.flip()
                time.sleep(1)
                input_done = 0
                input_pwd = ""
                print("invalid username or password")
    elif state == 5:
#         print(cur_idx)
        drawAdmin(screen,my_font,print_list[cur_idx])
        pygame.display.flip()
        if delete_cur_button:
            total_price = deleteItem(print_list, cur_idx, total_price)
            print("total_price:", total_price)
            delete_cur_button = 0
        if save_button:
            print("save")
            save_total_price = total_price
            save_print_list = copy.deepcopy(print_list)
            state = 1
            save_button = 0
            continue
        if admin_back_to_scan_button:
            print("decline and back")
            total_price = save_total_price
            print_list = copy.deepcopy(save_print_list)
            state = 1
            admin_back_to_scan_button = 0
    elif state == 6:
        drawCheckOut(pygame,screen,my_font,print_list, total_price)
        pygame.display.flip()
        if decline_pay_button:
            drawDecline(screen,my_font)
            pygame.display.flip()
            time.sleep(3)
            state = 0
            decline_pay_button = 0
            continue
        #pay_done = generate_pay()
        if pay_done:
            pay_done = 0
            state = 7
            start_state7 = time.time()
    elif state == 7:
        drawThank(pygame,screen,my_font)
        pygame.display.flip()
        if print_button:
            drawPrinting(pygame,screen,my_font)
            pygame.display.flip()
            printReceipt(print_list, total_price)
            print("print total price", total_price)
            print_button = 0
            time.sleep(3)
            print("All set")
            state = 0
            continue
        if time.time() - start_state7 >= 10:
            state = 0
 
#stop videostream
vs.stop()
#stop sql
conn.close()
#stop scale
GPIO.cleanup()
sys.exit()
