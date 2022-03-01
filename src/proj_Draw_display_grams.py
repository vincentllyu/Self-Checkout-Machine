import pygame
from collections import OrderedDict
import time
import os
import subprocess
from pygame.locals import *   # for event MOUSE variables

# 320*240
#state1
def drawWelcome(pygame,screen,my_font):
    screen.fill((0,0,0))
    welcome_surface = my_font.render("Welcom to Vincent's Shop",True, (255,255,255))
    welcome_rect = welcome_surface.get_rect(center = (160,60))

    pygame.draw.rect(screen,(255,0,0),(0,200,320,40))
    start_surface = my_font.render('start', True, (255,255,255))
    start_rect = start_surface.get_rect(center=(160,220))

    screen.blit(welcome_surface,welcome_rect)
    screen.blit(start_surface,start_rect)

#state2
def drawScan(pygame,screen,my_font,items):
    screen.fill((0,0,0))
    left_text_surface = my_font.render('Item', True, (255,255,255))
    left_text_rect = left_text_surface.get_rect(center=(60,60))
    right_text_surface = my_font.render('Price', True, (255,255,255))
    right_text_rect = right_text_surface.get_rect(center=(210,60))
    
    unit_text_surface = my_font.render('Unit', True, (255,255,255))
    unit_text_rect = right_text_surface.get_rect(center=(300,60))

    pygame.draw.rect(screen,(0,255,0),(0,200,320,40))
    co_surface = my_font.render('Check Out', True, (255,255,255))
    co_rect = co_surface.get_rect(center=(160,220))
    screen.blit(left_text_surface,left_text_rect)
    screen.blit(right_text_surface,right_text_rect)
    screen.blit(unit_text_surface,unit_text_rect)
    screen.blit(co_surface,co_rect)

    
    for i in range(len(items)):
        k_surface = my_font.render(items[i-5][0], True, (255,255,255))
        k_rect      = k_surface.get_rect(center = (60,70+(i+1)*20))

        if items[i-5][1] == '':
            itemP = ''
        else:
            itemP = "{:.2f}".format(float(items[i-5][1]))
                                    
        p_surface = my_font.render((itemP), True, (255,255,255))
        p_rect      = p_surface.get_rect(center = (210,70+(i+1)*20))
        
        u_surface = my_font.render(str(items[i-5][2]), True, (255,255,255))
        u_rect      = p_surface.get_rect(center = (300,70+(i+1)*20))

        screen.blit(k_surface,k_rect)
        screen.blit(p_surface,p_rect)
        screen.blit(u_surface,u_rect)
        if i == 5:
            break

#state3
def drawWeigh(screen,my_font):
    screen.fill((0,0,0))
    welcome_surface = my_font.render("This item needs weighing",True, (255,255,255))
    welcome_rect      = welcome_surface.get_rect(center = (160,60))
 
    scan_surface = my_font.render("Please put item on the scale", True, (255,255,255))
    scan_rect       = scan_surface.get_rect(center = (160,150))

    scan_surface1 = my_font.render("for 2 seconds", True, (255,255,255))
    scan_rect1       = scan_surface1.get_rect(center = (160,170))
    
    screen.blit(welcome_surface,welcome_rect)
    screen.blit(scan_surface,scan_rect)
    screen.blit(scan_surface1,scan_rect1)

#state4
def drawNumPad(screen,my_font,cur_pw):
    screen.fill((0,0,0))

    pw_surface = my_font.render("{:^}".format(str(cur_pw)),True, (255,255,255))
    pw_rect      = pw_surface.get_rect(center = (160,30))
    
    welcome_surface = my_font.render("1{: <15}2{: <15}3".format('',''),True, (255,255,255))
    welcome_rect      = welcome_surface.get_rect(center = (160,60))
 
    scan_surface = my_font.render("4{: <15}5{: <15}6".format('',''), True, (255,255,255))
    scan_rect       = scan_surface.get_rect(center = (160,100))

    scan_surface1 = my_font.render("7{: <15}8{: <15}9".format('',''), True, (255,255,255))
    scan_rect1       = scan_surface1.get_rect(center = (160,140))
    
    scan_surface2 = my_font.render("Del{: <14}0{: <11}Done".format('',''), True, (255,255,255))
    scan_rect2       = scan_surface2.get_rect(center = (160,180))

    pygame.draw.rect(screen,(255,0,0),(0,200,320,40))
    co_surface = my_font.render('Back', True, (255,255,255))
    co_rect = co_surface.get_rect(center=(160,220))

    screen.blit(pw_surface,pw_rect)
    screen.blit(welcome_surface,welcome_rect)
    screen.blit(scan_surface,scan_rect)
    screen.blit(scan_surface1,scan_rect1)
    screen.blit(scan_surface2,scan_rect2)
    screen.blit(co_surface,co_rect)

#state5
def drawAdmin(screen,my_font,cur_item):
    screen.fill((0,0,0))
    
    pygame.draw.rect(screen,(0,255,0),(0,200,160,40))
    save_surface = my_font.render('Save', True, (255,255,255))
    save_rect = save_surface.get_rect(center=(80,220))

    pygame.draw.rect(screen,(255,0,0),(160,200,160,40))
    back_surface = my_font.render('Back', True, (255,255,255))
    back_rect = back_surface.get_rect(center=(240,220))

    item_surface = my_font.render("{: <15}{: >10}".format(str(cur_item[0]),str(cur_item[1])),True, (255,255,255))
    item_rect      = item_surface.get_rect(center = (160,140))

    pw_surface = my_font.render("{:^}".format('Delete this item?'),True, (255,255,255))
    pw_rect      = pw_surface.get_rect(center = (160,40))

    pw1_surface = my_font.render("{:^}".format('Use button 23 to confirm'),True, (255,255,255))
    pw1_rect      = pw1_surface.get_rect(center = (160,60))
    screen.blit(pw1_surface,pw1_rect)
    
    pw1_surface = my_font.render("{:^}".format('Use button 27 to roll down'),True, (255,255,255))
    pw1_rect      = pw1_surface.get_rect(center = (160,80))
    
    screen.blit(save_surface,save_rect)
    screen.blit(back_surface,back_rect)
    screen.blit(item_surface,item_rect)
    screen.blit(pw_surface,pw_rect)
    screen.blit(pw1_surface,pw1_rect)
    

#state6
def drawCheckOut(pygame,screen,my_font,items, tot):
    screen.fill((0,0,0))
    
    pygame.draw.rect(screen,(0,255,0),(0,200,160,40))
    save_surface = my_font.render('Pay', True, (255,255,255))
    save_rect = save_surface.get_rect(center=(240,220))

    pygame.draw.rect(screen,(255,0,0),(160,200,160,40))
    back_surface = my_font.render('Decline', True, (255,255,255))
    back_rect = back_surface.get_rect(center=(80,220))

    pw1_surface = my_font.render("Your total is {:.2f}".format(tot),True, (255,255,255))
    pw1_rect      = pw1_surface.get_rect(center = (160,60))
    screen.blit(save_surface,save_rect)
    screen.blit(back_surface,back_rect)
    screen.blit(pw1_surface,pw1_rect)

#state7
def drawThank(pygame,screen,my_font):
    screen.fill((0,0,0))

    welcome_surface = my_font.render("See you next time!",True, (255,255,255))
    welcome_rect      = welcome_surface.get_rect(center = (160,60))
    
#     scan_surface = my_font.render("Print Reciept", True, (255,255,255))
#     scan_rect       = scan_surface.get_rect(center = (160,180))
    
    pygame.draw.rect(screen,(255,0,0),(0,200,320,40))
    recei_surface = my_font.render('Print Reciept', True, (255,255,255))
    recei_rect = recei_surface.get_rect(center=(160,220))
    
    screen.blit(welcome_surface,welcome_rect)
    screen.blit(recei_surface,recei_rect)
    

#state8
def drawPrinting(pygame,screen,my_font):
    screen.fill((0,0,0))
    welcome_surface = my_font.render("Receipt Printing...",True, (255,255,255))
    welcome_rect      = welcome_surface.get_rect(center = (160,60))
    
    screen.blit(welcome_surface,welcome_rect)
    
    
def drawInvalid(pygame,screen,my_font):
    screen.fill((0,0,0))
    welcome_surface = my_font.render("Invalid Item... Scan Again",True, (255,255,255))
    welcome_rect      = welcome_surface.get_rect(center = (160,60))
    screen.blit(welcome_surface,welcome_rect)
    
#state9
def drawDecline(screen,my_font):
    screen.fill((0,0,0))

    welcome_surface = my_font.render("Paymeny Declined",True, (255,255,255))
    welcome_rect      = welcome_surface.get_rect(center = (160,60))

    welcome1_surface = my_font.render("Returning to home screen...",True, (255,255,255))
    welcome1_rect      = welcome1_surface.get_rect(center = (160,140))

    screen.blit(welcome_surface,welcome_rect)
    screen.blit(welcome1_surface,welcome1_rect)

if __name__ == "__main__":
#     os.putenv('SDL_VIDEODRIVER', 'fbcon')   # Display on piTFT
#     os.putenv('SDL_FBDEV', '/dev/fb1')
#     os.putenv('SDL_MOUSEDRV', 'TSLIB')     # Track mouse clicks on piTFT
#     os.putenv('SDL_MOUSEDEV', '/dev/input/touchscreen')
    WHITE = 255, 255, 255
    BLACK = 0,0,0
    RED = 255, 0, 0
    GREEN = 0, 255, 0
    pygame.init()
    pygame.mouse.set_visible(True)
    screen = pygame.display.set_mode((320,240))
    my_font = pygame.font.Font(None,30)
    
##    drawWelcome(pygame,screen,my_font)
    printList =[['','',''],['','',''],['','',''],['','',''],['','',''],['Phone',20.0,1],['Brush',10.0,1],['Apple',58.2,11.64],['RPi',34.99,1],['Grape',66.0,22.0]]

##    drawScan(pygame,screen,my_font,printList)
##
##    drawWeigh(screen,my_font)
##    
##    drawNumPad(screen,my_font,439929)
    
##    cur_item = ['Phone',20,1]
##    drawAdmin(screen,my_font,cur_item)
##
##    drawCheckOut(pygame,screen,my_font,printList,166.00)
##
##    drawThank(pygame,screen,my_font)
##
##    drawDecline(screen,my_font)
    
##    drawInvalid(pygame,screen,my_font)

    drawPrinting(pygame,screen,my_font)
    
    pygame.display.flip()

    
