from tkinter import *
large_font = ('Verdana', 20)
small_font = ('Verdana', 10)

class Calculator():
    def __init__(self):
        self.gui = Tk()
        self.gui.title("Some Calculator")

        ## Buttons
        #Main entry
        e = Entry(self.gui, width=16, borderwidth=5, font=large_font)
        e.grid(row=0, column=0, columnspan=3)

        #Number Buttons
        button_1 = Button(self.gui, text='1', padx=40, pady=20, font=small_font, command=self.click1)
        button_2 = Button(self.gui, text='2', padx=40, pady=20, font=small_font, command=self.click1)
        button_3 = Button(self.gui, text='3', padx=40, pady=20, font=small_font, command=self.click1)
        button_4 = Button(self.gui, text='4', padx=40, pady=20, font=small_font, command=self.click1)
        button_5 = Button(self.gui, text='5', padx=40, pady=20, font=small_font, command=self.click1)
        button_6 = Button(self.gui, text='6', padx=40, pady=20, font=small_font, command=self.click1)
        button_7 = Button(self.gui, text='7', padx=40, pady=20, font=small_font, command=self.click1)
        button_8 = Button(self.gui, text='8', padx=40, pady=20, font=small_font, command=self.click1)
        button_9 = Button(self.gui, text='9', padx=40, pady=20, font=small_font, command=self.click1)
        button_0 = Button(self.gui, text='0', padx=40, pady=20, font=small_font, borderwidth=0, command=self.click1)

        button_dot = Button(self.gui, text='.', padx=40, pady=20, font=small_font, command=self.click1, background='lightgrey')
        button_posneg = Button(self.gui, text=chr(177), padx=37, pady=20, font=small_font, command=self.click1)

        #Operation Buttons
        button_equal    = Button(self.gui, text='=', padx=40, pady=20, font=small_font)
        button_add      = Button(self.gui, text='+', padx=40, pady=20, font=small_font)
        button_minus    = Button(self.gui, text='-', padx=40, pady=20, font=small_font)
        button_multiply = Button(self.gui, text='x', padx=40, pady=20, font=small_font)
        button_divide   = Button(self.gui, text=chr(247), padx=40, pady=20, font=small_font)
        button_inverse  = Button(self.gui, text='1/x', padx=40, pady=20, font=small_font)
        button_square   = Button(self.gui, text='x'+chr(178), padx=40, pady=20, font=small_font)
        button_sqrt     = Button(self.gui, text='Sqrt', padx=36, pady=20, font=small_font)

        #Place buttons
        button_inverse.grid(row=1, column=0)
        button_square.grid(row=1, column=1)
        button_sqrt.grid(row=1, column=2)
        button_divide.grid(row=1, column=3)

        button_7.grid(row=2, column=0)
        button_8.grid(row=2, column=1)
        button_9.grid(row=2, column=2)
        button_multiply.grid(row=2, column=3)

        button_4.grid(row=3, column=0)
        button_5.grid(row=3, column=1)
        button_6.grid(row=3, column=2)
        button_minus.grid(row=3, column=3)

        button_1.grid(row=4, column=0)
        button_2.grid(row=4, column=1)
        button_3.grid(row=4, column=2)
        button_add.grid(row=4, column=3)

        button_posneg.grid(row=5, column=0)
        button_0.grid(row=5, column=1)
        button_dot.grid(row=5, column=2)
        button_equal.grid(row=5, column=3)




    def start(self):
        """
        Main loop
        :return:
        """
        self.gui.protocol("WM_DELETE_WINDOW", self.clickExitNow)
        self.gui.mainloop()
        self.gui.destroy()

    def clickExitNow(self):
        exit()

    def click1(self):
        pass


CALC = Calculator()
CALC.start()