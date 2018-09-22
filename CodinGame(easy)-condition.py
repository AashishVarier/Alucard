#all does the same thing - codingame q:POWER OF THOR:E1

#example 1
lx, ly, x, y = [int(i) for i in input().split()]

while True:
    move  = 'N' if y>ly else 'S' if y<ly else ''
    move += 'W' if x>lx else 'E' if x<lx else ''
    
    if 'N' in move: y-=1
    if 'S' in move: y+=1
    if 'W' in move: x-=1
    if 'E' in move: x+=1

    print(move)


#examample 2

import sys, math

# LX: the X position of the light of power
# LY: the Y position of the light of power
# TX: Thor's starting X position
# TY: Thor's starting Y position
LX, LY, TX, TY = [int(i) for i in input().split()]

DX = LX - TX
DY = LY - TY

 # game loop
while 1:
    E = int(input()) # The level of Thor's remaining energy, representing the number of moves he can still make.
    
    h =""
    if DX > 0:
        h = "E"
        DX += 1 
    elif DX < 0:
        h = "W"
        DX -= 1
    v = ""
    if DY > 0:
        v = "S"
        DY -= 1 
    elif DY < 0:
        v = "N"
        DY += 1
        
    print(v+h)
    
