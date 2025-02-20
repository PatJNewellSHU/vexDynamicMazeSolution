#region VEXcode Generated Robot Configuration
import math
import random
from vexcode_vr import *

# Brain should be defined by default
brain=Brain()

drivetrain = Drivetrain("drivetrain", 0)
pen = Pen("pen", 8)
pen.set_pen_width(THIN)
left_bumper = Bumper("leftBumper", 2)
right_bumper = Bumper("rightBumper", 3)
front_eye = EyeSensor("frontEye", 4)
down_eye = EyeSensor("downEye", 5)
front_distance = Distance("frontdistance", 6)
distance = front_distance
magnet = Electromagnet("magnet", 7)
location = Location("location", 9)

#endregion VEXcode Generated Robot Configuration
# ------------------------------------------
# 
# 	Project:      VEXcode Project
#	Author:       VEX
#	Created:      Patrick Newell
#	Description:  VEXcode VR Python Project
# 
# ------------------------------------------

# Add project code in "main"
def main():
    #solveMaze()
    #drivetrain.turn_for(RIGHT, 90, DEGREES)
    #returnBack()

    mapMaze()
    

    


    

# VR threads — Do not delete
vr_thread(main)

def mapMaze():
    drivetrain.set_drive_velocity(100, PERCENT)
    drivetrain.set_turn_velocity(100, PERCENT)
    nodeList = []


    
    #starting postion based on top left conrer being 0,0
    xCor = 4
    yCor = 7
    pen.set_pen_width(WIDE)
    pen.set_pen_color(BLACK)
    pen.move(DOWN)

    while not down_eye.detect(RED):
        if front_distance.get_distance(MM) > 2000 and ((xCor == 4 or xCor == 3) and(yCor == 0 or yCor == 7)):
            drivetrain.turn_for(RIGHT, 180, DEGREES)



        nodeLogged = False
        up = 0
        down = 0
        left = 0
        right = 0

        # chekc if node exists
        #if it doesnt it will then rotate around the current node to see where it has walls
        #then it will create a new node with current coords and append them to the nodelist
        for n in nodeList:
            if n['x'] == xCor and n['y'] == yCor:
                nodeLogged = True 
        if nodeLogged == False:
            brain.print(front_distance.get_distance(MM))
            brain.new_line()
            if front_distance.get_distance(MM) < 260:
                up = 1 
            drivetrain.turn_for(RIGHT, 90, DEGREES)
            brain.print(front_distance.get_distance(MM))
            brain.new_line()
            if front_distance.get_distance(MM) < 260:
                right = 1
            drivetrain.turn_for(RIGHT, 90, DEGREES)
            brain.print(front_distance.get_distance(MM))
            brain.new_line()
            if front_distance.get_distance(MM) < 260:
                down = 1
            drivetrain.turn_for(RIGHT, 90, DEGREES)
            brain.print(front_distance.get_distance(MM))
            brain.new_line()
            if front_distance.get_distance(MM) < 260:
                left = 1
            drivetrain.turn_for(RIGHT, 90, DEGREES)
            brain.print(front_distance.get_distance(MM))
            brain.new_line()
            newNode = createNode(xCor,yCor,up,down,left,right)
            nodeList.append(newNode)
            brain.print(newNode)
            brain.new_line()
            brain.print(nodeList)
            

        if front_distance.get_distance(MM) > 260:

            drivetrain.drive_for(FORWARD, 250, MM)
            #change chords based on what movenets performed
            if drivetrain.heading(DEGREES) == 0:
                yCor -= 1
            
            elif drivetrain.heading(DEGREES) == 90:
                xCor += 1

            elif drivetrain.heading(DEGREES) == 180:
                yCor += 1

            elif drivetrain.heading(DEGREES) == 270:
                xCor -= 1
            drivetrain.turn_for(RIGHT, 90, DEGREES)
        else:
            drivetrain.turn_for(LEFT, 90, DEGREES)
        

    
    drivetrain.turn_for(RIGHT, 180, DEGREES)
    pen.set_pen_color(RED)
    pen.set_pen_width(EXTRA_THIN)
    pen.move(DOWN)
    while not (yCor == 7 and xCor == 4):
        if front_distance.get_distance(MM) > 2000 and ((xCor == 4 or xCor == 3) and(yCor == 0 or yCor == 7)):
            drivetrain.turn_for(RIGHT, 90, DEGREES)
        nodeLogged = False
        up = 0
        down = 0
        left = 0
        right = 0

        # chekc if node exists
        #if it doesnt it will then rotate around the current node to see where it has walls
        #then it will create a new node with current coords and append them to the nodelist

        for n in nodeList:
            if n['x'] == xCor and n['y'] == yCor:
                nodeLogged = True 
        if nodeLogged == False:
            brain.print(front_distance.get_distance(MM))
            brain.new_line()
            if front_distance.get_distance(MM) < 260:
                up = 1 
            drivetrain.turn_for(RIGHT, 90, DEGREES)
            brain.print(front_distance.get_distance(MM))
            brain.new_line()
            if front_distance.get_distance(MM) < 260:
                right = 1
            drivetrain.turn_for(RIGHT, 90, DEGREES)
            brain.print(front_distance.get_distance(MM))
            brain.new_line()
            if front_distance.get_distance(MM) < 260:
                down = 1
            drivetrain.turn_for(RIGHT, 90, DEGREES)
            brain.print(front_distance.get_distance(MM))
            brain.new_line()
            if front_distance.get_distance(MM) < 260:
                left = 1
            drivetrain.turn_for(RIGHT, 90, DEGREES)
            brain.print(front_distance.get_distance(MM))
            brain.new_line()
            newNode = createNode(xCor,yCor,up,down,left,right)
            nodeList.append(newNode)
            brain.print(newNode)
            brain.new_line()
            brain.print(nodeList)

        if front_distance.get_distance(MM) > 260:
            drivetrain.drive_for(FORWARD, 250, MM)
            if drivetrain.heading(DEGREES) == 0:
                yCor -= 1
            
            elif drivetrain.heading(DEGREES) == 90:
                xCor += 1

            elif drivetrain.heading(DEGREES) == 180:
                yCor += 1

            elif drivetrain.heading(DEGREES) == 270:
                xCor -= 1
            drivetrain.turn_for(RIGHT, 90, DEGREES)
        else:
            drivetrain.turn_for(LEFT, 90, DEGREES)
    while not down_eye.detect(RED):
        if front_distance.get_distance(MM) > 2000 and ((xCor == 4 or xCor == 3) and(yCor == 0 or yCor == 7)):
            drivetrain.turn_for(RIGHT, 180, DEGREES)
        nodeLogged = False
        up = 0
        down = 0
        left = 0
        right = 0

        # chekc if node exists
        #if it doesnt it will then rotate around the current node to see where it has walls
        #then it will create a new node with current coords and append them to the nodelist
        for n in nodeList:
            if n['x'] == xCor and n['y'] == yCor:
                nodeLogged = True 

        if nodeLogged == False:
            brain.print(front_distance.get_distance(MM))
            brain.new_line()
            if front_distance.get_distance(MM) < 260:
                up = 1 
            drivetrain.turn_for(RIGHT, 90, DEGREES)
            brain.print(front_distance.get_distance(MM))
            brain.new_line()
            if front_distance.get_distance(MM) < 260:
                right = 1
            drivetrain.turn_for(RIGHT, 90, DEGREES)
            brain.print(front_distance.get_distance(MM))
            brain.new_line()
            if front_distance.get_distance(MM) < 260:
                down = 1
            drivetrain.turn_for(RIGHT, 90, DEGREES)
            brain.print(front_distance.get_distance(MM))
            brain.new_line()
            if front_distance.get_distance(MM) < 260:
                left = 1
            drivetrain.turn_for(RIGHT, 90, DEGREES)
            brain.print(front_distance.get_distance(MM))
            brain.new_line()
            newNode = createNode(xCor,yCor,up,down,left,right)
            nodeList.append(newNode)
            brain.print(newNode)
            brain.new_line()
            brain.print(nodeList)

        if front_distance.get_distance(MM) > 260:
            drivetrain.drive_for(FORWARD, 250, MM)
            if drivetrain.heading(DEGREES) == 0:
                yCor -= 1
            
            elif drivetrain.heading(DEGREES) == 90:
                xCor += 1

            elif drivetrain.heading(DEGREES) == 180:
                yCor += 1

            elif drivetrain.heading(DEGREES) == 270:
                xCor -= 1
            drivetrain.turn_for(LEFT, 90, DEGREES)
        else:
            drivetrain.turn_for(RIGHT, 90, DEGREES)


    drawMaze(nodeList)
        


def solveMaze():
    #this is now redudnant
    pen.set_pen_width(WIDE)

    drivetrain.set_drive_velocity(100, PERCENT)
    pen.set_pen_color(BLACK)
    pen.move(DOWN)
    drivetrain.set_turn_velocity(100, PERCENT)
    while not down_eye.detect(RED):
        if front_distance.get_distance(MM) > 260:
            drivetrain.drive_for(FORWARD, 250, MM)
            drivetrain.turn_for(RIGHT, 90, DEGREES)
        else:
            drivetrain.turn_for(LEFT, 90, DEGREES)


def returnBack():
    #this is now redudnant
    drivetrain.set_drive_velocity(100, PERCENT)
    pen.set_pen_color(RED)
    pen.set_pen_width(EXTRA_THIN)
    pen.move(DOWN)
    drivetrain.set_turn_velocity(100, PERCENT)
    while front_distance.get_distance(MM) < 2000:
        if front_distance.get_distance(MM) > 260:
            drivetrain.drive_for(FORWARD, 250, MM)
            drivetrain.turn_for(RIGHT, 90, DEGREES)
        else:
            drivetrain.turn_for(LEFT, 90, DEGREES)
            
def createNode(x,y,up,down,left,right):
    node = {
        "x":x,
        "y":y,
        "vertices": [up,down,left,right]
    }
    return node
def drawMaze(nodes):
    brain.print(nodes)
    brain.new_line()
    #maze drawing function
    #im sorry this is so ugly
    #pick out  0,0 from list of nodes then draw out all up walls from that row then right and left then down 
    #then once thats done go to next row and repeat 
    #+++++ 1,1,1,1
    #+   +
    #+   +
    #+++++

    #+++++ 1,1,0,0
    #
    #
    #+++++

    #+   + 0,1,1,1
    #+   +
    #+   +
    #+++++

    #+++++ 1,1,1,0
    #+
    #+
    #+++++

    #+   + 0,0,1,1
    #+   +
    #+   +
    #+   +

    #+++++ 1,0,0,0
    #
    #
    #+   +

    #+   + 0,1,0,0
    #
    #
    #+++++

    #+   + 0,0,1,0 7
    #+
    #+
    #+   +

    #+   + 0,0,0,1 8
    #    +
    #    +
    #+   +

    #+++++ 1,0,1,1 9
    #+   +
    #+   +
    #+   +

    #+++++ 1,0,0,1 10
    #    +
    #    +
    #+   +

    #+++++ 1,0,1,0 11
    #+   
    #+
    #+   +

    #+   + 0,1,1,0 
    #+
    #+
    #+++++

    #+   + 0,1,0,1
    #    +
    #    +
    #+++++

    #+   + 0,0,0,0
    #
    #
    #+   +

    #+++++ 1,1,0,1
    #    +
    #    +
    #+++++




    maze = []

    x = 0
    y = 0
    for i in range(0,64):
        for n in nodes:
            if n['x'] == x and n['y'] == y:
                edges = n['vertices']
                #hell
                if edges[0] == 1 and edges[1] == 1 and edges[2] == 1 and edges[3] == 1:
                    block = "+++++\n+   +\n+   +\n+++++"
                    maze.append(block)

                elif edges[0] == 1 and edges[1] == 1 and edges[2] == 0 and edges[3] == 0:
                    block = "+++++\n\n\n+++++"
                    maze.append(block)

                elif edges[0] == 0 and edges[1] == 1 and edges[2] == 1 and edges[3] == 1:
                    block = "+   +\n+   +\n+   +\n+++++"
                    maze.append(block)


                elif edges[0] == 1 and edges[1] == 1 and edges[2] == 1 and edges[3] == 0:
                    block = "+++++\n+    \n+    \n+++++"
                    maze.append(block)

                elif edges[0] == 0 and edges[1] == 0 and edges[2] == 1 and edges[3] == 1:
                    block = "+   +\n+   +\n+   +\n+   +"
                    maze.append(block)

                elif edges[0] == 1 and edges[1] == 0 and edges[2] == 0 and edges[3] == 0:
                    block = "+++++\n\n\n+   +"
                    maze.append(block)

                elif edges[0] == 0 and edges[1] == 1 and edges[2] == 0 and edges[3] == 0:
                    block = "+   +\n\n\n+++++"
                    maze.append(block)

                elif edges[0] == 0 and edges[1] == 0 and edges[2] == 0 and edges[3] == 1:
                    block = "+   +\n    +\n    +\n+   +"
                    maze.append(block)

                elif edges[0] == 1 and edges[1] == 0 and edges[2] == 1 and edges[3] == 1:
                    block = "+++++\n+   +\n+   +\n+   +"
                    maze.append(block)

                elif edges[0] == 1 and edges[1] == 0 and edges[2] == 0 and edges[3] == 1:
                    block = "+++++\n    +\n    +\n+   +"

                elif edges[0] == 1 and edges[1] == 0 and edges[2] == 1 and edges[3] == 0:
                    block = "+++++\n+    \n+    \n+   +"
                    maze.append(block)

                elif edges[0] == 0 and edges[1] == 1 and edges[2] == 1 and edges[3] == 0:
                    block = "+   +\n+   +\n+   +\n+   +"
                    maze.append(block)

                elif edges[0] == 0 and edges[1] == 1 and edges[2] == 0 and edges[3] == 1:
                    block = "+   +\n    +\n    +\n+++++"
                    maze.append(block)

                elif edges[0] == 0 and edges[1] == 0 and edges[2] == 0 and edges[3] == 0:
                    block = "+   +\n\n\n+   +"
                    maze.append(block)

                elif edges[0] == 1 and edges[1] == 1 and edges[2] == 0 and edges[3] == 1:
                    block  = "+++++\n    +\n    +\n+++++"
                    
        if x == 7:
            x = 0
            y += 1
        x += 1
    count = 0
    for m in maze:
        brain.print(m)
        count += 1
        if count == 7:
            count = 0
            brain.new_line()


                



   


