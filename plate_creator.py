
"""
1. Generate X random points in  
"""
import pygame
import numpy as np
import random as rd
import pandas as pd
import math
import sys
import time

def fps_counter(display):
    font = pygame.font.SysFont("Arial" , 18 , bold = True)
    fps = str(int(clock.get_fps()))
    fps_t = font.render(fps , 1, pygame.Color("RED"))
    display.blit(fps_t,(0,0))

def run():
    while True:
        display.fill((200,0,0))


        display.blit(map_display,(0,0))


        for event in pygame.event.get():
                #event is an input of some description
                #CLose window event
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

        #fps_counter(display)
        #Scale up screen
        screen.blit(pygame.transform.scale(display, screen.get_size()),(0,0))
        pygame.display.update()
        #Force game to run at X FPS
        clock.tick(60)



def grow_grains(grains,map,colour_map):
    full = True
    n_grains = len(grains)
    map_size = [np.size(map,0),np.size(map,1)]
     #1. iterate through grains
    for grain in range(0,n_grains):
        edge_list = grains[str(grain)]['edges']
        pass_val = grains[str(grain)]['growth_factor']
        #2. iterate through edge point list
        to_remove = []
        for point in range(0,len(edge_list)):
          #look in neighbouring 4 tiles to see if there is any empty space (i.e. 0)
            edge = edge_list[point]
            liquid = []
            #use modulus to wrap
            neighbours = [
                 [(edge[0]+1)%map_size[0],edge[1]%map_size[1]],
                 [(edge[0]-1)%map_size[0],edge[1]%map_size[1]],
                 [edge[0]%map_size[0],(edge[1]+1)%map_size[1]],
                 [edge[0]%map_size[0],(edge[1]-1)%map_size[1]]
            ]
            for i in range(0,4):
                 if map[neighbours[i][0],neighbours[i][1]] == 0:
                      liquid.append(i)
                      full = False
                 else:
                      pass
                 
            #remove from edge list
            if len(liquid) == 0:
                 to_remove.append(edge)
            else:
                #see if grain grows.
                rd_val = rd.random()
                if rd_val > pass_val:
                    #grow
                    rd2 = rd.randint(0,len(liquid)-1)
                    grow_p = liquid[rd2]
                    map[neighbours[grow_p][0],neighbours[grow_p][1]] = grain
                    colour_map[neighbours[grow_p][0],neighbours[grow_p][1]] = grains[str(grain)]['colour']
                    #add new point to edge list
                    edge_list.append([neighbours[grow_p][0],neighbours[grow_p][1]])

        #remove any fully surrounded grains
        for i in range(0,len(to_remove)):
             edge_list.remove(to_remove[i])
        #remove duplicates:
        unique_data = [list(x) for x in set(tuple(x) for x in edge_list)]
        edge_list = unique_data
        grains[str(grain)]['edges'] = edge_list
    #time.sleep(0.1)
    return full

pygame.init()

pygame.display.set_caption('Plate Generator')

pygame.display.set_caption("Procedural Map")
# resolution of window
x_window = 700
y_window = 700

#scale of game. >1 means smaller pixels, <1 means bigger pixels
scale = 0.2


x_res = int(x_window*scale)
y_res = int(y_window*scale)
screen = pygame.display.set_mode((x_window,y_window))

        # To scale up the screen we render at a smaller size then scale it up.
        #Create a black box with 320,240 size.
display = pygame.Surface((x_res,y_res))

        #self.particle = Particle(self,(1,1),)

        #set max FPS
clock = pygame.time.Clock()



#Initialize a large map the size of the display


#Initialize map
map = np.zeros([x_res,y_res], dtype=int)
colour_map = np.zeros([x_res,y_res,3],dtype=int)
n_grains = 6

grains = {}

#Generate X grain starts
for g in range(0,n_grains):
    c = rd.randint(0,y_res-1)
    r = rd.randint(0,x_res-1)

    grains[str(g)] ={
         'edges': [[r,c]],
         'growth_factor': rd.random(),
         'colour': [rd.randint(0,255),rd.randint(0,255),rd.randint(0,255)]
    }

    map[r,c] = g
    colour_map[r,c,:] = grains[str(g)]['colour']

edge_list_Length = []

full = False
while full == False:
    #loop:
    n_edges = 0
    for grain in range(0,n_grains):
         n_edges = n_edges + len(grains[str(grain)]['edges'])
    print(n_edges)

    full = grow_grains(grains,map,colour_map)

    map_display = pygame.surfarray.make_surface(colour_map)
    display.blit(map_display,(0,0))
    screen.blit(pygame.transform.scale(display, screen.get_size()),(0,0))
    pygame.display.update()
    clock = pygame.time.Clock()
    clock.tick(60)

print('Finished!')
run()