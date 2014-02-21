#(GUI)Number Guessing - Created by: Michael Smith
#Version: 1.2.1 - Work in progress (Very buggy)
#Todo: Add int check,
#Fix reset button.
from tkinter import *
import random
number = random.randint(1,20)
guessesTaken = 0
class Application(Frame):
    def __init__(self, master):
        Frame.__init__(self, master)
        self.grid()
        self.create_widgets()
    def create_widgets(self):
        self.inst_lbl = Label(self, text = "Number Guessing Game - 1.2.1 (GUI Edition)")
        self.inst_lbl.grid(row = 0, column = 0, columnspan = 2, sticky = W)
             
        self.guess_lbl = Label(self, text = "Take a Guess.")
        self.guess_lbl.grid(row = 2, column = 0, sticky = W) 
        self.guess_ent = Entry(self)
        self.guess_ent.grid(row = 2, column = 1, sticky = W) 
        self.gap1_lbl = Label(self, text = " ")
        self.gap1_lbl.grid(row = 3, column = 0, sticky = W)
        
        self.submit_bttn = Button(self, text = "Submit", command = self.reveal)
        self.submit_bttn.grid(row = 6, column = 0, sticky = W)
        self.gap2_lbl = Label(self, text = " ")
        self.gap2_lbl.grid(row = 7, column = 0, sticky = W)

        #Fix me plox
        self.reset_bttn = Button(self, text = "Reset (Broken)", command = self.reveal)
        self.reset_bttn.grid(row = 6, column = 1, sticky = W)
        
        self.display1_txt = Text(self, width = 45, height = 1, wrap = WORD)
        self.display1_txt.grid(row = 8, column = 0, columnspan = 2, sticky = W)
        self.display2_txt = Text(self, width = 45, height = 1, wrap = WORD)
        self.display2_txt.grid(row = 9, column = 0, columnspan = 2, sticky = W)
        self.display3_txt = Text(self, width = 45, height = 1, wrap = WORD)
        self.display3_txt.grid(row = 10, column = 0, columnspan = 2, sticky = W)
        self.display4_txt = Text(self, width = 45, height = 1, wrap = WORD)
        self.display4_txt.grid(row = 11, column = 0, columnspan = 2, sticky = W)
        self.display5_txt = Text(self, width = 45, height = 1, wrap = WORD)
        self.display5_txt.grid(row = 12, column = 0, columnspan = 2, sticky = W)
        
    def reveal(self):
        global guessesTaken
        guess = self.guess_ent.get()
        if int(guess) > int(number):
            result_msg = "Lower ..."
            guessesTaken += 1
        if int(guess) < int(number):
            result_msg = "Higher ..."
            guessesTaken += 1
        if int(guess) == int(number):
            result_msg = "You got it."
            guessesTaken += 1
        welcome_msg = "Welcome "
        credit_msg = "Created by Michael Smith"
        guess_msg = "Your guess was: " + guess
        tries_msg = "You've taken " + str(guessesTaken) + " guesses out of your 6"
        if guessesTaken > 6:
            welcome_msg = "End of Game."
            guess_msg = "You had too many tires."
            result_msg = " "
            tries_msg = " "
        self.display1_txt.delete(0.0, END)
        self.display1_txt.insert(0.0, welcome_msg)
        self.display2_txt.delete(0.0, END)
        self.display2_txt.insert(0.0, guess_msg)
        self.display3_txt.delete(0.0, END)
        self.display3_txt.insert(0.0, result_msg)
        self.display4_txt.delete(0.0, END)
        self.display4_txt.insert(0.0, tries_msg)
        self.display5_txt.delete(0.0, END)
        self.display5_txt.insert(0.0, credit_msg)
    
mickgui = Tk()
mickgui.title("MickGUI 1.0")
mickgui.geometry("325x215")
mickgui.resizable(0,0)
app = Application(mickgui)
mickgui.mainloop()
