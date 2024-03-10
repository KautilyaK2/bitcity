import pygame
import random
import asyncio
pygame.init()
clock = pygame.time.Clock()
display=pygame.display.set_mode((800,800))
async def main():
    width=20
    height=20
    types={'grass':(0,255,0),'brick':(165,42,42),'water':(51,133,255),'blank':(0,0,0)}
    amounts={k:10 for k in list(types.keys())[:-1]}
    pi=0
    pj=0
    grid=[[random.choice(list(types.keys())[:-1]) for i in range(width)] for j in range(height)]
    done=0
    while not done:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                done=1
            if event.type==pygame.KEYDOWN:
                if event.key==pygame.K_LEFT:
                    pi=pi-1
                if event.key==pygame.K_RIGHT:
                    pi=pi+1
                if event.key==pygame.K_DOWN:
                    pj=pj+1
                if event.key==pygame.K_UP:
                    pj=pj-1
                if event.key==pygame.K_b:
                    if amounts['brick']>=1:
                        grid[pi][pj]='brick'
                        amounts['brick']-=1
                if event.key==pygame.K_g:
                    if amounts['grass']>=1:
                        grid[pi][pj]='grass'
                        amounts['grass']-=1
                if event.key==pygame.K_w:
                    if amounts['water']>=1:
                        grid[pi][pj]='water'
                        amounts['water']-=1
                if event.key==pygame.K_m:
                    mined=grid[pi][pj]
                    if mined!='blank':
                        amounts[mined]+=1
                        amounts[random.choice(['brick','water','grass'])]+=0.5
                    grid[pi][pj]='blank'
        display.fill((255,255,255))
        for i in range(width):
            for j in range(height):
                pygame.draw.rect(display,types[grid[i][j]], pygame.Rect(i*800/width, j*800/height, 800/width, 800/height))
        pygame.draw.rect(display,(255,0,0), pygame.Rect(pi*800/width, pj*800/height, 800/width, 800/height))
        pygame.display.update()
        clock.tick(40)
        await asyncio.sleep(0)
    pygame.quit()
asyncio.run(main())