# coding:utf-8
# GUI tx2调试程序  随机模式 定点模式
from Tkinter import *
import driver


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.label1 = Label(self, text='----随机模式----')
        self.label1.grid(row=0)

        self.randomModeButton = Button(self, text='随机发球', command=driver.init)
        self.randomModeButton.grid(row=1)

        self.label2 = Label(self, text='----定点模式----')
        self.label2.grid(row=2)

        self.fixedModeButton = Button(self, text='随机发球', command=driver.init)
        self.fixedModeButton.grid(row=3, column=0)

        self.positon0Button = Button(self, text='0', command=driver.init)
        self.positon0Button.grid(row=4, column=0)
        self.positon1Button = Button(self, text='1', command=driver.init)
        self.positon1Button.grid(row=4, column=1)
        self.positon2Button = Button(self, text='2', command=driver.init)
        self.positon2Button.grid(row=4, column=2)
        self.positon3Button = Button(self, text='3', command=driver.init)
        self.positon3Button.grid(row=4, column=3)
        self.positon4Button = Button(self, text='4', command=driver.init)
        self.positon4Button.grid(row=4, column=4)
        self.positon5Button = Button(self, text='5', command=driver.init)
        self.positon5Button.grid(row=5, column=0)
        self.positon6Button = Button(self, text='6', command=driver.init)
        self.positon6Button.grid(row=5, column=1)
        self.positon7Button = Button(self, text='7', command=driver.init)
        self.positon7Button.grid(row=5, column=2)
        self.positon8Button = Button(self, text='8', command=driver.init)
        self.positon8Button.grid(row=5, column=3)
        self.positon9Button = Button(self, text='9', command=driver.init)
        self.positon9Button.grid(row=5, column=4)
    def randMode(self):



app = Application()
# 设置窗口标题:
app.master.title('Hello World')
# 主消息循环:
try:
    app.mainloop()
finally:
    driver.destroy()
