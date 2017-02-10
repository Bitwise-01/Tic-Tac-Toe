#!/usr/bin/env python
#
# Play Tic-Tac-Toe
#
from Tkinter import *
from random import choice
from itertools import permutations

class Game(object): 
 def __init__(self,master):
  gui=master
  self.won  = False
  self.syms = choice(['X','O'])
  self.plts = []
  self._sym = []
  self.mid  = [01,10,11,21,12]
  self.corn = [00,02,20,22]
  self.flow = [
                [00,01,02],[20,21,22],
                [00,10,20],[02,12,22], 
                [10,11,12],[01,11,21],
                [00,11,22],[02,11,20]
              ]

 def corners(self,conn):
  for lst in self.flow:
   if lst[1] == conn:
    return lst[0],lst[2]
    
 def game(self,c1,c2,mid):  
  _game = []
  for plt,sym in zip(self.plts,self._sym):
   if plt==c1 or plt==c2 or plt==mid:
    _game.append(sym)  

  if len(_game) == 3:
   if _game[0]=='X' and _game[1]=='X' and _game[2]=='X':
    return 'X'
   if _game[0]=='O' and _game[1]=='O' and _game[2]=='O':
    return 'O'
  else:
   return  
 
 def criss_cross(self):
  if 10 in self.plts and 12 in self.plts:
   k = self.game(10,12,11)
   if k:
    self._color([10,11,12],k) 
    self.won=True 
    self._kill()    
  if 01 in self.plts and 21 in self.plts:
   k = self.game(01,21,11)
   if k:
    self._color([01,11,21],k)
    self.won=True
    self._kill()
  
  if 00 in self.plts and 22 in self.plts:
   k = self.game(00,22,11)
   if k:
    self._color([00,11,22],k)
    self.won=True
    self._kill()
  if 02 in self.plts and 20 in self.plts:
   k = self.game(02,20,11)
   if k:
    self._color([01,11,21],k)
    self.won=True
    self._kill()
    
 def _color(self,plts,sym='',color='green'):
  for loc in plts:
   if len(str(loc)) == 1:
    rows,columns=0,loc
   else:
    loc = str(loc)
    rows,columns = int(loc[0]),int(loc[1])

   recolor = Label(text=sym,bg=color)
   recolor.grid(row=rows,column=columns)
  
 def _kill(self):
  for lst in self.flow:
   for item in lst:
    if not item in self.plts:
     self.plts.append(item)

 def check(self):
  if len(self.plts) < 3: 
   return
  if len(self.plts) == 9 and not self.won:
   for lst in self.flow:
    self._color(lst,color='red')
  for n in self.plts:
   if n in self.mid:
    if n == 11:
     self.criss_cross()
    else:
     crns = self.corners(n)
     c1,c2=crns[0],crns[1]
     if c1 in self.plts and c1 in self.plts:
      k = self.game(c1,c2,n)
      if k:
       self._color([c1,n,c2],k)
       self.won=True
       self._kill()
       
    
 def clicked(self,y,x):
  iname = int('{}{}'.format(y,x))
  mark = Label(text=self.syms)
  if iname not in self.plts:
   self.plts.append(iname)
   self._sym.append(self.syms)
   mark.grid(row=y,column=x)
   self.syms = 'O' if self.syms == 'X' else 'X'
   self.check()
  
 def design(self):
  b0=Button(gui,command=lambda:self.clicked(0,0));b1=Button(gui,command=lambda:self.clicked(0,1));b2=Button(gui,command=lambda:self.clicked(0,2))
  b3=Button(gui,command=lambda:self.clicked(1,0));b4=Button(gui,command=lambda:self.clicked(1,1));b5=Button(gui,command=lambda:self.clicked(1,2))
  b6=Button(gui,command=lambda:self.clicked(2,0));b7=Button(gui,command=lambda:self.clicked(2,1));b8=Button(gui,command=lambda:self.clicked(2,2))

  b0.grid(row=0,column=0);b1.grid(row=0,column=1);b2.grid(row=0,column=2)
  b3.grid(row=1,column=0);b4.grid(row=1,column=1);b5.grid(row=1,column=2)
  b6.grid(row=2,column=0);b7.grid(row=2,column=1);b8.grid(row=2,column=2)

  b0.config(height=5,width=5);b1.config(height=5,width=5);b2.config(height=5,width=5)
  b3.config(height=5,width=5);b4.config(height=5,width=5);b5.config(height=5,width=5)
  b6.config(height=5,width=5);b7.config(height=5,width=5);b8.config(height=5,width=5)

if __name__ == '__main__':
  gui = Tk()
  gui.title('Game')
  Game(gui).design()
  gui.mainloop()
