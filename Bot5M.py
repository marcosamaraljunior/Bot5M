#!/usr/bin/python3.7


# NEXT STEPS
### CRIAR GetPosition
### CRIAR FUNCAO CLICK POSITION.

import tkinter as tk
from pynput.mouse import Button, Listener 
import pyautogui
 
root = tk.Tk()

AUXILIARY_COLOR = []
AXULIARY_POSITION =[]

BUY_POSITION =[]
BUY_COLOR =[]

SELL_POSITION =[]
SELL_COLOR =[]

RESET_POSITION =[]
RESET_COLOR =[]


def click(x,y,button,pressed):
        if len(AXULIARY_POSITION) > 0 and len(AUXILIARY_COLOR) >0 :
            AXULIARY_POSITION.clear()
            AUXILIARY_COLOR.clear()
        else:
            pass
        AXULIARY_POSITION.append(x)
        AXULIARY_POSITION.append(y)

        pixelColor = pyautogui.screenshot().getpixel((x, y))

        for number in range(0,3):
            AUXILIARY_COLOR.append(pixelColor[number])
                            
        return False

def _from_rgb(rgb):
    """translates an rgb tuple of int to a tkinter friendly color code
    """
    return "#%02x%02x%02x" % rgb 
 
class Funcs():
    def getBuyColor(self):
        with Listener(on_click=click) as listener:
            listener.join()
        if len(BUY_COLOR) > 0:
            BUY_COLOR.clear()
        for color in AUXILIARY_COLOR:
            BUY_COLOR.append(color) 
        self.btnGetBuyColor.configure(background=_from_rgb((BUY_COLOR[0],BUY_COLOR[1],BUY_COLOR[2])))   
        self.btnGetBuyColor.configure(text=f"RGB({BUY_COLOR[0]},{BUY_COLOR[1]},{BUY_COLOR[2]})")

    def getSellColor(self):
        with Listener(on_click=click) as listener:
            listener.join()
        if len(SELL_COLOR) > 0:
            SELL_COLOR.clear()
        for color in AUXILIARY_COLOR:
            SELL_COLOR.append(color)       
        self.btnGetSellColor.configure(background=_from_rgb((SELL_COLOR[0],SELL_COLOR[1],SELL_COLOR[2])))
        self.btnGetSellColor.configure(text=f"RGB({SELL_COLOR[0]},{SELL_COLOR[1]},{SELL_COLOR[2]})")

    def getResetColor(self):
        with Listener(on_click=click) as listener:
            listener.join()
        if len(RESET_COLOR) > 0:
            RESET_COLOR.clear()
        for color in AUXILIARY_COLOR:
            RESET_COLOR.append(color)       
        self.btnGetResetColor.configure(background=_from_rgb((RESET_COLOR[0],RESET_COLOR[1],RESET_COLOR[2])))
        self.btnGetResetColor.configure(text=f"RGB({RESET_COLOR[0]},{RESET_COLOR[1]},{RESET_COLOR[2]})")

    def openPosition(self):
        while True:
            if pyautogui.pixel(BUY_POSITION[0],BUY_POSITION[1])[0] == BUY_COLOR[0]:
                # CLICK INTO BUY BUTTON
                self.closePostion()
                break
            elif pyautogui.pixel(SELL_POSITION[0],SELL_POSITION[1])[0] == SELL_COLOR[0]:
                #CLICK INTO SELL BUTTON
                self.closePostion()
                break
        return
    
    def closePostion(self):
        while True:
            if pyautogui.pixel(RESET_POSITION[0],RESET_POSITION[1])[0] == RESET_COLOR[0]:
                # CLICK INTO RESET BUTTON
                break
        self.openPosition()
        return

class Application(Funcs):
    def __init__(self):
        self.root=root
        self.screen()
        self.widgets()
        root.wm_attributes("-topmost", True)
        root.mainloop()
    def screen(self):
        self.root.title("5M BOT")
        self.root.configure(background="#222222")
        self.root.geometry("500x200")
    def widgets(self): 
        ### BTN BUY COLOR
        self.btnGetBuyColor = tk.Button(self.root,text="Compra", command=self.getBuyColor)
        self.btnGetBuyColor.place(relx=0.1,rely=0.17, relwidth=0.25,relheight=0.1)
        ### BTN SELL COLOR
        self.btnGetSellColor = tk.Button(self.root,text="Venda", command=self.getSellColor)
        self.btnGetSellColor.place(relx=0.37,rely=0.17, relwidth=0.25,relheight=0.1)
        ### BTN RESET COLOR
        self.btnGetResetColor = tk.Button(self.root,text="Zerar", command=self.getResetColor)
        self.btnGetResetColor.place(relx=0.64,rely=0.17, relwidth=0.25,relheight=0.1)

        ### LABEL BTN BUY
        self.labelGetBuyColor = tk.Label(self.root, text="Buy Color", fg="white", bg="#222222")
        self.labelGetBuyColor.place(relx =0.1, rely=0.05)
        ### LABEL BTN SELL
        self.labelGetSellColor = tk.Label(self.root, text="Sell Color", fg="white", bg="#222222")
        self.labelGetSellColor.place(relx =0.37, rely=0.05)
        ### LABEL BTN RESET
        self.labelGetResetColor = tk.Label(self.root, text="Reset Color", fg="white", bg="#222222")
        self.labelGetResetColor.place(relx =0.64, rely=0.05)
       
Application()



