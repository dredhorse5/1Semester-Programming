def setup():
    size(500,500)
    background(0)

def draw():
    colorMode(HSB, width, height,100)
    if frameCount == 1:
        stepX = 0
        stepY = 0
        gridY = 0
        gridX = 0
    stepX = mouseX + 2
    stepY = mouseY + 2
    
    while gridY < height:
        gridY += stepY
        
        while gridX < width:
            stroke(gridX, height-gridY, 100)
            strokeWeight(stepX)
            line(gridX, gridY, stepX+gridX, stepY + gridY)
            
