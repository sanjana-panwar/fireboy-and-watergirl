# fireboy and watergirl in the 112 maze

from cmu_graphics import *

def drawHomeScreen(app):
    drawLabel("Fireboy", 360, 200, size=100, fill='crimson', 
              border='black', borderWidth=3, bold=True)
    drawLabel("&", 590, 200, size=70, fill='gold', 
              border='black', borderWidth=2, bold=True)
    drawLabel("Watergirl", 850, 200, size=100, fill='deepSkyBlue', 
              border='black', borderWidth=3, bold=True)
    drawLabel("in", 590, 300, size=50, fill='gold',
              border='black', borderWidth=1.5, bold=True)
    drawLabel("the 112 Maze", 600, 400, size=80, fill='gold',
              border='black', borderWidth=2.5, bold=True)
    drawLabel("Play", 600, 600, size=80, fill='gold',
              border='black', borderWidth=2.5, bold=True)

def drawLevelScreen(app):
    drawLabel("Choose your level!", 600, 170, size=90, fill='gold', 
              border='black', borderWidth=3, bold=True)
    drawLabel("Level 1", 600, 325, size=70, fill='gold', 
              border='black', borderWidth=2, bold=True)
    drawLabel("Level 2", 600, 450, size=70, fill='gold', 
              border='black', borderWidth=2, bold=True)
    drawLabel("Level 3", 600, 575, size=70, fill='gold', 
              border='black', borderWidth=2, bold=True)
    drawLabel("Help", 1130, 760, size=50, fill='gold', 
              border='black', borderWidth=1.5, bold=True)
    
def drawPauseScreen(app):
    drawLabel("Paused!", 600, 180, size=100, fill='gold',
              border='black', borderWidth=3, bold=True)
    drawLabel(f"Time: {app.time}", 600, 350, size=70, fill='gold',
              border='black', borderWidth=2, bold=True)
    drawLabel("Resume", 600, 475, size=70, fill='gold',
              border='black', borderWidth=2, bold=True)
    drawLabel("Start Again", 600, 600, size=70, fill='gold',
              border='black', borderWidth=2, bold=True)
    drawLabel("Help", 1130, 760, size=50, fill='gold', 
              border='black', borderWidth=1.5, bold=True)

def drawLoseScreen(app):
    drawLabel("Oh no!", 600, 175, size=80, fill='gold',
              border='black', borderWidth=2.5, bold=True)
    drawLabel("You Lost", 600, 300, size=125, fill='gold',
              border='black', borderWidth=3, bold=True)
    drawLabel("Try Again", 600, 475, size=70, fill='gold',
              border='black', borderWidth=2, bold=True)
    drawLabel("Back", 600, 600, size=70, fill='gold',
              border='black', borderWidth=2, bold=True)
    drawLabel("Help", 1130, 760, size=50, fill='gold', 
              border='black', borderWidth=1.5, bold=True)

def drawWinScreen(app):
    drawLabel("You Won!", 600, 200, size=125, fill='gold',
              border='black', borderWidth=3, bold=True)
    drawLabel(f"Time: {app.time}", 600, 400, size=70, fill='gold',
              border='black', borderWidth=2, bold=True)
    drawLabel("Retry", 600, 500, size=70, fill='gold',
              border='black', borderWidth=2, bold=True)
    drawLabel("Back", 600, 600, size=70, fill='gold',
              border='black', borderWidth=2, bold=True)

#------------------------------------------------------------------------------

class Block:
    def __init__(self, left, top):
        self.left = left
        self.top = top
        self.color = 'white'
    
    def makeBlock(self):
        drawRect(self.left, self.top, 5, 5, fill=self.color)

class emptyBlock(Block):
    def __init__(self, left, top):
        super().__init__(left, top)
        self.color = 'white'

class floorBlock(Block):
    def __init__(self, left, top):
        super().__init__(left, top)
        self.color = 'black'

class wallBlock(Block):
    def __init__(self, left, top):
        super().__init__(left, top)
        self.color = 'black'

class fireBlock(Block):
    def __init__(self, left, top):
        super().__init__(left, top)
        self.color = 'crimson'

class waterBlock(Block):
    def __init__(self, left, top):
        super().__init__(left, top)
        self.color = 'deepSkyBlue'

class gooBlock(Block):
    def __init__(self, left, top):
        super().__init__(left, top)
        self.color = 'yellowGreen'

#------------------------------------------------------------------------------

def drawMap1(app): # CITATION: same layout as level 1 from the game
    # doors
    drawRect(1000, 52, 65, 100, fill=None, border='crimson', borderWidth=5)
    drawRect(1100, 52, 65, 100, fill=None, border='deepSkyBlue', borderWidth=5)
    # lines
    drawLine(0, 790, 1000, 790, fill='black', lineWidth=3)
    drawLine(1000, 790, 1000, 650, fill='black', lineWidth=3)
    drawLine(1000, 650, 1200, 650, fill='black', lineWidth=3)
    drawLine(0, 650, 250, 650, fill='black', lineWidth=3)
    drawLine(0, 500, 350, 500, fill='black', lineWidth=3)
    drawLine(350, 500, 350, 550, fill='black', lineWidth=3)
    drawLine(350, 550, 950, 550, fill='black', lineWidth=3)
    drawLine(150, 370, 700, 370, fill='black', lineWidth=3)
    drawLine(700, 370, 700, 400, fill='black', lineWidth=3)
    drawLine(700, 400, 1200, 400, fill='black', lineWidth=3)
    drawLine(0, 150, 200, 150, fill='black', lineWidth=3)
    drawLine(200, 150, 200, 250, fill='black', lineWidth=3)
    drawLine(200, 250, 750, 250, fill='black', lineWidth=3)
    drawLine(750, 250, 750, 210, fill='black', lineWidth=3)
    drawLine(750, 210, 900, 210, fill='black', lineWidth=3)
    drawLine(900, 210, 900, 250, fill='black', lineWidth=3)
    drawLine(900, 250, 1050, 250, fill='black', lineWidth=3)
    drawLine(1050, 250, 1050, 275, fill='black', lineWidth=3)
    drawLine(350, 100, 400, 100, fill='black', lineWidth=3)
    drawLine(400, 100, 400, 150, fill='black', lineWidth=3)
    drawLine(400, 150, 1200, 150, fill='black', lineWidth=3)
    # levers
    drawRect(0, 350, 150, 25, fill=rgb(253, 233, 146))
    drawLine(200, 500, 275, 500, fill=rgb(253, 233, 146), lineWidth=8)
    # buttons
    drawRect(1050, 250, 150, 25, fill='plum')
    drawLine(400, 370, 460, 370, fill='plum', lineWidth=8)
    drawLine(950, 250, 1010, 250, fill='plum', lineWidth=8)
    # pools
    drawRect(500, 780, 150, 19, fill='crimson')
    drawRect(750, 780, 150, 19, fill='deepSkyBlue')
    drawRect(630, 540, 130, 20, fill='yellowGreen')

def drawMap2(app): # CITATION: same layout as level 8 from the game
    # lines
    drawLine(0, 720, 75, 720, fill= 'black', lineWidth=3)
    drawLine(75, 720, 75, 790, fill='black', lineWidth=3)
    drawLine(75, 790, 880, 790, fill='black', lineWidth=3)
    drawLine(950, 790, 1190, 790, fill='black', lineWidth=3)
    drawLine(120, 620, 450, 620, fill='black', lineWidth=3)
    drawLine(450, 620, 450, 580, fill='black', lineWidth=3)
    drawLine(450, 580, 650, 580, fill='black', lineWidth=3)
    drawLine(650, 580, 650, 690, fill='black', lineWidth=3)
    drawLine(650, 640, 780, 640, fill='black', lineWidth=3)
    drawLine(950, 790, 950, 480, fill='black', lineWidth=3)
    drawLine(880, 790, 880, 700, fill='black', lineWidth=3)
    drawLine(880, 700, 950, 700, fill='black', lineWidth=3)
    drawLine(1190, 100, 1190, 790, fill='black', lineWidth=3)
    drawLine(1120, 100, 1190, 100, fill='black', lineWidth=3)
    drawLine(800, 480, 1000, 480, fill='black', lineWidth=3)
    drawLine(1000, 480, 1000, 300, fill='black', lineWidth=3)
    drawLine(800, 530, 800, 480, fill='black', lineWidth=3)
    drawLine(800, 530, 720, 530, fill='black', lineWidth=3)
    drawLine(100, 430, 450, 430, fill='black', lineWidth=3)
    drawLine(0, 350, 50, 350, fill='black', lineWidth=3)
    drawLine(50, 350, 50, 380, fill='black', lineWidth=3)
    drawLine(50, 380, 100, 380, fill='black', lineWidth=3)
    drawLine(100, 380, 100, 430, fill='black', lineWidth=3)
    drawLine(450, 430, 450, 400, fill='black', lineWidth=3)
    drawLine(450, 400, 500, 400, fill='black', lineWidth=3)
    drawLine(500, 400, 500, 320, fill='black', lineWidth=3)
    drawLine(500, 320, 600, 320, fill='black', lineWidth=3)
    drawLine()
    # pools
    drawRect(200, 610, 180, 20, fill='deepSkyBlue')
    drawRect(670, 630, 90, 20, fill='crimson')
    drawRect(650, 780, 150, 19, fill='crimson')

# LEFTOVER FROM TP1 (didn't get to complete)
#    drawHelpScreen function
#    finish maps
#    allow navigation through all the different screens
#    include timer
#    start sprites

# IDEAS 
#   1. can implement high score board for each level for best times (but
#      player must acquire all diamonds to qualify)
#   2. if time, can add a hint feature for harder levels


def onAppStart(app):
    app.width = 1200
    app.height = 800
    app.homeScreen = True
    app.levelScreen = False
    app.map1 = False
    app.map2 = False
    app.map3 = False
    app.time = 0

def redrawAll(app):
    '''
    if app.homeScreen:
        drawHomeScreen(app)
    if app.levelScreen:
        drawLevelScreen(app)
    if app.map1:
        drawMap1(app)
    if app.map2:
        drawMap2(app)
    if app.map3:
        drawMap3(app)
    '''
    drawMap1(app)

def onMousePress(app, mouseX, mouseY):
    if app.homeScreen:
        # play button
        if (520 < mouseX < 680) and (570 < mouseY < 630):
            app.homeScreen = False
            app.levelScreen = True
    if app.levelScreen:
        # level 1 button
        if (485 < mouseX < 715) and (300 < mouseY < 350):
            app.levelScreen = False
            app.map1 = True
        # level 2 button
        if (485 < mouseX < 715) and (425 < mouseY < 475):
            app.levelScreen = False
            app.map2 = True
        # level 3 button
        # if (485 < mouseX < 715) and (550 < mouseY < 600):
            # app.levelScreen = False
            # app.map3 = True

def onMouseMove(app, mouseX, mouseY):
    pass
    # highlight buttons when mouse hovers over them

def main():
    runApp()

main()