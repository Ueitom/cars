# -*- coding: utf-8 -*-
import pygame

width = 600
height = 600

pygame.init()

posx = 0
posy = 300
posx1= 300
posy2= 0

fundo = pygame.display.set_mode((width,height))

sair = True

while sair:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sair = False
    fundo.fill((0,0,0))
    pygame.draw.rect(fundo, (255,255,255), [posx,posy,20 , 10])
    posx+=0.5
    
    pygame.draw.rect(fundo, (255,255,255), [posx1,posy2,10 , 20])
    posy2+=0.5
        
    pygame.display.update()
    if posx >= width:
        posx=0
    if posy2 >= height:
        posy2=0

pygame.quit()
