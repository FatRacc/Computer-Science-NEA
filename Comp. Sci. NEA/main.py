#pip3 install pygame -pre
#redo tasks 1-5 of the NEA to ensure continuity.
#https://www.aqa.org.uk/subjects/computer-science-and-it/as-and-a-level/computer-science-7516-7517/subject-content-a-level/non-exam-assessment-the-computing-practical-project


#===============================================================================
#Modules being imported
#===============================================================================
import pygame
from pygame.locals import *
import sys
import tkinter
from tkinter import messagebox
from tkinter.simpledialog import askstring
from tkinter import *
from tkinter import Tk, Label
from button import Button
import sqlite3
import os
import time
import random
import math
import re
import time

#===============================================================================
#parameters
#===============================================================================
pygame.init() #initialising pygame 

fps = 60
fpsClock = pygame.time.Clock()
screen = pygame.display.set_mode((1280, 720))
color = (255,255,255)
colorLight = (170,170,170)
colorDark = (100,100,100)
smallfont = pygame.font.SysFont('Corbel',35)
clock = pygame.time.Clock()
run = True
x_1 = 20
y_1 = 20
width = 40
height = 60
vel = 2.87
ALPHA = (0, 255, 0)


#===============================================================================
#display the background image
#===============================================================================
def backgroundDisplay():
    imp = pygame.image.load("assets/Background.png").convert() #loads the image

    screen.blit(imp, (0, 0)) #sets the position of the image
    pygame.display.flip()
    status = True
    while (status): #checks if the game has been closed
        for i in pygame.event.get():
            if i.type == pygame.QUIT:
                status = False





#===============================================================================
# main menu
#===============================================================================
BG = pygame.image.load("assets/Background.jpg")




def get_font(size): # Returns Press-Start-2P in the desired size
  return pygame.font.Font("assets/font.ttf", size)




def play():
    player_render()



def options():
  while True:
      OPTIONS_MOUSE_POS = pygame.mouse.get_pos()




      screen.fill("white")




      OPTIONS_TEXT = get_font(45).render("This is the OPTIONS screen.", True, "Black")
      OPTIONS_RECT = OPTIONS_TEXT.get_rect(center=(640, 260))
      screen.blit(OPTIONS_TEXT, OPTIONS_RECT)




      OPTIONS_BACK = Button(image=None, pos=(640, 460),
                          text_input="BACK", font=get_font(75), base_color="Black", hovering_color="Green")




      OPTIONS_BACK.changeColor(OPTIONS_MOUSE_POS)
      OPTIONS_BACK.update(screen)




      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              pygame.quit()
              sys.exit()
          if event.type == pygame.MOUSEBUTTONDOWN:
              if OPTIONS_BACK.checkForInput(OPTIONS_MOUSE_POS):
                  main_menu()




      pygame.display.update()




def main_menu():
  while True:
      screen.blit(BG, (0, 0))




      MENU_MOUSE_POS = pygame.mouse.get_pos()




      MENU_TEXT = get_font(100).render("FACTORY GAME", True, "#b68f40")
      MENU_RECT = MENU_TEXT.get_rect(center=(675, 100))




      PLAY_BUTTON = Button(image=pygame.image.load("assets/Play Rect.png"), pos=(640, 250),
                          text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
      OPTIONS_BUTTON = Button(image=pygame.image.load("assets/Options Rect.png"), pos=(640, 400),
                          text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
      QUIT_BUTTON = Button(image=pygame.image.load("assets/Quit Rect.png"), pos=(640, 550),
                          text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")




      screen.blit(MENU_TEXT, MENU_RECT)




      for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
          button.changeColor(MENU_MOUSE_POS)
          button.update(screen)
    
      for event in pygame.event.get():
          if event.type == pygame.QUIT:
              pygame.quit()
              sys.exit()
          if event.type == pygame.MOUSEBUTTONDOWN:
              if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                  play()
              if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                  options()
              if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                  pygame.quit()
                  sys.exit()




      pygame.display.update()




#===============================================================================
#charchter render and movement
#===============================================================================
def player_render():
    time.sleep(0.1)
    x, y = 0, 0  #sets charchter position
    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  #checks if the program is quit
                run = False

        keys = pygame.key.get_pressed() #checks the keys being pressed 
        
        if keys[pygame.K_a]:
            x -= vel  #player velocity set
            camera_follow()
            print("left")

        if keys[pygame.K_d]:
            x += vel #player velocity set
            camera_follow()
            print("right")

        if keys[pygame.K_w]:
            y -= vel #player velocity set
            camera_follow()
            print("up")

        if keys[pygame.K_s]:
            y += vel #player velocity set
            camera_follow()
            print("down")

        if keys[pygame.K_ESCAPE]:
            print("returned to main menu") #returns to the main menu
            main_menu()

        left, middle, right = pygame.mouse.get_pressed()
        if left:
            time.sleep(0.3)
            buildingPlacement() #allows factory building to be placed
        if right:
            time.sleep(0.3)
            beltPlacement() #allows belt to be placed

        

        checkered_background()
        charachter = pygame.image.load(os.path.join("assets", "SPRITE1.PNG"))
        screen.blit(charachter, (x, y)) #displays the image of the player
        mainPlayerInventory(playerInventory) #initialises the player inventory
        pygame.display.flip()
        #camera_follow()

#===============================================================================
#tkinter text input window class
#===============================================================================
import tkinter as tk
class App(tk.Tk):
    def __init__(self):
        super().__init__()




#===============================================================================
#checkered background
#===============================================================================
def checkered_background():
    square_size = 32 #defines the sqaure size
    width = 1920
    height = 1080
    for row in range(height // square_size):
        for column in range(width // square_size):
            x = column * square_size  # math for calculating the squares
            y = row * square_size  
            if (row+column) % 2 == 0:
                color = (255, 255, 255) #white
            else:
                color = (0, 0, 0) #black
            pygame.draw.rect(screen, color, (x, y, square_size, square_size)) #displays the sqaures




#===============================================================================
#Camera Follow Player
#===============================================================================
def camera_follow():         # currently unused
    camera_width, camera_height = 1280, 1720
    camera = pygame.Rect(0, 0, camera_width, camera_height)
    camera.x, camera.y = 0, 0

    camera_speed = vel
    keys = pygame.key.get_pressed()

    if keys[pygame.K_LEFT]:
        camera.x -= camera_speed
        print("CamLeft")
    if keys[pygame.K_RIGHT]:
        camera.x += camera_speed
        print("CamRight")
    if keys[pygame.K_UP]:
        camera.y -= camera_speed
        print("CamUp")
    if keys[pygame.K_DOWN]:
        camera.y += camera_speed
        print("CamDown")

    pygame.display.update(camera.move(camera.x, camera.y))
    pygame.display.flip()

#===============================================================================
#Inventory Main
#===============================================================================
playerInventory = [] #initialise the list

def mainPlayerInventory(playerInventory):
    pygame.draw.rect(screen, (234, 221, 202), (0, 0, 500, 100))#inventory hotbar
    keys = pygame.key.get_pressed()# checks for actively pressed keys

    if keys[pygame.K_q]: #checks the active key and if it is q
        choice = askstring("Input", "Would you like to 'add' or 'retrieve' an item?")#asks the user what item they want to add
        if choice == "add":
            item = askstring("Input", "Please enter the name of the item you would like to add")# item name
            if len(playerInventory) >= 5:#checks if the list is full
                print("Inventory full!")
            else:
                playerInventory.append(item)#adds the item to the list
                print("Item added!")
                print(playerInventory)#recalls the function to draw the inventory again
        elif choice == "retrieve":
            item = askstring("Input", "Please enter the name of the item you would like to retrieve")# asks the user for the item name
            try:
                playerInventory.remove(item)#removes the item from the list
                print("Item retrieved!")
                print(playerInventory)#recalls the function to draw the inventory again
            except ValueError:
                print("Item not in inventory")#checks if the item is there or not 

    posX = len(playerInventory) * 100 #finds the position of the item depending on its position in the list
    pygame.draw.rect(screen, (0, 0, 255), (0, 0, posX, 100)) #updates the screen with the inventory items
    pygame.display.flip()


#===============================================================================
#Mouse x-y coordinate grabber
#===============================================================================
def getMouseXY():
    x1,y1 = pygame.mouse.get_pos()
    return x1,y1
#===============================================================================
#Factory Building Placement
#===============================================================================
buildingCoordinates = [] #initialises the list

def buildingPlacement():
    print("Building placement attempted")#detects if the mouse is clicked and displays a message if so
    #getMouseXY()
    x1,y1 = pygame.mouse.get_pos()
    x_over = x1 % 32 
    x_building_pos = x1 - x_over
    y_over = y1 % 32
    y_building_pos = y1 - y_over

    print("Y-Position = ", y_building_pos)
    print("X-Position = ", x_building_pos)

    print("Currrent Building Locations: ", buildingCoordinates)

    if y_building_pos in buildingCoordinates and x_building_pos in buildingCoordinates:
        print("Building already here!")
    else:
        buildingCoordinates.append(x_building_pos)
        buildingCoordinates.append(y_building_pos)
        buildingFunction(x_building_pos, y_building_pos)
        print("Buildings placed at ", buildingCoordinates)
        
        
        building = pygame.image.load(os.path.join("assets", "machine_assembler_tier_1.PNG"))
        screen.blit(building, (x_building_pos, y_building_pos))
        pygame.display.flip()
        

#===============================================================================
#Factory Building function window
#===============================================================================
def buildingFunction(x_building_pos, y_building_pos):
    window = tk.Tk()
    window.title("Building Function")
    
    def button_click(button_number):
        print(f"button {button_number} clicked!")
#===============================================================================
#Factory Belt Placement
#===============================================================================
def beltPlacement():
    print("Belt Placed")#detects if mouse was clicked and displays a message if so


#===============================================================================
# Login system
#===============================================================================
window = tk.Tk()
window.title("Login form")
window.geometry('340x440')
window.configure(bg='#333333')



def login():
    master_username = "test"
    master_password = "test"
    if username_entry.get()==master_username and password_entry.get()==master_password:
        messagebox.showinfo(title="Login Success", message="You successfully logged in.")
        main_menu()
    else:
        messagebox.showerror(title="Error", message="Invalid login.")

frame = tkinter.Frame(bg='#333333')


# Creating widgets
login_label = tk.Label(
    frame, text="Login", bg='#333333', fg="#FF3399", font=("Arial", 30))
username_label = tk.Label(
    frame, text="Username", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
username_entry = tk.Entry(frame, font=("Arial", 16))
password_entry = tk.Entry(frame, show="*", font=("Arial", 16))
password_label = tk.Label(
    frame, text="Password", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
login_button = tk.Button(
    frame, text="Login", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=login)

# Placing widgets on the screen
login_label.grid(row=0, column=0, columnspan=2, sticky="news", pady=40)
username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1, pady=20)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1, pady=20)
login_button.grid(row=3, column=0, columnspan=2, pady=30)

frame.pack()

window.mainloop()
#===============================================================================
#goofy ahh database
#===============================================================================
#connect main database
def databaseConnect():
    conn = sqlite3.connect('main.db')
    curs = conn.cursor()

    curs.execute("""CREAE TABLE IF NOT EXISTS logindata (
                    username text,
                    password text,
                    primary key(username)
                    )""")

#===============================================================================
#placeholder
#===============================================================================



#===============================================================================
#placeholder
#===============================================================================



#===============================================================================
#placeholder
#===============================================================================



#===============================================================================
#placeholder
#===============================================================================



#===============================================================================
#placeholder
#===============================================================================



#===============================================================================
#Main function
#===============================================================================
def program_start():
    login()
    pygame.quit()#checks if the program is closed down or quit


#===============================================================================
#Main While loop - LEAVE AS IS
#===============================================================================
while run:
  program_start()#start function to avoid recusrion errors

