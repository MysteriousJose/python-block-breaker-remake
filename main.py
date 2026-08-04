### TODO ###
# Add GUI selections 
# Powerups 

from cmu_graphics import *
app.dx = 0
app.dy = 0
app.background='darkGray'
ball = Circle(200,345,10)
border1= Rect(0,-50,400,60)
border2 = Rect(-50,0,60,400)
border3 = Rect(0,420,400,60)
border4 = Rect(390,0,50,400)


paddle = Rect(155,380,90,5)
paddle2 = Rect(550,380,90,5)


pColide1= Rect(155,380,11.25,5, visible=False)
pColide2= Rect(166.25,380,11.25,5, visible=False)
pColide3= Rect(177.5,380,11.25,5, visible=False)
pColide4= Rect(188.75,380,11.25,5, visible=False)
pColide5= Rect(200,380,11.25,5, visible=False)
pColide6= Rect(211.25,380,11.25,5, visible=False)
pColide7= Rect(222.5,380,11.25,5, visible=False)
pColide8= Rect(233.75,380,11.25,5, visible=False)

pColide9= Rect(155,380,11.25,5, visible=False)
pColide10= Rect(166.25,380,11.25,5, visible=False)
pColide11= Rect(177.5,380,11.25,5, visible=False)
pColide12= Rect(188.75,380,11.25,5, visible=False)
pColide13= Rect(200,380,11.25,5, visible=False)
pColide14= Rect(211.25,380,11.25,5, visible=False)
pColide15= Rect(222.5,380,11.25,5, visible=False)
pColide16= Rect(233.75,380,11.25,5, visible=False)

app.paddleRight=False
app.paddleLeft=False
app.counter = 0
gameStart=False
l = Label(app.counter,200,30, fill='white', size=25)
blockZ = 40
blockC = 30
loseMsg = Label("You Lose",200,200,fill='red', size=60, visible=False)
app.blocksInvis = 0

app.blocks={
    Rect(50,60,blockZ,blockC, fill='red'),
    Rect(102,60,blockZ,blockC, fill='red'),
    Rect(154,60,blockZ,blockC, fill='red'),
    Rect(206,60,blockZ,blockC, fill='red'),
    Rect(258,60,blockZ,blockC, fill='red'),
    Rect(310,60,blockZ,blockC, fill='red'),
    Rect(310,100,blockZ,blockC, fill='green'),
    Rect(258,100,blockZ,blockC, fill='green'),
    Rect(206,100,blockZ,blockC, fill='green'),
    Rect(154,100,blockZ,blockC, fill='green'),
    Rect(102,100,blockZ,blockC, fill='green'),
    Rect(50,100,blockZ,blockC, fill='green'),
    Rect(50,140,blockZ,blockC, fill='blue'),
    Rect(102,140,blockZ,blockC, fill='blue'),
    Rect(154,140,blockZ,blockC, fill='blue'),
    Rect(206,140,blockZ,blockC, fill='blue'),
    Rect(258,140,blockZ,blockC, fill='blue'),
    Rect(310,140,blockZ,blockC, fill='blue')
}

app.arcs = {
Group(Arc(54,64,15,15,270,90,fill='crimson'), Arc(54,86,15,15,180,90,fill='crimson'), Arc(86,86,15,15,90,90,fill='crimson'), Arc(86,64,15,15,0,90, fill='crimson')),
Group(Arc(106,64,15,15,270,90,fill='crimson'), Arc(106,86,15,15,180,90,fill='crimson'), Arc(138,86,15,15,90,90,fill='crimson'), Arc(138,64,15,15,0,90, fill='crimson')),
Group(Arc(158,64,15,15,270,90,fill='crimson'), Arc(158,86,15,15,180,90,fill='crimson'), Arc(190,86,15,15,90,90,fill='crimson'), Arc(190,64,15,15,0,90, fill='crimson')),
Group(Arc(210,64,15,15,270,90,fill='crimson'), Arc(210,86,15,15,180,90,fill='crimson'), Arc(242,86,15,15,90,90,fill='crimson'), Arc(242,64,15,15,0,90, fill='crimson')),
Group(Arc(262,64,15,15,270,90,fill='crimson'), Arc(262,86,15,15,180,90,fill='crimson'), Arc(294,86,15,15,90,90,fill='crimson'), Arc(294,64,15,15,0,90, fill='crimson')),
Group(Arc(314,64,15,15,270,90,fill='crimson'), Arc(314,86,15,15,180,90,fill='crimson'), Arc(346,86,15,15,90,90,fill='crimson'), Arc(346,64,15,15,0,90, fill='crimson')),

Group(Arc(54,104,15,15,270,90,fill='darkGreen'), Arc(54,126,15,15,180,90,fill='darkGreen'), Arc(86,126,15,15,90,90,fill='darkGreen'), Arc(86,104,15,15,0,90, fill='darkGreen')),
Group(Arc(106,104,15,15,270,90,fill='darkGreen'), Arc(106,126,15,15,180,90,fill='darkGreen'), Arc(138,126,15,15,90,90,fill='darkGreen'), Arc(138,104,15,15,0,90, fill='darkGreen')),
Group(Arc(158,104,15,15,270,90,fill='darkGreen'), Arc(158,126,15,15,180,90,fill='darkGreen'), Arc(190,126,15,15,90,90,fill='darkGreen'), Arc(190,104,15,15,0,90, fill='darkGreen')),
Group(Arc(210,104,15,15,270,90,fill='darkGreen'), Arc(210,126,15,15,180,90,fill='darkGreen'), Arc(242,126,15,15,90,90,fill='darkGreen'), Arc(242,104,15,15,0,90, fill='darkGreen')),
Group(Arc(262,104,15,15,270,90,fill='darkGreen'), Arc(262,126,15,15,180,90,fill='darkGreen'), Arc(294,126,15,15,90,90,fill='darkGreen'), Arc(294,104,15,15,0,90, fill='darkGreen')),
Group(Arc(314,104,15,15,270,90,fill='darkGreen'), Arc(314,126,15,15,180,90,fill='darkGreen'), Arc(346,126,15,15,90,90,fill='darkGreen'), Arc(346,104,15,15,0,90, fill='darkGreen')),

Group(Arc(54,144,15,15,270,90,fill='darkBlue'), Arc(54,166,15,15,180,90,fill='darkBlue'), Arc(86,166,15,15,90,90,fill='darkBlue'), Arc(86,144,15,15,0,90, fill='darkBlue')),
Group(Arc(106,144,15,15,270,90,fill='darkBlue'), Arc(106,166,15,15,180,90,fill='darkBlue'), Arc(138,166,15,15,90,90,fill='darkBlue'), Arc(138,144,15,15,0,90, fill='darkBlue')),
Group(Arc(158,144,15,15,270,90,fill='darkBlue'), Arc(158,166,15,15,180,90,fill='darkBlue'), Arc(190,166,15,15,90,90,fill='darkBlue'), Arc(190,144,15,15,0,90, fill='darkBlue')),
Group(Arc(210,144,15,15,270,90,fill='darkBlue'), Arc(210,166,15,15,180,90,fill='darkBlue'), Arc(242,166,15,15,90,90,fill='darkBlue'), Arc(242,144,15,15,0,90, fill='darkBlue')),
Group(Arc(262,144,15,15,270,90,fill='darkBlue'), Arc(262,166,15,15,180,90,fill='darkBlue'), Arc(294,166,15,15,90,90,fill='darkBlue'), Arc(294,144,15,15,0,90, fill='darkBlue')),
Group(Arc(314,144,15,15,270,90,fill='darkBlue'), Arc(314,166,15,15,180,90,fill='darkBlue'), Arc(346,166,15,15,90,90,fill='darkBlue'), Arc(346,144,15,15,0,90, fill='darkBlue')),

}

app.arcConectors ={
Group(Rect(54,57,32,7,fill='crimson'), Rect(54,86,32,7,fill='crimson'), Rect(47,64,7,24, fill='crimson'), Rect(86,64,7,24, fill='crimson')),
Group(Rect(106,57,32,7,fill='crimson'), Rect(106,86,32,7,fill='crimson'), Rect(99,64,7,24, fill='crimson'), Rect(138,64,7,24, fill='crimson')),
Group(Rect(158,57,32,7,fill='crimson'), Rect(158,86,32,7,fill='crimson'), Rect(151,64,7,24, fill='crimson'), Rect(190,64,7,24, fill='crimson')),
Group(Rect(210,57,32,7,fill='crimson'), Rect(210,86,32,7,fill='crimson'), Rect(203,64,7,24, fill='crimson'), Rect(242,64,7,24, fill='crimson')),
Group(Rect(262,57,32,7,fill='crimson'), Rect(262,86,32,7,fill='crimson'), Rect(255,64,7,24, fill='crimson'), Rect(294,64,7,24, fill='crimson')),
Group(Rect(314,57,32,7,fill='crimson'), Rect(314,86,32,7,fill='crimson'), Rect(307,64,7,24, fill='crimson'), Rect(346,64,7,24, fill='crimson')),

Group(Rect(54,97,32,7,fill='darkGreen'), Rect(54,126,32,7,fill='darkGreen'), Rect(47,104,7,24, fill='darkGreen'), Rect(86,104,7,24, fill='darkGreen')),
Group(Rect(106,97,32,7,fill='darkGreen'), Rect(106,126,32,7,fill='darkGreen'), Rect(99,104,7,24, fill='darkGreen'), Rect(138,104,7,24, fill='darkGreen')),
Group(Rect(158,97,32,7,fill='darkGreen'), Rect(158,126,32,7,fill='darkGreen'), Rect(151,104,7,24, fill='darkGreen'), Rect(190,104,7,24, fill='darkGreen')),
Group(Rect(210,97,32,7,fill='darkGreen'), Rect(210,126,32,7,fill='darkGreen'), Rect(203,104,7,24, fill='darkGreen'), Rect(242,104,7,24, fill='darkGreen')),
Group(Rect(262,97,32,7,fill='darkGreen'), Rect(262,126,32,7,fill='darkGreen'), Rect(255,104,7,24, fill='darkGreen'), Rect(294,104,7,24, fill='darkGreen')),
Group(Rect(314,97,32,7,fill='darkGreen'), Rect(314,126,32,7,fill='darkGreen'), Rect(307,104,7,24, fill='darkGreen'), Rect(346,104,7,24, fill='darkGreen')),

Group(Rect(54,137,32,7,fill='darkBlue'), Rect(54,166,32,7,fill='darkBlue'), Rect(47,144,7,24, fill='darkBlue'), Rect(86,144,7,24, fill='darkBlue')),
Group(Rect(106,137,32,7,fill='darkBlue'), Rect(106,166,32,7,fill='darkBlue'), Rect(99,144,7,24, fill='darkBlue'), Rect(138,144,7,24, fill='darkBlue')),
Group(Rect(158,137,32,7,fill='darkBlue'), Rect(158,166,32,7,fill='darkBlue'), Rect(151,144,7,24, fill='darkBlue'), Rect(190,144,7,24, fill='darkBlue')),
Group(Rect(210,137,32,7,fill='darkBlue'), Rect(210,166,32,7,fill='darkBlue'), Rect(203,144,7,24, fill='darkBlue'), Rect(242,144,7,24, fill='darkBlue')),
Group(Rect(262,137,32,7,fill='darkBlue'), Rect(262,166,32,7,fill='darkBlue'), Rect(255,144,7,24, fill='darkBlue'), Rect(294,144,7,24, fill='darkBlue')),
Group(Rect(314,137,32,7,fill='darkBlue'), Rect(314,166,32,7,fill='darkBlue'), Rect(307,144,7,24, fill='darkBlue'), Rect(346,144,7,24, fill='darkBlue')),
}

def onMousePress(x,y):
    app.dx=randrange(-6,6)
    app.dy=-6
    gameStart=False
    pass

def onStep():
    if(paddle2.centerX>555):
        paddle2.centerX=-245
    if(paddle.centerX>555):
        paddle.centerX=-245
    if(paddle2.centerX<-245):
        paddle2.centerX=555
    if(paddle.centerX<-245):
        paddle.centerX=555
    
    l.value=app.counter
    pColide1.left = paddle.left
    pColide2.left = paddle.left+11.25
    pColide3.left = paddle.left+22.5
    pColide4.left = paddle.left+33.75
    pColide5.left = paddle.left+45
    pColide6.left = paddle.left+56.25
    pColide7.left = paddle.left+67.5
    pColide8.right = paddle.right
    pColide9.left = paddle2.left
    pColide10.left = paddle2.left+11.25
    pColide11.left = paddle2.left+22.5
    pColide12.left = paddle2.left+33.75
    pColide13.left = paddle2.left+45
    pColide14.left = paddle2.left+56.25
    pColide15.left = paddle2.left+67.5
    pColide16.right = paddle2.right
    #if app.blocksInvis == 18:
     #   app.counter+=1
        
    ball.centerX+=app.dx
    ball.centerY+=app.dy
    #paddle.centerX=ball.centerX#+randrange(-79,79) # uncomment for commputer
    #paddle2.centerX=400-ball.centerX
    
    if ball.centerX>400:
        ball.centerX=0
    if ball.centerX<0:
        ball.centerX=400
        
    if ball.centerY>399:
        loseMsg.visible=True
        sleep(0.5)
        loseMsg.visible=False
        reset()
    if app.blocksInvis==19:
        app.blocksInvis=1
        app.dy+=1
    if app.dy>12:
        app.dy=12
    if app.paddleLeft==True:
        paddle.centerX-=12
    if app.paddleRight==True:
        paddle.centerX+=12
    if ball.hitsShape(border1):
        app.dy=abs(app.dy)
    if ball.hitsShape(border3):
        app.dx=0
        app.dy=0
        ball.centerX=200
        ball.centerY=345
        ball.visible=True
        loseMsg.visible=True
        sleep(0.5)
        loseMsg.visible=False
        reset()
        
        pass
    #if ball.hitsShape(border2):
     #   app.dx=randrange(1,6)
    #if ball.hitsShape(border4):
     #   app.dx=randrange(-6,-1)
    if gameStart==True:
        if ball.hitsShape(pColide1):
            app.dy=-6           
            app.dx=-6
        if ball.hitsShape(pColide2):
            app.dy=-6
            app.dx=-4.375
        if ball.hitsShape(pColide3):
            app.dy=-6
            app.dx=-2.75
        if ball.hitsShape(pColide4):
            app.dy=-6
            app.dx=-1.125
        if ball.hitsShape(pColide5):
            app.dy=-6
            app.dx=0.5
        if ball.hitsShape(pColide6):
            app.dy=-6
            app.dx=2.125
        if ball.hitsShape(pColide7):
            app.dy=-6
            app.dx=3.75
        if ball.hitsShape(pColide8):
            app.dy=-6
            app.dx=5.375
        if ball.hitsShape(pColide9):
            app.dy=-6           
            app.dx=-6
        if ball.hitsShape(pColide10):
            app.dy=-6
            app.dx=-4.375
        if ball.hitsShape(pColide11):
            app.dy=-6
            app.dx=-2.75
        if ball.hitsShape(pColide12):
            app.dy=-6
            app.dx=-1.125
        if ball.hitsShape(pColide13):
            app.dy=-6
            app.dx=0.5
        if ball.hitsShape(pColide14):
            app.dy=-6
            app.dx=2.125
        if ball.hitsShape(pColide15):
            app.dy=-6
            app.dx=3.75
        if ball.hitsShape(pColide16):
            app.dy=-6
            app.dx=5.375
    if gameStart==False:
        if ball.hitsShape(paddle) or ball.hitsShape(paddle2):
            app.dy=-abs(app.dy)
            app.dx=randrange(-6,6)
    for block in app.blocks:
        if block.visible and ball.hitsShape(block):
            app.dy=app.dy*-1
            block.visible=False
            app.blocksInvis+=1
    
    for group in app.arcs:
        if group.visible and ball.hitsShape(group):
            group.visible=False
        
    for group in app.arcConectors:
        if group.visible and ball.hitsShape(group):
            group.visible=False
    
    if app.blocksInvis==18 and ball.hitsShape(paddle) or app.blocksInvis==18 and ball.hitsShape(paddle2):
        app.counter+=1
        app.dy-=1
        for block in app.blocks:
            block.visible=True
        for arc in app.arcs:
            arc.visible=True
        for rect in app.arcConectors:
            rect.visible=True
        
        app.blocksInvis=0
        
def reset():
    ball.centerX=200
    ball.centerY=345
    app.dx=0
    app.dy=0
    app.blocksInvis=0
    app.counter=0
    paddle.x1=155
    for group in app.arcConectors:
        group.visible=True
    for group in app.arcs:
        group.visible=True
    for block in app.blocks:
        block.visible=True
def onKeyPress(key):
    if key == 'w':
        app.dx=randrange(-6,6)
        app.dy=-6
        gameStart=True
    if key == 'up':
        app.dx=randrange(-6,6)
        app.dy=-6
        gameStart=True
    if key =='r':
        reset()
def onKeyHold(keys):
    if 'a' in keys:
        paddle.centerX-=10
        paddle2.centerX-=10
    if 'd' in keys:
        paddle.centerX+=10
        paddle2.centerX+=10

#def onMouseMove(x,y):
 #   paddle.centerX=x
#def onMouseDrag(x,y):
 #   paddle.centerX=x

cmu_graphics.run()