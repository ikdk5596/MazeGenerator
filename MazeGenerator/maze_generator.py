import argparse
from PIL import Image
import numpy as np


parser = argparse.ArgumentParser()
parser.add_argument("width", help = "The width of the resulting Image in Pixels", type=int)
parser.add_argument("height", help = "The height of the resulting Image in Pixels", type=int)
parser.add_argument("--output", help = "The name of the output-file", type=str)
args=parser.parse_args()

width = args.width
height =  args.height

print("Starting to compute the maze...")

wallArr = np.zeros((width,height,4))
visitedArr = np.zeros((width,height))
#   1
# 0 z 2 
#   3
walls = []


#walls.append((np.random.randint(0,width),np.random.randint(0,height)))
x=0
y=height/2
wallArr[x,y,0]=1
visitedArr[x,y]=1

if(x-1>0):
    walls.append((x,y,0))
if(y-1>0):
    walls.append((x,y,1))
if(x+1<width):
    walls.append((x,y,2))
if(y+1<height):
    walls.append((x,y,3))

finished = False

while(not finished):
    #print(len(walls))
    i = np.random.randint(0,len(walls))
    x=walls[i][0]
    y=walls[i][1]
    w=walls[i][2]
    xDest=x
    yDest=y
    if(w==0):
        xDest = xDest - 1
    if w==1:
        yDest = yDest - 1
    if w==2:
        xDest = xDest + 1
    if w==3:
        yDest = yDest + 1
    if(xDest >= 0 and yDest >= 0 and xDest<width and yDest<height) and ((visitedArr[x,y]+visitedArr[xDest,yDest]) == 1):#Exakt eine Zelle Besucht
        #print "Visited: ",visitedArr[x,y]," ",visitedArr[xDest,yDest]
        wallArr[x,y,w] = 1
        visitedArr[xDest,yDest] = 1    
        #if(xDest-1>=0):
        walls.append((xDest,yDest,0))
        #if(yDest-1>=0):
        walls.append((xDest,yDest,1))
        #if(xDest+1<width):
        walls.append((xDest,yDest,2))
        #if(yDest+1<height):
        walls.append((xDest,yDest,3))
    del walls[i]
    if(len(walls)==0):
        finished = True
    #else:
        #print("Not Finished")

print("Finished!\nNow plotting the maze")
img = Image.new("RGB",(width*2+1,height*2+1),"black")
for x in range(0,len(visitedArr)):
    for y in range(0,len(visitedArr[x])):
        if(visitedArr[x,y]==1):
            img.putpixel((x * 2 +1,y * 2 +1),(255,255,255))
        if(wallArr[x,y,0]==1):
            img.putpixel((x*2,y*2+1),(255,255,255))
        if(wallArr[x,y,1]==1):
            img.putpixel((x*2+1,y*2),(255,255,255))
        if(wallArr[x,y,2]==1):
            img.putpixel((x*2+2,y*2+1),(255,255,255))
        if(wallArr[x,y,3]==1):
            img.putpixel((x*2+1,y*2+2),(255,255,255))
output = "output.jpg"
if args.output:
    output = args.output
img.save(output, interpolation = 'none')
img.show()
print("Finished!")

