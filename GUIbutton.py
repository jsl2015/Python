#!/usr/bin/env python 
# -*- coding:utf-8 -*-

from Tkinter import * 
import tkMessageBox


class Application(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()

    def createWidgets(self):
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alterButton = Button(self, text='test', command=self.text)
        self.alterButton.pack()

    def text(self):
        name = self.nameInput.get() or 'world'
        tkMessageBox.showinfo('Message', 'Hello, %s' % name)

app = Application()
app.master.title('Hello World')
app.mainloop()
tkMessageBox.showinfo()