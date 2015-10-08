import pygame
import random

pygame.init()

display_width = 840
display_height = 600
button_color = (30, 50, 70)

lane_height = 400

white = (255,255,255)

gameDisplay = pygame.display.set_mode((display_width,display_height))

pygame.display.set_caption('purple')
clock = pygame.time.Clock()

class Lane():
    
    def __init__(self, position):
        self.position = position
        
        self.proportion = lane_height /2
        self.xposition = position * 150 - 80
        self.red_switch = False
        self.blue_switch = False
        
        self.button_intervalx = [self.xposition, self.xposition + 100]
        
        
    def checkSwitches(self):
        if self.red_switch == True and self.blue_switch == False:
            
            #red player wins exchange
            self.proportion += 1
        elif self.red_switch == False and self.blue_switch:
            
            #blue player wins exchange
            self.proportion -= 1
        
        
    def draw_lane(self):
        pygame.draw.rect(gameDisplay, (0,0,255), [self.xposition , 100, 100, lane_height])
    
        pygame.draw.rect(gameDisplay, (255,0,0), [self.xposition , 100, 100, self.proportion])
        
        # red switches
        if self.red_switch == False:
            pygame.draw.rect(gameDisplay, button_color, [self.xposition, 30, 100, 50])
        else:
            pygame.draw.rect(gameDisplay, (255,0,0), [self.xposition, 30, 100, 50])
        
        #blue switches
        if self.blue_switch == False:
            pygame.draw.rect(gameDisplay, button_color, [self.xposition, 525, 100, 50])
        else:
            pygame.draw.rect(gameDisplay, (0,0,255), [self.xposition, 525, 100, 50])
        

        
        
    
class Player():
    
    def __init__(self, color):
        self.color = color
        self.winner = False
        self.used_switches = 0
        
    def changeSwitch(self, lane):
        
        if self.color == "red":
            #red player
            if lanes[lane].red_switch == True:
                lanes[lane].red_switch = False
                self.used_switches -= 1
            else:
                if self.used_switches < 3:
                    lanes[lane].red_switch = True
                    self.used_switches +=1
        else:
            
            #blue player
            if lanes[lane].blue_switch == True:
                lanes[lane].blue_switch = False
                self.used_switches -=1
            else:
                if self.used_switches < 3:
                    lanes[lane].blue_switch = True
                    self.used_switches += 1



class AI():
    def __init__(self):
        self.time_check = 0
        
        
    def change_red_score(self):
    
        if self.time_check < pygame.time.get_ticks():
            self.time_check += 3000
            computer.changeSwitch(0)
            print "now!"
        
        
    
def draw_board():
    for i in lanes:
        i.draw_lane()

                     

def game_loop():
    still_playing = True
    while still_playing:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse = pygame.mouse.get_pos()
                # print "down"
                for i in lanes:
                    if mouse[1] > 525 and mouse[1] < 575:
                        if i.button_intervalx[0] < mouse[0] and i.button_intervalx[1] > mouse[0]:
                            mitchell.changeSwitch( i.position -1 )
                            print "succesfully switched"
            #print(event)
        
        gameDisplay.fill(white)
        
        
        lane1.checkSwitches()
        lane2.checkSwitches()
        lane3.checkSwitches()
        lane4.checkSwitches()
        lane5.checkSwitches()
        
        
        draw_board()
        
        pygame.display.update()
        clock.tick(20)
    
    

lane1 = Lane(1)
lane2 = Lane(2)
lane3 = Lane(3)
lane4 = Lane(4)
lane5 = Lane(5)

mitchell = Player('blue')
computer = Player('red')
AI_controller = AI()

lanes = [lane1, lane2, lane3, lane4, lane5]



game_loop()


