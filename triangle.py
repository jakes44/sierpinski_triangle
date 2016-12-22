"""
This scipt generates an random animation of the chaos game, in the hopes of 
generating a sierpinski triangle. 

"""
# import for set up and plotting
import math
import random
from matplotlib import pyplot as plt
from matplotlib import animation

# Set up empty plot to start 
fig = plt.figure()
ax = plt.axes(xlim = (-30, 120), ylim = (-30, 120))
pts, = ax.plot([],[], 'k,')

# Point class to make drawing points easier
class point:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distanceTo(self, pt):
        d = math.sqrt((pt.x - self.x)**2 + (pt.y - self.y)**2)
        return d

    def getXY(self):
        return (self.x,self.y)

    def midpoint(self, pt):
        midX = (self.x + pt.x)/2
        midY = (self.y + pt.y)/2
        return (midX,midY)

# Keeo track of random point each turn
curPt = point(random.randint(0,100), random.randint(0,100))

# equilateral triangle with pts (0,0), (a,0), (a/2, sqrt(3)a/2)
pt1 = point(0,0)
pt2 = point(100,0)
pt3 = point(50,86.60)
vertexlist = (pt1,pt2,pt3)

# init function to start out an equilateral triangle
def init():

    pts.set_data( zip(*[pt1.getXY(),pt2.getXY(), pt3.getXY()]) )

    return pts,

def inTriangle(pt):
    #Fudge value since need to be fairly accurate... Not too much, but enough
    epsilon = 0.00001

    # Calculate the barycentric wieghts to determine  if point is in the triangle
    # Converts a given cartesian coordinate into barycentric cooridnate
    bary1 = ((pt2.y - pt3.y)*(pt.x - pt3.x) + (pt3.x - pt2.x)*(pt.y - pt3.y))/( (pt2.y-pt3.y)*(pt1.x-pt3.x) + (pt3.x-pt2.x)*(pt1.y-pt3.y))
    bary2 = ((pt3.y - pt1.y)*(pt.x - pt3.x) + (pt1.x - pt3.x)*(pt.y - pt3.y))/( (pt2.y-pt3.y)*(pt1.x-pt3.x) + (pt3.x-pt2.x)*(pt1.y-pt3.y))
    bary3 = 1 - bary1 - bary2

    for i in (bary1,bary2,bary3):
        if i+epsilon < 0 or i-epsilon > 1:
            return False

    return True

# Function to draw random points... 
# This is what makes the choas game/seiprinski triangle.
def animate(i):

    # Throw out initial rolls, in case of error
    # Have to account because this is only pseudo-random 
    if i % 4 == 0:
        return pts,
    # Pick random point, loop until find one in triangle
    if i == 0:
        curPt.x = random.random() * 100
        curPt.y = random.random() * 100 

    while not inTriangle(curPt):
        curPt.x = random.random() * 100
        curPt.y = random.random() * 100 

    # Pick a random vertex and calculate midpoint between it and current point
    vertex = vertexlist[random.randint(0,2)]
    midpoint = point(*vertex.midpoint(curPt))

    # Set new point to current point
    curPt.x = midpoint.x
    curPt.y = midpoint.y
    # Plot the data
    xdata = list(pts.get_xdata())
    ydata = list(pts.get_ydata())
    xdata.append(midpoint.x)
    ydata.append(midpoint.y)
    pts.set_data(xdata,ydata)
    return pts,

# Set up animation
# Change frames to get more dots and interval to change the speed at which they are produced (higher is faster in this case)
anim = animation.FuncAnimation(fig, animate, init_func=init, frames = 5000, interval = 1, blit=True)

# save animation
# ffmpegwriter = animation.writers['ffmpeg']
# writer = ffmpegwriter(fps=30, bitrate=1800)

# anim.save('chaos.mp4', writer=writer)

plt.show()