def setup():
    size(400,600)
    frameRate(25)
    rectMode(CENTER)
    global slownik_kolorow
    slownik_kolorow = {"czerwony":(255,0,0, 80), "niebieski":(0,0,255,80), "zielony":(0,255,0,80)}
    
    global lista_kolorow
    lista_kolorow = []
    
    for k, w in slownik_kolorow.items():
        lista_kolorow.append(w)
    global x
    x = 50
    global y
    y = 300
    global dx
    dx = 2
    global dy
    dy = 3
    global iteracja
    iteracja = 0
    clear()
def draw():
    background(0)
    global dx
    global dy
    global x
    global y
    global iteracja
    iteracja +=1  
    
    fill(*lista_kolorow[iteracja%len(lista_kolorow)])
    rect(x,y,100,100)
    x += dx
    y += dy
    
    if(x > (width-50)):
        dx = -2    
    elif(x < (50)):
        dx = 2
        
    if(y > (height-50)):
        dy = -3    
    elif(y < (50)):
        dy = 3
        
    if mousePressed:
        exit()    
    
       
           
    
    
    
    
