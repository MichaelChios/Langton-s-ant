# Langton's ant by Michael Stefanioros ( up1072774 )

import turtle as t
import tkinter as tk

posandcolor = {} # the position and the color of the ant
root1= tk.Tk()
root1.geometry('50x50+1150+20')

root1.counter=0

SV=tk.StringVar()
L= tk.Label (root1, textvariable=SV)
L.pack()  

stop_flag=False                                                

def stop_button_pressed():                                     
    global stop_flag                                
    stop_flag=True  

B1=tk.Button(root1, text="STOP", command=stop_button_pressed)
B1.pack()

def version1():
    global exit_signal, ant
    root2.destroy()
    # Creating the window
    window = t.Screen()
    window.bgcolor("white")
    window.screensize(1000,1000)

    # Creating ant
    ant = t.Turtle()
    ant.shape("square")
    ant.shapesize(0.5)
    ant.speed(1000000)
    pos=position(ant)

    step=10
    while(True):
        if stop_flag: break
        if pos not in posandcolor or posandcolor[pos] =="white" :
            ant.fillcolor("black")
            ant.stamp()
            change(posandcolor, ant,"black")
            ant.right(90)
            ant.forward(step)
            pos=position(ant)
            root1.counter+=1
                
        elif posandcolor[pos] =="black" :
            ant.fillcolor("white")
            ant.stamp()
            change(posandcolor, ant,"white")
            ant.left(90)
            ant.forward(step)
            pos=position(ant)
            root1.counter+=1

        SV.set('Movements : '  + str(root1.counter))

def version2a():
    global exit_signal
    root2.destroy()
    # Creating the window
    window = t.Screen()
    window.bgcolor("white")
    window.screensize(1000,1000)

    # Creating ant
    ant = t.Turtle()
    ant.shape("square")
    ant.shapesize(0.5)
    ant.speed(100000)
    ant.left(90)
    pos=position(ant)

    step=10
    while(True):
        if stop_flag: break                                     
        if pos not in posandcolor or posandcolor[pos] =="green" :
            ant.fillcolor("black")
            ant.stamp()
            change(posandcolor, ant,"black")
            ant.right(90)
            ant.forward(step)
            pos=position(ant)
            root1.counter+=1
            
        elif posandcolor[pos] =="black" :
            ant.fillcolor("purple")
            ant.stamp()
            change(posandcolor, ant,"purple")
            ant.left(90)
            ant.forward(step)
            pos=position(ant)
            root1.counter+=1

        elif posandcolor[pos] =="purple" :
            ant.fillcolor("green")
            ant.stamp()
            change(posandcolor, ant,"green")
            ant.right(90)
            ant.forward(step)
            pos=position(ant)
            root1.counter+=1

        SV.set('Movements : ' + str(root1.counter))

def version2b():
    global exit_signal
    root2.destroy()
    # Creating the window
    window = t.Screen()
    window.bgcolor("white")
    window.screensize(1000,1000)

    # Creating ant
    ant = t.Turtle()
    ant.shape("square")
    ant.shapesize(0.5)
    ant.speed(1000000)
    pos=position(ant)

    step=10
    while(True):
        if stop_flag: break                                     
        if pos not in posandcolor or posandcolor[pos] =="green" :
            ant.fillcolor("black")
            ant.stamp()
            change(posandcolor, ant,"black")
            ant.right(90)
            ant.forward(step)
            pos=position(ant)
            root1.counter+=1
            
        elif posandcolor[pos] =="black" :
            ant.fillcolor("purple")
            ant.stamp()
            change(posandcolor, ant,"purple")
            ant.right(90)
            ant.forward(step)
            pos=position(ant)
            root1.counter+=1

        elif posandcolor[pos] =="purple" :
            ant.fillcolor("green")
            ant.stamp()
            change(posandcolor, ant,"green")
            ant.left(90)
            ant.forward(step)
            pos=position(ant)
            root1.counter+=1

        SV.set('Movements : ' + str(root1.counter))

def version3():
    global exit_signal
    root2.destroy()
    # Creating the window
    window = t.Screen()
    window.bgcolor("white")
    window.screensize(1000,1000)

    # Creating ant
    ant = t.Turtle()
    ant.shape("square")
    ant.shapesize(0.5)
    ant.speed(10000)
    pos=position(ant)

    step=10
    while(True):
        if stop_flag: break                                     
        if pos not in posandcolor or posandcolor[pos] =="yellow" :
            ant.fillcolor("black")
            ant.stamp()
            change(posandcolor, ant,"black")
            ant.left(90)
            ant.forward(step)
            pos=position(ant)
            root1.counter+=1
            
        elif posandcolor[pos] =="black" :
            ant.fillcolor("purple")
            ant.stamp()
            change(posandcolor, ant,"purple")
            ant.left(90)
            ant.forward(step)
            pos=position(ant)
            root1.counter+=1

        elif posandcolor[pos] =="purple" :
            ant.fillcolor("green")
            ant.stamp()
            change(posandcolor, ant,"green")
            ant.right(90)
            ant.forward(step)
            pos=position(ant)
            root1.counter+=1

        elif posandcolor[pos] =="green" :
            ant.fillcolor("yellow")
            ant.stamp()
            change(posandcolor, ant,"yellow")
            ant.right(90)
            ant.forward(step)
            pos=position(ant)
            root1.counter+=1

        SV.set('Movements : ' + str(root1.counter))

def version4():
    global exit_signal
    root2.destroy()
    # Creating the window
    window = t.Screen()
    window.bgcolor("white")
    window.screensize(1000,1000)

    # Creating ant
    ant = t.Turtle()
    ant.shape("square")
    ant.shapesize(0.5)
    ant.speed(1000000)
    pos=position(ant)

    step=10
    while(True):
        if stop_flag: break                                     
        if pos not in posandcolor or posandcolor[pos] =="seagreen" :
            ant.fillcolor("black")
            ant.stamp()
            change(posandcolor, ant,"black")
            ant.left(90)
            ant.forward(step)
            pos=position(ant)
            root1.counter+=1
            
        elif posandcolor[pos] =="black" :
            ant.fillcolor("purple")
            ant.stamp()
            change(posandcolor, ant,"purple")
            ant.right(90)
            ant.forward(step)
            pos=position(ant)
            root1.counter+=1

        elif posandcolor[pos] =="purple" :
            ant.fillcolor("green")
            ant.stamp()
            change(posandcolor, ant,"green")
            ant.right(90)
            ant.forward(step)
            pos=position(ant)
            root1.counter+=1

        elif posandcolor[pos] =="green" :
            ant.fillcolor("yellow")
            ant.stamp()
            change(posandcolor, ant,"yellow")
            ant.right(90)
            ant.forward(step)
            pos=position(ant)
            root1.counter+=1

        elif posandcolor[pos] =="yellow" :
            ant.fillcolor("white")
            ant.stamp()
            change(posandcolor, ant,"white")
            ant.right(90)
            ant.forward(step)
            pos=position(ant)
            root1.counter+=1

        elif posandcolor[pos] =="white" :
            ant.fillcolor("red")
            ant.stamp()
            change(posandcolor, ant,"red")
            ant.right(90)
            ant.forward(step)
            pos=position(ant)
            root1.counter+=1

        elif posandcolor[pos] =="red" :
            ant.fillcolor("grey")
            ant.stamp()
            change(posandcolor, ant,"grey")
            ant.left(90)
            ant.forward(step)
            pos=position(ant)
            root1.counter+=1

        elif posandcolor[pos] =="grey" :
            ant.fillcolor("pink")
            ant.stamp()
            change(posandcolor, ant,"pink")
            ant.left(90)
            ant.forward(step)
            pos=position(ant)
            root1.counter+=1

        elif posandcolor[pos] =="pink" :
            ant.fillcolor("seagreen")
            ant.stamp()
            change(posandcolor, ant,"seagreen")
            ant.right(90)
            ant.forward(step)
            pos=position(ant)
            root1.counter+=1

        SV.set('Movements : ' + str(root1.counter))

def version5():
    global exit_signal
    root2.destroy()
    # Creating the window
    window = t.Screen()
    window.bgcolor("white")
    window.screensize(1000,1000)

    # Creating ant
    ant = t.Turtle()
    ant.shape("square")
    ant.shapesize(0.5)
    ant.speed(1000000)
    ant.right(90)
    pos=position(ant)

    step=10
    while(True):
        if stop_flag: break                                     
        if pos not in posandcolor or posandcolor[pos] =="darkmagenta" :
            ant.fillcolor("black")
            ant.stamp()
            change(posandcolor, ant,"black")
            ant.left(90)
            ant.forward(step)
            pos=position(ant)
            root1.counter+=1
            
        elif posandcolor[pos] =="black" :
            ant.fillcolor("purple")
            ant.stamp()
            change(posandcolor, ant,"purple")
            ant.left(90)
            ant.forward(step)
            pos=position(ant)
            root1.counter+=1

        elif posandcolor[pos] =="purple" :
            ant.fillcolor("green")
            ant.stamp()
            change(posandcolor, ant,"green")
            ant.right(90)
            ant.forward(step)
            pos=position(ant)
            root1.counter+=1

        elif posandcolor[pos] =="green" :
            ant.fillcolor("yellow")
            ant.stamp()
            change(posandcolor, ant,"yellow")
            ant.right(90)
            ant.forward(step)
            pos=position(ant)
            root1.counter+=1

        elif posandcolor[pos] =="yellow" :
            ant.fillcolor("white")
            ant.stamp()
            change(posandcolor, ant,"white")
            ant.right(90)
            ant.forward(step)
            pos=position(ant)
            root1.counter+=1

        elif posandcolor[pos] =="white" :
            ant.fillcolor("red")
            ant.stamp()
            change(posandcolor, ant,"red")
            ant.left(90)
            ant.forward(step)
            pos=position(ant)
            root1.counter+=1

        elif posandcolor[pos] =="red" :
            ant.fillcolor("grey")
            ant.stamp()
            change(posandcolor, ant,"grey")
            ant.right(90)
            ant.forward(step)
            pos=position(ant)
            root1.counter+=1

        elif posandcolor[pos] =="grey" :
            ant.fillcolor("pink")
            ant.stamp()
            change(posandcolor, ant,"pink")
            ant.left(90)
            ant.forward(step)
            pos=position(ant)
            root1.counter+=1

        elif posandcolor[pos] =="pink" :
            ant.fillcolor("seagreen")
            ant.stamp()
            change(posandcolor, ant,"seagreen")
            ant.right(90)
            ant.forward(step)
            pos=position(ant)
            root1.counter+=1

        elif posandcolor[pos] =="seagreen" :
            ant.fillcolor("orange")
            ant.stamp()
            change(posandcolor, ant,"orange")
            ant.left(90)
            ant.forward(step)
            pos=position(ant)
            root1.counter+=1

        elif posandcolor[pos] =="orange" :
            ant.fillcolor("dimgrey")
            ant.stamp()
            change(posandcolor, ant,"dimgrey")
            ant.left(90)
            ant.forward(step)
            pos=position(ant)
            root1.counter+=1

        elif posandcolor[pos] =="dimgrey" :
            ant.fillcolor("darkmagenta")
            ant.stamp()
            change(posandcolor, ant,"darkmagenta")
            ant.right(90)
            ant.forward(step)
            pos=position(ant)
            root1.counter+=1

        SV.set('Movements : ' + str(root1.counter))

def version6():
    global exit_signal
    root2.destroy()
    # Creating the window
    window = t.Screen()
    window.bgcolor("white")
    window.screensize(1000,1000)

    # Creating ant
    ant = t.Turtle()
    ant.shape("square")
    ant.shapesize(0.5)
    ant.speed(1000000)
    pos=position(ant)

    step=10
    while(True):
        if stop_flag: break                                     
        if pos not in posandcolor or posandcolor[pos] =="darkmagenta" :
            ant.fillcolor("black")
            ant.stamp()
            change(posandcolor, ant,"black")
            ant.right(90)
            ant.forward(step)
            pos=position(ant)
            root1.counter+=1
            
        elif posandcolor[pos] =="black" :
            ant.fillcolor("purple")
            ant.stamp()
            change(posandcolor, ant,"purple")
            ant.right(90)
            ant.forward(step)
            pos=position(ant)
            root1.counter+=1

        elif posandcolor[pos] =="purple" :
            ant.fillcolor("green")
            ant.stamp()
            change(posandcolor, ant,"green")
            ant.left(90)
            ant.forward(step)
            pos=position(ant)
            root1.counter+=1

        elif posandcolor[pos] =="green" :
            ant.fillcolor("yellow")
            ant.stamp()
            change(posandcolor, ant,"yellow")
            ant.left(90)
            ant.forward(step)
            pos=position(ant)
            root1.counter+=1

        elif posandcolor[pos] =="yellow" :
            ant.fillcolor("white")
            ant.stamp()
            change(posandcolor, ant,"white")
            ant.left(90)
            ant.forward(step)
            pos=position(ant)
            root1.counter+=1

        elif posandcolor[pos] =="white" :
            ant.fillcolor("red")
            ant.stamp()
            change(posandcolor, ant,"red")
            ant.right(90)
            ant.forward(step)
            pos=position(ant)
            root1.counter+=1

        elif posandcolor[pos] =="red" :
            ant.fillcolor("grey")
            ant.stamp()
            change(posandcolor, ant,"grey")
            ant.left(90)
            ant.forward(step)
            pos=position(ant)
            root1.counter+=1

        elif posandcolor[pos] =="grey" :
            ant.fillcolor("pink")
            ant.stamp()
            change(posandcolor, ant,"pink")
            ant.left(90)
            ant.forward(step)
            pos=position(ant)
            root1.counter+=1

        elif posandcolor[pos] =="pink" :
            ant.fillcolor("seagreen")
            ant.stamp()
            change(posandcolor, ant,"seagreen")
            ant.left(90)
            ant.forward(step)
            pos=position(ant)
            root1.counter+=1

        elif posandcolor[pos] =="seagreen" :
            ant.fillcolor("orange")
            ant.stamp()
            change(posandcolor, ant,"orange")
            ant.right(90)
            ant.forward(step)
            pos=position(ant)
            root1.counter+=1

        elif posandcolor[pos] =="orange" :
            ant.fillcolor("dimgrey")
            ant.stamp()
            change(posandcolor, ant,"dimgrey")
            ant.right(90)
            ant.forward(step)
            pos=position(ant)
            root1.counter+=1

        elif posandcolor[pos] =="dimgrey" :
            ant.fillcolor("darkmagenta")
            ant.stamp()
            change(posandcolor, ant,"darkmagenta")
            ant.right(90)
            ant.forward(step)
            pos=position(ant)
            root1.counter+=1

        SV.set('Movements : ' + str(root1.counter))

def version7():
    global exit_signal
    root2.destroy()
    # Creating the window
    window = t.Screen()
    window.bgcolor("white")
    window.screensize(10000,10000)

    # Creating ant
    ant = t.Turtle()
    ant.shape("square")
    ant.shapesize(0.5)
    ant.speed(1000000)
    pos=position(ant)

    step=10
    while(True):
        if stop_flag: break                                     
        if pos not in posandcolor or posandcolor[pos] =="navajowhite" :
            ant.fillcolor("darkorange")
            ant.stamp()
            change(posandcolor, ant,"darkorange")
            ant.left(120)
            ant.forward(step)
            pos=position(ant)
            root1.counter+=1
            
        elif posandcolor[pos] =="darkorange" :
            ant.fillcolor("orange")
            ant.stamp()
            change(posandcolor, ant,"orange")
            ant.forward(step)
            pos=position(ant)
            root1.counter+=1

        elif posandcolor[pos] =="orange" :
            ant.fillcolor("red")
            ant.stamp()
            change(posandcolor, ant,"red")
            ant.forward(step)
            pos=position(ant)
            root1.counter+=1

        elif posandcolor[pos] =="red" :
            ant.fillcolor("goldenrod")
            ant.stamp()
            change(posandcolor, ant,"goldenrod")
            ant.left(60)
            ant.forward(step)
            pos=position(ant)
            root1.counter+=1

        elif posandcolor[pos] =="goldenrod" :
            ant.fillcolor("orangered")
            ant.stamp()
            change(posandcolor, ant,"orangered")
            ant.left(120)
            ant.forward(step)
            pos=position(ant)
            root1.counter+=1

        elif posandcolor[pos] =="orangered" :
            ant.fillcolor("navajowhite")
            ant.stamp()
            change(posandcolor, ant,"navajowhite")
            ant.left(60)
            ant.forward(step)
            pos=position(ant)
            root1.counter+=1

        SV.set('Movements : ' + str(root1.counter))

def version8():
    global exit_signal
    root2.destroy()
    # Creating the window
    window = t.Screen()
    window.bgcolor("white")
    window.screensize(10000,10000)

    # Creating ant
    ant = t.Turtle()
    ant.shape("square")
    ant.shapesize(0.5)
    ant.speed(1000000)
    pos=position(ant)

    step=10
    while(True):
        if stop_flag: break                                     
        if pos not in posandcolor or posandcolor[pos] =="blue" :
            ant.fillcolor("royalblue")
            ant.stamp()
            change(posandcolor, ant,"royalblue")
            ant.left(60)
            ant.forward(step)
            pos=position(ant)
            root1.counter+=1
            
        elif posandcolor[pos] =="royalblue" :
            ant.fillcolor("cornflowerblue")
            ant.stamp()
            change(posandcolor, ant,"cornflowerblue")
            ant.left(120)
            ant.forward(step)
            pos=position(ant)
            root1.counter+=1

        elif posandcolor[pos] =="cornflowerblue" :
            ant.fillcolor("midnightblue")
            ant.stamp()
            change(posandcolor, ant,"midnightblue")
            ant.forward(step)
            pos=position(ant)
            root1.counter+=1

        elif posandcolor[pos] =="midnightblue" :
            ant.fillcolor("navy")
            ant.stamp()
            change(posandcolor, ant,"navy")
            ant.left(180)
            ant.forward(step)
            pos=position(ant)
            root1.counter+=1

        elif posandcolor[pos] =="navy" :
            ant.fillcolor("darkblue")
            ant.stamp()
            change(posandcolor, ant,"darkblue")
            ant.left(120)
            ant.forward(step)
            pos=position(ant)
            root1.counter+=1

        elif posandcolor[pos] =="darkblue" :
            ant.fillcolor("mediumblue")
            ant.stamp()
            change(posandcolor, ant,"mediumblue")
            ant.left(60)
            ant.forward(step)
            pos=position(ant)
            root1.counter+=1

        elif posandcolor[pos] =="mediumblue" :
            ant.fillcolor("blue")
            ant.stamp()
            change(posandcolor, ant,"blue")
            ant.right(120)
            ant.forward(step)
            pos=position(ant)
            root1.counter+=1

        SV.set('Movements : ' + str(root1.counter))

def version9():
    global exit_signal
    root2.destroy()
    # Creating the window
    window = t.Screen()
    window.bgcolor("white")
    window.screensize(10000,10000)

    # Creating ant
    ant = t.Turtle()
    ant.shape("square")
    ant.shapesize(0.5)
    ant.speed(1000000)
    pos=position(ant)

    step=10
    while(True):
        if stop_flag: break                                     
        if pos not in posandcolor or posandcolor[pos] =="darkgreen" :
            ant.fillcolor("forestgreen")
            ant.stamp()
            change(posandcolor, ant,"forestgreen")
            ant.right(60)
            ant.forward(step)
            pos=position(ant)
            root1.counter+=1
            
        elif posandcolor[pos] =="forestgreen" :
            ant.fillcolor("limegreen")
            ant.stamp()
            change(posandcolor, ant,"limegreen")
            ant.right(120)
            ant.forward(step)
            pos=position(ant)
            root1.counter+=1

        elif posandcolor[pos] =="limegreen" :
            ant.fillcolor("green")
            ant.stamp()
            change(posandcolor, ant,"green")
            ant.forward(step)
            pos=position(ant)
            root1.counter+=1

        elif posandcolor[pos] =="green" :
            ant.fillcolor("seagreen")
            ant.stamp()
            change(posandcolor, ant,"seagreen")
            ant.right(180)
            ant.forward(step)
            pos=position(ant)
            root1.counter+=1

        elif posandcolor[pos] =="seagreen" :
            ant.fillcolor("springgreen")
            ant.stamp()
            change(posandcolor, ant,"springgreen")
            ant.right(120)
            ant.forward(step)
            pos=position(ant)
            root1.counter+=1

        elif posandcolor[pos] =="springgreen" :
            ant.fillcolor("lime")
            ant.stamp()
            change(posandcolor, ant,"lime")
            ant.right(60)
            ant.forward(step)
            pos=position(ant)
            root1.counter+=1

        elif posandcolor[pos] =="lime" :
            ant.fillcolor("darkgreen")
            ant.stamp()
            change(posandcolor, ant,"darkgreen")
            ant.left(120)
            ant.forward(step)
            pos=position(ant)
            root1.counter+=1

        SV.set('Movements : ' + str(root1.counter)) 

def position(ant): 
    return (round(ant.xcor()), round(ant.ycor()))

def change(graph, ant, color): 
    graph[position(ant)] = color

def choice():
    global root2
    root2=tk.Tk()
    root2.configure(bg='black')
    frame=tk.Frame(root2,relief='ridge',borderwidth=5,bg='black')
    frame.pack()
    label = tk.Label(frame, text="Choose version",font='Arial 20',fg='white',bg='black')
    label.pack(fill="x", expand=1)
    button1=tk.Button(root2, text='Version 1',font='Arial 20', command=version1)
    button1.configure(bg='black',borderwidth=2,fg='white')
    button1.pack(fill="both",expand=1)
    button2a=tk.Button(root2, text='Version 2A',font='Arial 20', command=version2a)
    button2a.configure(bg='black',borderwidth=2,fg='white')
    button2a.pack(fill="both",expand=1)
    button2b=tk.Button(root2, text='Version 2B',font='Arial 20', command=version2b)
    button2b.configure(bg='black',borderwidth=2,fg='white')
    button2b.pack(fill="both",expand=1)
    button3=tk.Button(root2, text='Version 3',font='Arial 20', command=version3)
    button3.configure(bg='black',borderwidth=2,fg='white')
    button3.pack(fill="both",expand=1)
    button4=tk.Button(root2, text='Version 4',font='Arial 20', command=version4)
    button4.configure(bg='black',borderwidth=2,fg='white')
    button4.pack(fill="both",expand=1)
    button5=tk.Button(root2, text='Version 5',font='Arial 20', command=version5)
    button5.configure(bg='black',borderwidth=2,fg='white')
    button5.pack(fill="both",expand=1)
    button6=tk.Button(root2, text='Version 6',font='Arial 20', command=version6)
    button6.configure(bg='black',borderwidth=2,fg='white')
    button6.pack(fill="both",expand=1)
    button7=tk.Button(root2, text='Version 7',font='Arial 20', command=version7)
    button7.configure(bg='black',borderwidth=2,fg='white')
    button7.pack(fill="both",expand=1)
    button8=tk.Button(root2, text='Version 8',font='Arial 20', command=version8)
    button8.configure(bg='black',borderwidth=2,fg='white')
    button8.pack(fill="both",expand=1)
    button9=tk.Button(root2, text='Version 9',font='Arial 20', command=version9)
    button9.configure(bg='black',borderwidth=2,fg='white')
    button9.pack(fill="both",expand=1)
    root2.geometry('350x700+600+100')
    root2.overrideredirect(True)
    root2.resizable(False,False)

if __name__ == '__main__':   
    choice()


    
