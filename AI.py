#!/usr/bin/env python
#
# Plays Tic-Tac-Toe
#
import time
import random
from Tkinter import *

class TicTacToe(object): 
 def __init__(self):
  self.fullboard       = 9
  self.positionsPlayed = {}                     
  self.gui             = None
  self.gameOver        = False  
  self.computerTurn    = random.randint(0,2)
  self.currentSymbol   = random.choice(['X','O'])                 
  self.waysOfWinning   = [[0,1,2],[6,7,8],[0,3,6],[2,5,8],[3,4,5],[1,4,7],[0,4,8],[2,4,6]] 
 
 def run(self):
  self.gui=Tk()
  self.gui.title('Artificial Intelligence')
  self.design()
  
 def wins(self):
  for winList in self.waysOfWinning:
   if all([winList[0] in self.positionsPlayed, winList[1] in self.positionsPlayed, winList[2] in self.positionsPlayed]):

    if all([self.positionsPlayed[winList[0]]=='X',self.positionsPlayed[winList[1]]=='X',self.positionsPlayed[winList[2]]=='X']): 
     fails=[coord for coord in self.positionsPlayed if not coord in winList] 
     self.finalStep(winList,'green') 
     self.finalStep(fails,'red')
     self.gameOver=True     

    if all([self.positionsPlayed[winList[0]]=='O',self.positionsPlayed[winList[1]]=='O',self.positionsPlayed[winList[2]]=='O']): 
     fails=[coord for coord in self.positionsPlayed if not coord in winList]
     self.finalStep(winList,'green') 
     self.finalStep(fails,'red') 
     self.gameOver=True   

 def analyze(self):
  if len(self.positionsPlayed)==self.fullboard:
   self.finalStep(self.positionsPlayed,'red')
   self.gameOver=True
  self.wins()
 
 def finalStep(self,plotList,color):
  plotList=[self.inflate(point) for point in plotList]

  for coord in plotList:
   symbol = self.positionsPlayed[self.deflate(coord)]
   coord  = str(coord)
   if len(coord)==1:
    row,column=0,coord
   else:
    row,column=int(coord[0]),int(coord[1])
   self.applyColor(row,column,symbol,color)  
 
 def applyColor(self,row,column,symbol,color): 
  recolor = Label(text=symbol,bg=color)
  recolor.config(font=("Courier", 44))
  recolor.grid(row=row,column=column)
  
 def deflate(self,num):
  if num<=2:
   return num
  if num<=12:
   return num-7
  return num-14

 def inflate(self,num):
  if num<=2:
   return num
  if num<=5:
   return num+7
  return num+14 
       
 def clicked(self,y,x):
  if self.gameOver:return
  coord = self.deflate(int('{}{}'.format(y,x)))
  mark  = Label(text=self.currentSymbol)        
  mark.config(font=("Courier", 50)) 

  if coord not in self.positionsPlayed:
   self.positionsPlayed[coord]=self.currentSymbol

   mark.grid(row=y,column=x) 
   self.analyze() 
   self.currentSymbol = 'O' if self.currentSymbol=='X' else 'X' 
   self.computerTurn  = False if self.computerTurn else True 
 
 def resetGui(self):
  engine.ai=None
  engine.reset()

 def design(self):
  reset=Button(self.gui,text='Reset',command=lambda:self.resetGui())
  b0=Button(self.gui,command=lambda:self.clicked(0,0));b1=Button(self.gui,command=lambda:self.clicked(0,1));b2=Button(self.gui,command=lambda:self.clicked(0,2))
  b3=Button(self.gui,command=lambda:self.clicked(1,0));b4=Button(self.gui,command=lambda:self.clicked(1,1));b5=Button(self.gui,command=lambda:self.clicked(1,2))
  b6=Button(self.gui,command=lambda:self.clicked(2,0));b7=Button(self.gui,command=lambda:self.clicked(2,1));b8=Button(self.gui,command=lambda:self.clicked(2,2))

  reset.grid(row=9,column=0)
  b0.grid(row=0,column=0);b1.grid(row=0,column=1);b2.grid(row=0,column=2)
  b3.grid(row=1,column=0);b4.grid(row=1,column=1);b5.grid(row=1,column=2)
  b6.grid(row=2,column=0);b7.grid(row=2,column=1);b8.grid(row=2,column=2)

  b0.config(height=15,width=15);b1.config(height=15,width=15);b2.config(height=15,width=15)
  b3.config(height=15,width=15);b4.config(height=15,width=15);b5.config(height=15,width=15)
  b6.config(height=15,width=15);b7.config(height=15,width=15);b8.config(height=15,width=15)

class AI(object):
 def __init__(self):
  self.corner   = [0,2,6,8]
  self.diagonal = [[0,8],[2,6]]
    
 def play(self):
  time.sleep(.1)
  if not engine.game.positionsPlayed:
   spot=str(engine.game.inflate(self.corner[random.randint(0,3)]))
   
   if len(spot)!=2:
    engine.game.clicked(0,int(spot))
   else:
    engine.game.clicked(int(spot[0]),int(spot[1])) 
   return

  if len(engine.game.positionsPlayed)==2:
   for lst in self.diagonal:
    spot=lst[0] if lst[1] in engine.game.positionsPlayed and not lst[0] in engine.game.positionsPlayed else lst[1] if lst[0] in engine.game.positionsPlayed and lst[1] not in engine.game.positionsPlayed else None
    if spot:
     spot=str(engine.game.inflate(spot))
     if len(spot)!=2:
      engine.game.clicked(0,int(spot))
     else:
      engine.game.clicked(int(spot[0]),int(spot[1])) 
     return

  if len(engine.game.positionsPlayed)==1:
   if not 4 in engine.game.positionsPlayed:
    engine.game.clicked(1,1)
    return
  
  if len(engine.game.positionsPlayed)==3:
   goodSpot=self.logic()
   if goodSpot!=None:
    spot=str(engine.game.inflate(goodSpot))
    if len(str(spot))!=2:
     engine.game.clicked(0,spot)
    else:
     engine.game.clicked(int(str(spot)[0]),int(str(spot)[1])) 
    return   
   if all([1 in engine.game.positionsPlayed,8 in engine.game.positionsPlayed]):
    if engine.game.positionsPlayed[1]==engine.game.positionsPlayed[8]:
     engine.game.clicked(0,2)
     return  
   if all([1 in engine.game.positionsPlayed,6 in engine.game.positionsPlayed]):
    if engine.game.positionsPlayed[1]==engine.game.positionsPlayed[6]:
     engine.game.clicked(0,0)
     return
   spot=[num for num in range(9) if not num in engine.game.positionsPlayed]
   spot=engine.game.inflate(random.choice(spot))   
   if len(str(spot))!=2:engine.game.clicked(0,spot)
   else:engine.game.clicked(int(str(spot)[0]),int(str(spot)[1]))  
   return 

  if len(engine.game.positionsPlayed)==4:
   goodSpot=self.logic()
   if goodSpot!=None:
    spot=str(engine.game.inflate(goodSpot))
    if len(str(spot))!=2:
     engine.game.clicked(0,spot)
    else:
     engine.game.clicked(int(str(spot)[0]),int(str(spot)[1])) 
    return  
   if all([2 in engine.game.positionsPlayed,not 8 in engine.game.positionsPlayed]):
    engine.game.clicked(2,2)
    return
   if all([7 in engine.game.positionsPlayed,not 0 in engine.game.positionsPlayed]):
    engine.game.clicked(0,0)
    return    

  goodSpot = self.logic()
  corner   = [num for num in self.corner if not num in engine.game.positionsPlayed]
  backup   = [num for num in range(9) if not num in engine.game.positionsPlayed]
  spot     = engine.game.inflate(goodSpot if goodSpot!=None else random.choice(corner) if corner else random.choice(backup) if backup else None) 
 
  if len(str(spot))!=2:engine.game.clicked(0,spot)
  else:engine.game.clicked(int(str(spot)[0]),int(str(spot)[1]))       
 
 def logic(self):
  for lst in engine.game.waysOfWinning:
   for a,alpha in enumerate(lst):
    for b,beta in enumerate(lst):
     if a==b:continue
     if all([alpha in engine.game.positionsPlayed,beta in engine.game.positionsPlayed]):
      if engine.game.positionsPlayed[alpha]==engine.game.positionsPlayed[beta]:
       for num in range(3):
        if all([a!=num,b!=num]):
         if not lst[num] in engine.game.positionsPlayed:
          return lst[num]

class Controls(object):
 def __init__(self):
  self.game = None
  self.ai   = None
  
 def engine(self):
  if not self.ai:
   self.game=TicTacToe()
   self.game.run()
   self.ai=AI()
  else:
   if engine.game.computerTurn:
    self.ai.play() 
    self.game.computerTurn=False
  if self.ai:
   for i in range(3):print '\n'
   self.game.gui.after(1,self.engine)   

 def reset(self):
  self.game.gui.after_cancel(self.game.gui)
  self.game.gui.destroy()
  engine=Controls()
  self.engine()  

if __name__ == '__main__':
 engine=Controls()
 engine.engine()
 engine.game.gui.mainloop() 
