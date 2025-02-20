# vexDynamicMazeSolution

=
Solving the Maze
=
the basic solver aglorithm I used can be seen in the solve maze function which is expanded upon once it comes to mapping the maze
this is a simple wall following algorihtm that will go unti a red square is detected by the optical sensor

=
Solving in the shortest Path
=
for the shortest Path I turned the robot around from where ti reached the red square and have it folow the right wall back to the start but this time drawing inn a different and thinner pen colour
this meant that the overlapping paths and could be seen and here the returning path and the innital path overlap is the shortest path

=
Returning 
=
for retruning I at first did it turn around frm the red square then perform the wall following algorithm until it reaches a point with a large distance in fornt as this would mean it is string at the entracne 
this is later chnaged with it going until it reachs the start coordinates from the maze mapping code as this makes it more accurate

=
Maze Mapping
=

for mapping the maze I created three loops 
the first does a right wall follow to the exit fo fthe maze at the red suqare creating a node and its coordinates based on the top left being 0,0
each node is checked to see if tit exists if it doesnt the robot spins and notes the existance of surrounding walls
once it reaches the exit it turns around and does a other right wall foloow back ot the start noting any new nodes on the way
once at the start it turns aorund and follows the left wall back to the exit noting any new nodes on the way
to make sure it doesnt drive off the edge i make sure if it is on the exit or entracen coords and the distacne is greater than 2000 meaning its looking over the edge then it will turn away and go a different path
theb the horrible mighty if soup creates an ascii art maze reporuduction however ran out of time an ideas for getitng to dipslay nicely 

VideoDemoLink:
for some reason part of my screen gets cut off but all you miss is the list of nodes 
https://youtu.be/4Pox6jUbSI8
