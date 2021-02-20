#!/usr/bin/python3.7

import tkinter as tk
from pynput.mouse import Button, Listener 
import pyautogui
import time
import win32api, win32con
import threading
 
root = tk.Tk()


AUXILIARY_COLOR = []
AUXILIARY_POSITION =[]

BUY_POSITION =[]
BUY_COLOR =[]
BUY_COLOR_POSITION =[]

SELL_POSITION =[]
SELL_COLOR =[]
SELL_COLOR_POSITION =[]

RESET_POSITION =[]
RESET_COLOR =[]
RESET_COLOR_POSITION =[]

OPEN_MARKET= False

RUNNING_TIME = 0

SECURITY_STOP  = False

SHOULD_RUN = True



def click(x,y,button,pressed):
        if len(AUXILIARY_POSITION) > 0 and len(AUXILIARY_COLOR) >0 :
            AUXILIARY_POSITION.clear()
            AUXILIARY_COLOR.clear()
        else:
            pass
        AUXILIARY_POSITION.append(x)
        AUXILIARY_POSITION.append(y)

        pixelColor = pyautogui.screenshot().getpixel((x, y))

        for number in range(0,3):
            AUXILIARY_COLOR.append(pixelColor[number])
                            
        return False

def _from_rgb(rgb):
    """translates an rgb tuple of int to a tkinter friendly color code
    """
    return "#%02x%02x%02x" % rgb 
 
class Funcs():

# ---------------- BUY COLOR FUNCS------------------------
    def getBuyColor(self):
        with Listener(on_click=click) as listener:
            listener.join()
        if len(BUY_COLOR) > 0:
            BUY_COLOR.clear()
        for color in AUXILIARY_COLOR:
            BUY_COLOR.append(color)
        self.btnGetBuyColor.configure(background=_from_rgb((BUY_COLOR[0],BUY_COLOR[1],BUY_COLOR[2])))   
        print("BUY COLOR PICKED RGB: ", BUY_COLOR)

    def getBuyColorPosition(self):
        with Listener(on_click=click) as listener:
            listener.join()
        if len(BUY_COLOR_POSITION) > 0:
            BUY_COLOR_POSITION.clear()
        for position in AUXILIARY_POSITION:
            BUY_COLOR_POSITION.append(position)
        self.btnGetBuyColorPosition.configure(text=f"{BUY_COLOR_POSITION[0]}x{BUY_COLOR_POSITION[1]}")

# -----------------SELL COLOR FUNCS-----------------------
    def getSellColor(self):
        with Listener(on_click=click) as listener:
            listener.join()
        if len(SELL_COLOR) > 0:
            SELL_COLOR.clear()
            SELL_COLOR_POSITION.clear()
        for color in AUXILIARY_COLOR:
            SELL_COLOR.append(color) 
        for position in AUXILIARY_POSITION:
            SELL_COLOR_POSITION.append(position)       
        self.btnGetSellColor.configure(background=_from_rgb((SELL_COLOR[0],SELL_COLOR[1],SELL_COLOR[2])))
        print("SELL COLOR PICKED RGB: ", SELL_COLOR)

    def getSellColorPosition(self):
        with Listener(on_click=click) as listener:
            listener.join()
        if len(SELL_COLOR_POSITION) > 0:
            SELL_COLOR_POSITION.clear()
        for position in AUXILIARY_POSITION:
            SELL_COLOR_POSITION.append(position)
        self.btnGetSellColorPosition.configure(text=f"{SELL_COLOR_POSITION[0]}x{SELL_COLOR_POSITION[1]}")

# -----------------RESET COLOR FUNCS-----------------------

    def getResetColor(self):
        with Listener(on_click=click) as listener:
            listener.join()
        if len(RESET_COLOR) > 0:
            RESET_COLOR.clear()
            RESET_COLOR_POSITION.clear()
        for color in AUXILIARY_COLOR:
            RESET_COLOR.append(color)
        for position in AUXILIARY_POSITION:
            RESET_COLOR_POSITION.append(position)        
        self.btnGetResetColor.configure(background=_from_rgb((RESET_COLOR[0],RESET_COLOR[1],RESET_COLOR[2])))
        print("RESET COLOR PICKED RGB: ", RESET_COLOR)

    def getResetColorPosition(self):
        with Listener(on_click=click) as listener:
            listener.join()
        if len(RESET_COLOR_POSITION) > 0:
            RESET_COLOR_POSITION.clear()
        for position in AUXILIARY_POSITION:
            RESET_COLOR_POSITION.append(position)
        self.btnGetResetColorPosition.configure(text=f"{RESET_COLOR_POSITION[0]}x{RESET_COLOR_POSITION[1]}")

# ----------------- CLICK POSITION FUNCS ------------------

    def getBuyPositionClick(self):
        with Listener(on_click=click) as listener:
            listener.join()
        if len(BUY_POSITION) > 0:
            BUY_POSITION.clear()
        for position in AUXILIARY_POSITION:
            BUY_POSITION.append(position)
        self.btnGetBuyPosition.configure(background=_from_rgb((30,114,255)))   
        self.btnGetBuyPosition.configure(text=f"{BUY_POSITION[0]}x{BUY_POSITION[1]}")
       
    def getSellPositionClick(self):
        with Listener(on_click=click) as listener:
            listener.join()
        if len(SELL_POSITION) > 0:
            SELL_POSITION.clear()
        for position in AUXILIARY_POSITION:
            SELL_POSITION.append(position)
        self.btnGetSellPosition.configure(background=_from_rgb((30,114,255)))   
        self.btnGetSellPosition.configure(text=f"{SELL_POSITION[0]}x{SELL_POSITION[1]}")
        
    def getResetPositionClick(self):
        with Listener(on_click=click) as listener:
            listener.join()
        if len(RESET_POSITION) > 0:
            RESET_POSITION.clear()
        for position in AUXILIARY_POSITION:
            RESET_POSITION.append(position)
        self.btnGetResetPosition.configure(background=_from_rgb((30,114,255)))   
        self.btnGetResetPosition.configure(text=f"{RESET_POSITION[0]}x{RESET_POSITION[1]}")

# ----------------- MARKET FUNCS --------------------------

    def openMarket(self):
        print("ENTROU NO OPEN MARKET")

        open_market_thread = threading.Thread(target=self.closeMarket)

        print("QUANTIDADE DE THREEADS: ",threading.active_count())

        time.sleep(2)
        global OPEN_MARKET
        global RUNNING_TIME
        global SHOULD_RUN

        print(OPEN_MARKET, SHOULD_RUN)

        if(time.clock() - RUNNING_TIME < 2):
            self.securityStop()
            print("Codigo parado por seguranca")
            return

        self.statusLabel.configure(background="white", text="Aguardando posição...", fg="black")

        while OPEN_MARKET == False and SHOULD_RUN == True:
            buy_R = pyautogui.pixel(BUY_COLOR_POSITION[0],BUY_COLOR_POSITION[1])[0] == BUY_COLOR[0]
            buy_G = pyautogui.pixel(BUY_COLOR_POSITION[0],BUY_COLOR_POSITION[1])[1] == BUY_COLOR[1]
            buy_B = pyautogui.pixel(BUY_COLOR_POSITION[0],BUY_COLOR_POSITION[1])[2] == BUY_COLOR[2]
            sell_R = pyautogui.pixel(SELL_COLOR_POSITION[0],SELL_COLOR_POSITION[1])[0] == SELL_COLOR[0]
            sell_G = pyautogui.pixel(SELL_COLOR_POSITION[0],SELL_COLOR_POSITION[1])[1] == SELL_COLOR[1]
            sell_B = pyautogui.pixel(SELL_COLOR_POSITION[0],SELL_COLOR_POSITION[1])[2] == SELL_COLOR[2] 

            if buy_R and buy_G and buy_B :
                print("Entrou na condicao de BUY")

                RUNNING_TIME = time.clock()
                OPEN_MARKET = True

                self.clickMarket(BUY_POSITION[0],BUY_POSITION[1])
                open_market_thread.start()
                self.statusLabel.configure(background="green", text="Operacao de Compra Aberta...", fg="black")

                break
            elif sell_R and sell_G and sell_B:
                print("Entrou na condicao de SELL")

                RUNNING_TIME = time.clock()
                OPEN_MARKET= True
                

                self.clickMarket(SELL_POSITION[0],SELL_POSITION[1])
                open_market_thread.start()
                self.statusLabel.configure(background="red", text="Operacao de Venda Aberta...", fg="white")

                break

    def closeMarket(self):
        print("\r\n \r\n CHAMOU O CLOSE MARKET....")
        global OPEN_MARKET
        global SHOULD_RUN

        print("QUANTIDADE DE THREEADS: ",threading.active_count())

        while SHOULD_RUN == True:
            if pyautogui.pixel(RESET_COLOR_POSITION[0],RESET_COLOR_POSITION[1])[0] == RESET_COLOR[0] and pyautogui.pixel(RESET_COLOR_POSITION[0],RESET_COLOR_POSITION[1])[1] == RESET_COLOR[1] and pyautogui.pixel(RESET_COLOR_POSITION[0],RESET_COLOR_POSITION[1])[2] == RESET_COLOR[2]:
                
                if SHOULD_RUN == True:
                    self.statusLabel.configure(background="#f6b609", text="Operacao Encerrada...", fg="black")
                    self.clickMarket(RESET_POSITION[0],RESET_POSITION[1])
                    threading.Thread(target=self.openMarket).start()
                    
                break

            else:
                pass
        OPEN_MARKET= False
        

        return

    def clickMarket(self,x,y):
        global SHOULD_RUN

        if SHOULD_RUN == True:
            win32api.SetCursorPos((x,y))
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
            time.sleep(0.01)
            win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
        
# ---------------- START AND STOP FUNCS -------------------

    def startRunning(self):
        global OPEN_MARKET
        global SHOULD_RUN

        OPEN_MARKET = False
        SHOULD_RUN = True

        threading.Thread(target=self.openMarket).start()
        print("QUANTIDADE DE THREEADS: ",threading.active_count())
       
        self.btnTurnOn["state"] = "disabled"
        self.btnTurnOff["state"] = "normal"

    def stopRunning(self):
        
        global SHOULD_RUN
        SHOULD_RUN = False
        self.statusLabel.configure(background="white", text="-- DESLIGADO --", fg="black")
        self.enableOnButton()
        return

    def securityStop(self):
        global SECURITY_STOP

        self.security = tk.Toplevel(root)
        self.security.title("Security stop")
        self.security.configure(background="red")
        self.security.geometry("400x100")
        self.securityWarning = tk.Label(self.security, text="Ordens paradas por seguranca.", fg="black", bg="red")
        self.securityWarning.config(font=("Courier", 15,'bold'))
        self.securityWarning.place(relx=0.05,rely=0.40)
        self.security.wm_attributes("-topmost", True)
        self.btnTurnOff["state"] = "disabled"
        
        SECURITY_STOP = True
        self.security.protocol("WM_DELETE_WINDOW", self.enableOnButton)
        print("QUANTIDADE DE THREEADS: ",threading.active_count())

        self.statusLabel.configure(background="white", text="-- DESLIGADO --", fg="black")

    def enableOnButton(self):
        global SECURITY_STOP

        if SECURITY_STOP == True:
            self.security.destroy()
            SECURITY_STOP = False
        else:
            time.sleep(1)
            
        self.btnTurnOn["state"] = "normal"

class Application(Funcs):
    def __init__(self):
        self.root=root

        self.screen()
        self.status()
        self.labels_properties()

        self.button_buy_color_properties()
        self.button_sell_color_properties()
        self.button_reset_color_properties()


        self.getPositionClickWidgets()
        self.turn_OnOffButton()
        root.wm_attributes("-topmost", True)
        self.root.protocol("WM_DELETE_WINDOW", self.close_program)
        
        root.mainloop()

    def status(self):
        self.statusLabel = tk.Label(self.root, text="-- DESLIGADO --", bg="white",font=("Courier", 10,'bold'))
        self.statusLabel.place(relx=0.01, rely=0.02, relwidth=0.98, relheight=0.1)

    def screen(self):
        self.root.title("5M BOT")
        self.root.configure(background="#222222")
        self.root.geometry("500x200")

    def button_buy_color_properties(self):
        ### BTN BUY COLOR POSITION
        self.btnGetBuyColorPosition = tk.Button(self.root,text="0x0", command=self.getBuyColorPosition)
        self.btnGetBuyColorPosition.place(relx=0.1,rely=0.27, relwidth=0.15,relheight=0.1)

        ### BTN BUY COLOR 
        self.btnGetBuyColor = tk.Button(self.root, command=self.getBuyColor)
        self.btnGetBuyColor.place(relx=0.26,rely=0.27, relwidth=0.05,relheight=0.1)

    def button_sell_color_properties (self):
        ### BTN SELL COLOR POSITION
        self.btnGetSellColorPosition = tk.Button(self.root,text="0x0", command=self.getSellColorPosition)
        self.btnGetSellColorPosition.place(relx=0.37,rely=0.27, relwidth=0.15,relheight=0.1)

        ### BTN SELL COLOR 
        self.btnGetSellColor = tk.Button(self.root, command=self.getSellColor)
        self.btnGetSellColor.place(relx=0.53,rely=0.27, relwidth=0.05,relheight=0.1)

    def button_reset_color_properties(self):
        ### BTN RESET COLOR  POSITION
        self.btnGetResetColorPosition = tk.Button(self.root,text="0x0", command=self.getResetColorPosition)
        self.btnGetResetColorPosition.place(relx=0.64,rely=0.27, relwidth=0.15,relheight=0.1)


         ### BTN RESET COLOR 
        self.btnGetResetColor = tk.Button(self.root, command=self.getResetColor)
        self.btnGetResetColor.place(relx=0.80,rely=0.27, relwidth=0.05,relheight=0.1)

    def labels_properties(self): 
        
   
        ### LABEL BTN BUY
        self.labelGetBuyColor = tk.Label(self.root, text="Buy Color", fg="white", bg="#222222")
        self.labelGetBuyColor.place(relx =0.1, rely=0.15)
        ### LABEL BTN SELL
        self.labelGetSellColor = tk.Label(self.root, text="Sell Color", fg="white", bg="#222222")
        self.labelGetSellColor.place(relx =0.37, rely=0.15)
        ### LABEL BTN RESET
        self.labelGetResetColor = tk.Label(self.root, text="Reset Color", fg="white", bg="#222222")
        self.labelGetResetColor.place(relx =0.64, rely=0.15)

    def close_program(self):
        self.stopRunning()
        self.root.destroy()



    def getPositionClickWidgets(self):
        ### BTN BUY Position
        self.btnGetBuyPosition = tk.Button(self.root,text="0x0", command=self.getBuyPositionClick)
        self.btnGetBuyPosition.place(relx=0.1,rely=0.53, relwidth=0.25,relheight=0.1)
        ### BTN SELL Position
        self.btnGetSellPosition = tk.Button(self.root,text="0x0", command=self.getSellPositionClick)
        self.btnGetSellPosition.place(relx=0.37,rely=0.53, relwidth=0.25,relheight=0.1)
        ### BTN RESET Position
        self.btnGetResetPosition = tk.Button(self.root,text="0x0", command=self.getResetPositionClick)
        self.btnGetResetPosition.place(relx=0.64,rely=0.53, relwidth=0.25,relheight=0.1)
    
        ### LABEL BTN BUY
        self.labelGetBuyPosition = tk.Label(self.root, text="Buy Position:", fg="white", bg="#222222")
        self.labelGetBuyPosition.place(relx =0.1, rely=0.40)
        ### LABEL BTN SELL
        self.labelGetSellPosition = tk.Label(self.root, text="Sell Position:", fg="white", bg="#222222")
        self.labelGetSellPosition.place(relx =0.37, rely=0.40)
        ### LABEL BTN RESET
        self.labelGetResetPosition = tk.Label(self.root, text="Reset Position:", fg="white", bg="#222222")
        self.labelGetResetPosition.place(relx =0.64, rely=0.40)
        pass
    
    def turn_OnOffButton(self):
        ### TURN ON or OFF BUTTON
        self.btnTurnOn = tk.Button(self.root,text="ON", bg="green",command=self.startRunning)
        self.btnTurnOn.place(relx=0.17,rely=0.80, relwidth=0.25,relheight=0.1)

        self.btnTurnOff = tk.Button(self.root,text="OFF", bg="red",command=self.stopRunning)
        self.btnTurnOff.place(relx=0.54,rely=0.80, relwidth=0.25,relheight=0.1)

        
Application()

