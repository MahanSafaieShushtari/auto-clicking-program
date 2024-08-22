import pyautogui as pa 
import random as rn 
import math 
import time
def get_position():
    print("please take your mouce to the centre of the target coin!!")
    x,y=pa.position()
    print(f"x={x},y={y}")
    
    return x, y



def autoclick(range1=rn.randint(20,100)):
    

    while True:
        for i in range(0,range1):
           
            x,y=pa.position()
            pa.click(x,y)

            

            print(f"clicked for {i+1} time along ({x},{y})")
            time.sleep(0.2)




if __name__=="__main__":
   x,y=get_position()
   
   autoclick()

    











