import tkinter as tk
from tkinter import *
window = tk.Tk()
window.title("Console Dino")
canvas = tk.Canvas(window, width=500,height=500)
canvas.pack()
canvas.create_line(0,250,500,250)
points_label = tk.Label(window, text="Points: " )
points_label1 = tk.Label(window, text=0)
points_label.pack()
points_label1.pack()
points_label1.place(x=120,y=50)
points_label.place(x=80,y=50)
message = tk.Label(window, text="Press Enter to Restart.")
message.pack()
message.place(x=210,y=260)


class Dino():
    def __init__(self,cact):
        self.image = tk.PhotoImage(file="dinosaur.gif")
        self.X_cor = 250-(self.image.width()/2)
        self.Y_cor = 250 - self.image.height()+7
        self.height = 0
        self.height_counter = 0
        self.startofjump = True
        self.ifdonejump = False
        self.imageobject = canvas.create_image(self.X_cor, self.Y_cor, anchor=tk.NW, image=self.image)
        self.cact = cact
        
    def jump(self,event):
        
        if self.Y_cor <= 207 and self.ifdonejump == False :
            if self.Y_cor != 207 and self.startofjump != True:
                print(self.Y_cor , "1")
                canvas.move(self.imageobject,0,-self.height )
                self.Y_cor -= self.height
                
                self.height = (18 - 1.2* self.height_counter)
                self.height_counter += 1
                window.after(10,lambda: self.jump(event))
            elif self.startofjump:
                
                self.height = (18 - 1.2* self.height_counter)
                self.height_counter += 1
                canvas.move(self.imageobject,0,-self.height )
                self.Y_cor -= self.height
               
                window.after(10,lambda: self.jump(event))   
            if self.startofjump:
                self.startofjump = False
        else:
            canvas.move(self.imageobject,0,-(self.get_Y()-207))
            self.Y_cor += -(self.get_Y()-207)
            self.startofjump = True
            self.ifdonejump = False
            self.height = 0
            self.height_counter = 0
    def get_X(self):
        return self.X_cor
    def get_Y(self):
        return self.Y_cor
    def keypresschecker(self,event):
        
        if event.keysym == "space":
            littledino.jump(event)
        else:
            self.cact.restart(self)
            self.imageobject = canvas.create_image(self.X_cor, self.Y_cor, anchor=tk.NW, image=self.image)
class Cactus:
    def __init__(self):
        self.image = tk.PhotoImage(file="cactus.png")
        self.X_cor = 490
        self.Y_cor = 250 - self.image.height()
        self.imageobject = canvas.create_image(self.X_cor, self.Y_cor, anchor=tk.NW, image=self.image)
        self.lost = False
        self.points = 0
        self.speed = 5
    def Cactus_Move(self,dino):
        if not self.lost: 
            self.X_cor -= self.speed
            canvas.move(self.imageobject,-self.speed,0)
            if((self.X_cor >= dino.get_X()and self.X_cor <= dino.get_X()+10) and dino.get_Y() >= (250 - self.image.height())):
                canvas.delete("all")
             
                points_label.destroy
                points_label1.destroy
                points_label.place(x=230,y=240)
                points_label1.place(x=270,y=240)
                
                self.lost = True
                
            elif self.X_cor <= -30:
                self.X_cor = 500
                canvas.move(self.imageobject,530,0)
                
                self.points += 1
                if(self.speed < 10):
                    self.speed += 1
                points_label1.config(text = self.points)
            window.after(10,lambda: self.Cactus_Move(dino))   
    def getiflost(self):
        print(self.lost)
        return self.lost    
    
    def restart(self,cact):
        canvas.delete("all")
             
       
        self.points = 0
        self.speed = 5
        points_label1.config(text = self.points)
        self.X_cor = 490
        self.Y_cor = 250 - self.image.height()
        self.imageobject = canvas.create_image(self.X_cor, self.Y_cor, anchor=tk.NW, image=self.image)
        self.lost = False
        points_label1.place(x=120,y=50)
        points_label.place(x=80,y=50)
        canvas.create_line(0,250,500,250)
        
        self.Cactus_Move(cact)
        

littlecactus = Cactus()
littledino = Dino(littlecactus)
canvas.bind("<Button-1>", littledino.jump)
window.bind("<KeyPress>",littledino.keypresschecker)
window.after(1000,littlecactus.Cactus_Move,littledino)
window.mainloop()
