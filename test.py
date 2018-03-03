# coding=utf-8
import time, threading, random, Queue
import serialTransmitter
from Tkinter import *

RANDOM_MODE = 0
FIXED_MODE = 1
mode = RANDOM_MODE
position = random.randint(0, 10)


def makePosFunc(pos):
    def inner():
        global position
        position = pos

    return inner


def switchToRandomMode():
    global mode, RANDOM_MODE
    mode = RANDOM_MODE
    print('change to random',mode)


def switchToFixedMode():
    global mode, FIXED_MODE
    mode = FIXED_MODE
    print('change to fixed',mode)


class Application(Frame):
    def __init__(self, master, queue, endCommand):
        Frame.__init__(self, master)
        self.pack()

        self.queue = queue

        self.label1 = Label(self, text='----随机模式----')
        self.label1.grid(row=0)

        self.randomModeButton = Button(self, text='随机发球', command=switchToRandomMode)
        self.randomModeButton.grid(row=1)

        self.label2 = Label(self, text='----定点模式----')
        self.label2.grid(row=2)

        self.fixedModeButton = Button(self, text='定点发球', command=switchToFixedMode)
        self.fixedModeButton.grid(row=3, column=0)

        self.positon0Button = Button(self, text='0', command=makePosFunc(0))
        self.positon0Button.grid(row=4, column=0)
        self.positon1Button = Button(self, text='1', command=makePosFunc(1))
        self.positon1Button.grid(row=4, column=1)
        self.positon2Button = Button(self, text='2', command=makePosFunc(2))
        self.positon2Button.grid(row=4, column=2)
        self.positon3Button = Button(self, text='3', command=makePosFunc(3))
        self.positon3Button.grid(row=4, column=3)
        self.positon4Button = Button(self, text='4', command=makePosFunc(4))
        self.positon4Button.grid(row=4, column=4)
        self.positon5Button = Button(self, text='5', command=makePosFunc(5))
        self.positon5Button.grid(row=5, column=0)
        self.positon6Button = Button(self, text='6', command=makePosFunc(6))
        self.positon6Button.grid(row=5, column=1)
        self.positon7Button = Button(self, text='7', command=makePosFunc(7))
        self.positon7Button.grid(row=5, column=2)
        self.positon8Button = Button(self, text='8', command=makePosFunc(8))
        self.positon8Button.grid(row=5, column=3)
        self.positon9Button = Button(self, text='9', command=makePosFunc(9))
        self.positon9Button.grid(row=5, column=4)

    def processIncoming(self):
        while self.queue.qsize():
            try:
                msg = self.queue.get(0)
                print msg
            except Queue.Empty:
                pass


class ThreadedClient():
    def __init__(self, master):
        self.master = master
        self.queue = Queue.Queue()
        self.gui = Application(master, self.queue, self.endApplication)
        self.running = True
        self.thread1 = threading.Thread(target=self.workerThread1)
        self.thread1.start()
        self.periodicCall()

    def periodicCall(self):
        self.master.after(200, self.periodicCall)
        self.gui.processIncoming()
        if not self.running:
            self.master.destroy()

    def workerThread1(self):
        global position, RANDOM_MODE, mode
        while self.running:
            time.sleep(1)
            if mode == RANDOM_MODE:
                position = random.randint(0, 10)
            # serialTransmitter.move(position)
            print('move  {}'.format(position))

    def endApplication(self):
        self.running = False
        print('end')
        # serialTransmitter.destroy()


# serialTransmitter.init()

rand = random.Random()
root = Tk()
client = ThreadedClient(root)
root.mainloop()
