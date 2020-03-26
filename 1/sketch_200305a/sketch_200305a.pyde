def setup():
    size(400,600)
    point(50,50)
    rectMode(CORNER)
    
def draw():
    print(mouseX,mouseY,mousePressed)
    clear()
    
    if mousePressed:
        rect(mouseX,width,width/2,50) # warto tam gdzie można używać wartości zależnych
        c = color(255,254,0)
        fill(c)
    else:
        rect(100,400,200,50)
        w = color(255,0,0)
        fill(w)
        
# 1,75pkt
