# coding:utf-8
from Tkinter import *
import driver


class Application(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.label1 = Label(self, text='------电源------')
        self.label1.pack()
        self.startButton = Button(self, text='启动', command=driver.init)
        self.startButton.pack()
        self.shutdownButton = Button(self, text='结束', command=driver.destroy)
        self.shutdownButton.pack()
        self.label2 = Label(self, text='----------------装载电机----------------')
        self.label2.pack()
        self.startLoadButton = Button(self, text='启动装载电机', command=driver.startLoadMotor)
        self.startLoadButton.pack()
        self.stopLoadButton = Button(self, text='停止装载电机', command=driver.stopLoadMotor)
        self.stopLoadButton.pack()
        self.loadBallsButton = Button(self, text='装载模式', command=driver.loadBalls)
        self.loadBallsButton.pack()
        self.unloadBallsButton = Button(self, text='卸载模式', command=driver.unloadBalls)
        self.unloadBallsButton.pack()
        self.label3 = Label(self, text='----------------上旋占空比----------------')
        self.label3.pack()
        self.upInput = Entry(self)
        self.upInput.pack()
        self.upButton = Button(self, text='上旋电机占空比', command=self.changeUpDutyCycle)
        self.upButton.pack()
        self.label4 = Label(self, text='----------------下旋占空比----------------')
        self.label4.pack()
        self.downInput = Entry(self)
        self.downInput.pack()
        self.downButton = Button(self, text='下旋电机占空比', command=self.changeDownDutyCycle)
        self.downButton.pack()
        self.label5 = Label(self, text='----------------装载占空比----------------')
        self.label5.pack()
        self.loadInput = Entry(self)
        self.loadInput.pack()
        self.loadButton = Button(self, text='装载电机占空比', command=self.changeLoadDutyCycle)
        self.loadButton.pack()
        self.label5 = Label(self, text='----------------调整角度----------------')
        self.label5.pack()
        self.PWMInput = Entry(self)
        self.PWMInput.pack()
        self.PWMButton = Button(self, text='调整角度', command=self.movePWM)
        self.PWMButton.pack()
        self.label6 = Label(self, text='----------------PWM电机速度----------------')
        self.label6.pack()
        self.PWMSpeedInput = Entry(self)
        self.PWMSpeedInput.pack()
        self.PWMSpeedButton = Button(self, text='调整速度', command=self.changePWMSpeed)
        self.PWMSpeedButton.pack()
        self.label6 = Label(self, text='----------------强制退出----------------')
        self.label6.pack()
        self.exitButton = Button(self, text='退出', command=self.quit)
        self.exitButton.pack()
        
        
    def changeUpDutyCycle(self):
        dc = int(self.upInput.get())
        driver.changeUpDutyCycle(dc)
        
    
    def changeDownDutyCycle(self):
        dc = int(self.downInput.get())
        driver.changeDownDutyCycle(dc)
        
    
    def changeLoadDutyCycle(self):
        dc = int(self.loadInput.get())
        driver.changeLoadDutyCycle(dc)
    
    
    def changePWMSpeed(self):
        factor = float(self.PWMSpeedInput.get())
        driver.changePWMSpeed(factor)
        
        
    def movePWM(self):
        dc = int(self.PWMInput.get())
        driver.movePWM(dc)


app = Application()
# 设置窗口标题:
app.master.title('Hello World')
# 主消息循环:
try:
    app.mainloop()
finally:
    driver.destroy()