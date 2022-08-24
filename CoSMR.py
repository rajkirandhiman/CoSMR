from tkinter import *
import numpy as np
import math
from matplotlib import pyplot as plt
import pandas as pd


class MyWindow:
    def __init__(self, win):
      
      def planar():
         self.b1=Button(win, text='Generate CoSMR chart for planar/wedge', command=self.add,font=("Times New Roman", 12, "bold"))
         self.b1.place(x=230, y=255)
      def toppling():
         self.b1=Button(win, text='Generate CoSMR chart for toppling         ', command=self.add2,font=("Times New Roman", 12, "bold"))
         self.b1.place(x=230, y=255) 
       
      Radiobutton(win,text="Planar/Wedge Failure",command=planar,font=("Times New Roman", 13, "bold")).grid(row=1,column=1)
      Radiobutton(win,text="Toppling Failure",command=toppling,font=("Times New Roman", 13, "bold")).grid(row=1,column=2)
      
      
      self.dip=Label(win, text='Dip amount of slope',font=("Times New Roman", 13, "bold"))
      self.dip.place(x=40, y=130)
      self.dip=Entry()
      self.dip.place(x=200, y=133)
      
      
      self.f4=Label(win, text='Excavation factor',font=("Times New Roman", 13, "bold"))
      self.f4.place(x=385, y=130)
      self.f4=Entry()
      self.f4.place(x=530, y=133)
      
   
    
    def add(self):
    
        num1=int(self.dip.get())
        num2=int(self.f4.get())
        
        def FACTOR1(x):
           FACTOR1 = 16 / 25 - 3 / 500 * math.atan((abs(x) - 17) / 10) * 180 / math.pi
           return FACTOR1
#F1: measure of parallelism between slope and discontinuity strikes or dip directions
# Basically here we are considering only one quadrant  that is o to 90 deg
# we are not considering upto 180 deg [0,90]


        def FACTOR2(n):
           FACTOR2 = 9 / 16 + 1 / 195 * math.atan(17 / 100 * n - 5) * 180 / math.pi
           return FACTOR2
#F2: measurement of the discontinuity dip
# [0,90]

        def FACTOR3(m):
           FACTOR3 = -30 + 1 / 3 * math.atan(m) * 180 / math.pi
           return FACTOR3
# F3: slope dip ratio and discontinuity
# dip values ?? range [0,90]
# therefore the input argument ranges from [-90,90]


      # For Planar/Wedge failure
        RMR=100 # changes in RMR do not affect SMR contours
        bs=num1  # slope dip (bs) can be changed manually
        f4 =num2  # f4 can be changed here manually
        xpartes=90
        ypartes=90
     # add bj and A
        bj=np.linspace(0.0,90.0,num = 90)
        A=np.linspace(0.0,90.0,num = 90)
        (A,bj)=np.meshgrid(A,bj) # meshgrid formation with domain vectors
      #SMR = np.empty((90,90), int)
        df  = pd.DataFrame()
        df=A
        for i in range(0,89):
         for j in range(0,89):
          a=RMR + FACTOR1(A[i,j])*FACTOR2(bj[i,j])*FACTOR3(bj[i,j]-bs) + f4
          df[i][j]=a
    
        for i in range(0,89):
         for j in range(0,89):
          if df[i][j]<0: 
           df[i][j]=0
        bj=np.linspace(0.0,90.0,num = 90)
        A=np.linspace(0.0,90.0,num = 90)
        plt.contour(A,bj,df,[-20,-15,-10,-5,0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100,105,110,115,120],colors='black')

        csfont = {'fontname':'Times New Roman'}
        plt.xlabel("A (Strike Parallelism) (°)",**csfont,fontsize=12,style='italic',fontweight="bold")
        plt.ylabel('Joint dip (βj) / Plunge (βi)(°)',**csfont,fontsize=12,style='italic',fontweight="bold")
        plt.title(f"Slope Dip (βs) = %d$°$, RMRb =_______" % bs,**csfont,fontweight="bold")
        plt.tick_params(width=2) 
        plt.show() 

    def add2(self):
    
        num1=int(self.dip.get())
        num2=int(self.f4.get())
        
        def FACTOR1(x):
           FACTOR1 = 16 / 25 - 3 / 500 * math.atan((abs(x) - 17) / 10) * 180 / math.pi
           return FACTOR1

        def FACTOR2(x):
           if x>0 or x<90:
             FACTOR2=1
           else:
             FACTOR2=0
           return FACTOR2

        def FACTOR3(x):
           FACTOR3 =-13 - 1 / 7 * math.atan(x - 120) * 180 / math.pi
           return FACTOR3

      # For toppling failure
        RMR=100 # changes in RMR do not affect SMR contours
        bs=num1  # slope dip (bs) can be changed manually
        f4 =num2  # f4 can be changed here manually
        xpartes=90
        ypartes=90
     # add bj and A
        bj=np.linspace(0.0,90.0,num = 90)
        A=np.linspace(0.0,90.0,num = 90)
        (A,bj)=np.meshgrid(A,bj) # meshgrid formation with domain vectors
      #SMR = np.empty((90,90), int)
        df  = pd.DataFrame()
        df=A
        for i in range(0,89):
         for j in range(0,89):
          a=RMR + FACTOR1(A[i,j])*FACTOR2(bj[i,j])*FACTOR3(bj[i,j]+bs) + f4
          df[i][j]=a
    
        for i in range(0,89):
         for j in range(0,89):
          if df[i][j]<0: 
           df[i][j]=0
         
        bj=np.linspace(0.0,90.0,num = 90)
        A=np.linspace(0.0,90.0,num = 90)
        plt.contour(A,bj,df,[-20,-15,-10,-5,0,5,10,15,20,25,30,35,40,45,50,55,60,65,70,75,80,85,90,95,100,105,110,115,120],colors='black')

        csfont = {'fontname':'Times New Roman'}
        plt.xlabel("A (Strike Parallelism) (°)",**csfont,fontsize=12,style='italic',fontweight="bold")
        plt.ylabel('Joint dip (βj) (°)',**csfont,fontsize=12,style='italic',fontweight="bold")
        plt.title(f"Slope Dip (βs) = %d$°$, RMR =_______" % bs,**csfont,fontweight="bold")
        plt.tick_params(width=2) 
        plt.show() 
# creating tkinter window
window=Tk()
header = Frame(window,width=700, height= 300, bg="#1874CD")
header.grid(columnspan=4, rowspan=2, row=0)

middle = Frame(window,width=700, height= 50)
middle.grid(columnspan=4, rowspan=1, row=1)


Label(window, text="Continuous Slope Mass Rating (CoSMR) Charts 📈", font=("Times New Roman", 18, "bold")).grid(rowspan=1,columnspan=4, row=0)

MyWindow(window)
window.title('CoSMR charts generator')
window.geometry("700x300")


window.mainloop()