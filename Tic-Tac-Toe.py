#!/usr/bin/env python
#
# Play Tic-Tac-Toe
#
from Tkinter import *
from random import choice

class Game(object): 
 def __init__(self,master):
  gui                  = master
  self.gameOver        = False 
  self.currentSymbol   = choice(['X','O'])    # Random choice for symbol to start with
  self.positionsPlayed = {}                   # plots  history
  self.fullboard       = 9                    # When no more space is left
  self.waysOfWinning   = [
                          [0,1,2], [6,7,8],
                          [0,3,6], [2,5,8], 
                          [3,4,5], [1,4,7],
                          [0,4,8], [2,4,6]
                         ] 

 def checkForWins(self):
  for winList in self.waysOfWinning:
   if all([winList[0] in self.positionsPlayed, winList[1] in self.positionsPlayed, winList[2] in self.positionsPlayed]):
    if all([self.positionsPlayed[winList[0]]=='X',self.positionsPlayed[winList[1]]=='X',self.positionsPlayed[winList[2]]=='X']): 
     fails=[coord for coord in self.positionsPlayed if not coord in winList] # List of failed plot
     self.finalStep(winList,'green') # Color winning plots to green
     self.finalStep(fails,'red') # Color failed plots to red
     self.gameOver=True     

    if all([self.positionsPlayed[winList[0]]=='O',self.positionsPlayed[winList[1]]=='O',self.positionsPlayed[winList[2]]=='O']): 
     fails=[coord for coord in self.positionsPlayed if not coord in winList]
     self.finalStep(winList,'green') # Color winning plots to green
     self.finalStep(fails,'red') # Color failed plots to red
     self.gameOver=True   

 def analyze(self):
  if len(self.positionsPlayed)==self.fullboard:
   self.finalStep(self.positionsPlayed,'red')
   self.gameOver=True
  self.checkForWins()
 
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
  coord = self.deflate(int('{}{}'.format(y,x))) # Combine X and Y and turn it into a number then decrease into smaller numbers 
  mark  = Label(text=self.currentSymbol)        
  mark.config(font=("Courier", 50)) # Increase size of symbol   

  if coord not in self.positionsPlayed:
   self.positionsPlayed[coord]=self.currentSymbol

   mark.grid(row=y,column=x) # Mark on game grid
   self.currentSymbol='O' if self.currentSymbol=='X' else 'X' # Change the symbol
   self.analyze() # Analyze the game play   
  
 def design(self):
  b0=Button(gui,command=lambda:self.clicked(0,0));b1=Button(gui,command=lambda:self.clicked(0,1));b2=Button(gui,command=lambda:self.clicked(0,2))
  b3=Button(gui,command=lambda:self.clicked(1,0));b4=Button(gui,command=lambda:self.clicked(1,1));b5=Button(gui,command=lambda:self.clicked(1,2))
  b6=Button(gui,command=lambda:self.clicked(2,0));b7=Button(gui,command=lambda:self.clicked(2,1));b8=Button(gui,command=lambda:self.clicked(2,2))

  b0.grid(row=0,column=0);b1.grid(row=0,column=1);b2.grid(row=0,column=2)
  b3.grid(row=1,column=0);b4.grid(row=1,column=1);b5.grid(row=1,column=2)
  b6.grid(row=2,column=0);b7.grid(row=2,column=1);b8.grid(row=2,column=2)

  b0.config(height=15,width=15);b1.config(height=15,width=15);b2.config(height=15,width=15)
  b3.config(height=15,width=15);b4.config(height=15,width=15);b5.config(height=15,width=15)
  b6.config(height=15,width=15);b7.config(height=15,width=15);b8.config(height=15,width=15)

if __name__ == '__main__':
 gui=Tk()
 gui.title('Tic-Tac-Toe')
 Game(gui).design()
 gui.mainloop()
