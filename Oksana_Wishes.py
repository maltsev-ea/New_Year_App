from smsc_api import *
import tkinter as tk
#  import requests if need to targetly request from the server
#  https://smsc.ru/sys/send.php?login=<login>&psw=<password>&phones=<phones>&mes=<message>


class MyLoveAPP(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()

        self.e1 = tk.Entry(width=50)
        self.e1.pack()

        self.button1 = tk.Button(text='Отправить')
        self.button1['command'] = self.button_send
        self.button1.pack()
        
        self.button2 = tk.Button(text='Загадать еще желание')
        self.button2['command'] = self.button_refresh
        self.button2.pack()
        
    def button_refresh(self):
        self.button1['text'] = 'Отправить'
        self.e1.delete(0, 'end')


    def button_send(self):
        self.button1['text'] = 'Отправлено'
        message = self.e1.get()
        smsc.send_sms("79215891572", message, sender="sms")


root = tk.Tk()
love = MyLoveAPP(root)
smsc = SMSC()
love.mainloop()
