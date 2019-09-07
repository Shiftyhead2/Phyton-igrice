from tkinter import*
import turtle
import time
import random
import pickle
import os
import winsound

d = 0.1

#Zmija
def zmija():
    delay = d
    #Score
    Score = 0
    if os.path.isfile('Snake.data'): #Provjerava dali postoji ova datoteka
        HighScore = pickle.load(open('Snake.data','rb')) #Ako postoji onda učitava tu datoteku
    else:
       HighScore = 0 #ako ne postoji onda stavlja ovu variablu kao nula
    
    #Program
    gn = turtle.Screen()
    gn.title('Zmija')
    gn.bgcolor('black')
    gn.setup(width = 600 , height = 600)
    gn.tracer(0)
    

    #Olovka
    olovka = turtle.Turtle()
    olovka.speed(0)
    olovka.shape('square')
    olovka.color('white')
    olovka.penup()
    olovka.hideturtle()
    olovka.goto(0,260)
    olovka.write('Score: {}  HighScore: {}'.format(Score,HighScore),align = 'center',font =('Courier',14,'normal'))

    #Glava
    glava = turtle.Turtle()
    glava.speed(0)
    glava.shape('square')
    glava.color('white')
    glava.penup()
    glava.goto(0,0)
    glava.direction = 'stop'

    #Hrana
    hrana = turtle.Turtle()
    hrana.speed(0)
    hrana.shape('circle')
    hrana.color('red')
    hrana.penup()
    hrana.goto(0,100)

    

    dijelovi = []

    #Funkcije
    def idi_gore():
        if glava.direction != 'down':
            glava.direction = 'up'

    def idi_dolje():
        if glava.direction != 'up':
            glava.direction = 'down'

    def idi_lijevo():
        if glava.direction != 'right':
            glava.direction = 'left'

    def idi_desno():
        if glava.direction != 'left':
            glava.direction = 'right'


    def kretanje():
        if glava.direction == 'up':
            y = glava.ycor()
            glava.sety(y+20)
        if glava.direction == 'down':
            y = glava.ycor()
            glava.sety(y-20)
        if glava.direction == 'left':
            x = glava.xcor()
            glava.setx(x+20)
        if glava.direction == 'right':
            x = glava.xcor()
            glava.setx(x-20)




     
    #Tipkovnica
    gn.listen()
    gn.onkeypress(idi_gore,'w')
    gn.onkeypress(idi_dolje,'s')
    gn.onkeypress(idi_desno,'a')
    gn.onkeypress(idi_lijevo,'d')

    #Igra loop
    while True:
        gn.update()
        time.sleep(delay)

        #Udaranje u zid
        if glava.xcor()>290 or glava.xcor() < -290 or glava.ycor() > 290 or glava.ycor() < -290:
            winsound.PlaySound('Hit_Hurt.wav',winsound.SND_ASYNC)
            time.sleep(1)
            glava.goto(0,0)
            glava.direction = 'stop'

            for dio in dijelovi:
                dio.goto(1000,1000)

            dijelovi.clear()

            #Izgubi bodove
            Score = 0
            olovka.clear()
            olovka.write('Score: {}  HighScore: {}'.format(Score,HighScore),align = 'center', font =('Courier',14,'normal'))
            
            delay = 0.1

            

        #Zmija pojede hranu   
        if glava.distance(hrana) < 20:
            #Hrana ide negdje
            x = random.randint(-290,290)
            y = random.randint(-290,290)
            hrana.goto(x,y)

            novi_dio = turtle.Turtle()
            novi_dio.speed(0)
            novi_dio.shape('square')
            novi_dio.color('white')
            novi_dio.penup()
            dijelovi.append(novi_dio)

            #Dobije bodove
            Score += 10

            if Score >= HighScore:
                HighScore = Score
                pickle.dump(HighScore,open('Snake.data','wb')) #Spremanje highscora
            
            olovka.clear()
            olovka.write('Score: {}  HighScore: {}'.format(Score,HighScore),align = 'center', font =('Courier',14,'normal'))
            winsound.PlaySound('Eat.wav',winsound.SND_ASYNC)
            
            delay -= 0.001


        #Kretanje dijelova
        for index in range(len(dijelovi)-1,0,-1):
            x = dijelovi[index -1].xcor()
            y = dijelovi[index-1].ycor()
            dijelovi[index].goto(x,y)

        if len(dijelovi) > 0:
            x = glava.xcor()
            y = glava.ycor()
            dijelovi[0].goto(x,y)
            
        kretanje()

        #Zmija udari sebe
        for dio in dijelovi:
            if dio.distance(glava) < 20:
                winsound.PlaySound('Hit_Hurt.wav',winsound.SND_ASYNC)
                time.sleep(1)
                glava.goto(0,0)
                glava.direction = 'stop'

                for dio in dijelovi:
                    dio.goto(1000,1000)

                dijelovi.clear()


                #Izgubi bodove
                Score = 0
                olovka.clear()
                olovka.write('Score: {}  HighScore: {}'.format(Score,HighScore),align = 'center', font =('Courier',14,'normal'))
                
                delay = 0.1
                

        


    gn.mainloop()

#Pong
def pong():

    #Pong prozor
    pn = turtle.Screen()
    pn.title('Pong')
    pn.bgcolor('black')
    pn.setup(width = 800 , height = 600)
    pn.tracer(0)

    #Bodovi
    bodovi_a = 0
    bodovi_b = 0

    #Igrač A
    igrac_a = turtle.Turtle()
    igrac_a.speed(0)
    igrac_a.shape('square')
    igrac_a.color('white')
    igrac_a.shapesize(stretch_wid = 5,stretch_len = 1)
    igrac_a.penup()
    igrac_a.goto(-350,0)

    #Igrač B
    igrac_b = turtle.Turtle()
    igrac_b.speed(0)
    igrac_b.shape('square')
    igrac_b.color('white')
    igrac_b.shapesize(stretch_wid = 5,stretch_len = 1)
    igrac_b.penup()
    igrac_b.goto(350,0)

    #Lopta
    lopta = turtle.Turtle()
    lopta.speed(0)
    lopta.shape('square')
    lopta.color('white')
    lopta.penup()
    lopta.goto(0,0)
    lopta.dx = 15
    lopta.dy = 15

    #Olovka
    olovka = turtle.Turtle()
    olovka.speed(0)
    olovka.color('white')
    olovka.penup()
    olovka.hideturtle()
    olovka.goto(0,260)
    olovka.write('Igrač A: 0 Igrač B: 0',align = 'center',font=('Courier',14,'normal'))

    #Funkcije
    def igrac_a_gore():
        y = igrac_a.ycor()
        y += 20
        igrac_a.sety(y)
    def igrac_a_dolje():
        y = igrac_a.ycor()
        y -= 20
        igrac_a.sety(y)
    def igrac_b_gore():
        y = igrac_b.ycor()
        y += 20
        igrac_b.sety(y)
    def igrac_b_dolje():
        y = igrac_b.ycor()
        y -= 20
        igrac_b.sety(y)

    #Tipkovnica
    pn.listen()
    pn.onkeypress(igrac_a_gore,'w')
    pn.onkeypress(igrac_a_dolje,'s')
    pn.onkeypress(igrac_b_gore,'Up')
    pn.onkeypress(igrac_b_dolje,'Down')
    
    
    #Loop
    while True:
        pn.update()

        #Kretanje lopte
        lopta.setx(lopta.xcor()+lopta.dx)
        lopta.sety(lopta.ycor()+lopta.dy)
        

        #Provjeri dali udaramo zid
        if lopta.ycor() > 290:
            lopta.sety(290)
            lopta.dy *= -1
            winsound.PlaySound('bounce.wav',winsound.SND_ASYNC)
            
        if lopta.ycor() < -290:
            lopta.sety(-290)
            lopta.dy *= -1
            winsound.PlaySound('bounce.wav',winsound.SND_ASYNC)
            
        if lopta.xcor() > 390:
            lopta.goto(0,0)
            lopta.dx *= -1
            bodovi_a += 1
            olovka.clear()
            olovka.write('Igrač A: {} Igrač B: {}'.format(bodovi_a,bodovi_b),align = 'center',font=('Courier',14,'normal'))
            
        if lopta.xcor() < -390:
            lopta.goto(0,0)
            lopta.dx *= -1
            bodovi_b += 1
            olovka.clear()
            olovka.write('Igrač A: {} Igrač B: {}'.format(bodovi_a,bodovi_b),align = 'center',font=('Courier',14,'normal'))

        #Provjeri dali udaramo igrače
        if (lopta.xcor() > 340 and lopta.xcor() < 360) and (lopta.ycor() < igrac_b.ycor() + 40 and lopta.ycor() > igrac_b.ycor() -40):
            lopta.setx(340)
            lopta.dx *= -1
            winsound.PlaySound('bounce.wav',winsound.SND_ASYNC)
        if (lopta.xcor() < -340 and lopta.xcor() > -360) and (lopta.ycor() < igrac_a.ycor() + 40 and lopta.ycor() > igrac_a.ycor() -40):
            lopta.setx(-340)
            lopta.dx *= -1
            winsound.PlaySound('bounce.wav',winsound.SND_ASYNC)

        time.sleep(d)
            
    pn.mainloop() 
        


#GUI prozor
t = Tk()
t.title('Igrice')
t.config(bg = 'black',width = 200 , height = 200)

#gumb za otvaranje igrice Zmija
gS = Button(t,text = 'Zmija',bg = 'black' , fg = 'white',command = zmija)
gS.place(x=0,y=0)
#Gumb za otvaranje igrice Pong
gP = Button(t,text = 'Pong',bg = 'black' , fg = 'white',command = pong)
gP.place(x=50,y=0)
t.mainloop()


