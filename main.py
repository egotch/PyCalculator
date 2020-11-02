from tkinter import *
import tkinter as tk
large_font = ('Verdana', 20)
small_font = ('Verdana', 10)

evaluators = [
    '+', '-', '\\', 'x'
]

def isvalidvalue(some_val):
    try:
        float(some_val)
        return True
    except:
        return False

class Calculator():
    def __init__(self):
        self.gui = Tk()
        self.gui.title("Py Calculator")
        self.gui.attributes('-alpha', 0.9)
        self.gui.configure(bg='grey27')

        self.curr_eval = StringVar()
        self.curr_equation = StringVar()
        self.curr_value = IntVar()
        self.curr_value.set(0)
        self.curr_display_val = StringVar()
        self.curr_display_val.set('')
        self.last_click = StringVar()

        ## Buttons
        #Main entry
        equation = Entry(self.gui, textvariable=self.curr_equation, width=16, font=small_font, relief='flat', background=self.gui['background'], foreground='white')
        equation.grid(row=0, column=0, columnspan=3)

        evaluation = Entry(self.gui, textvariable=self.curr_display_val, width=16, borderwidth=5, font=large_font, relief='flat', background=self.gui['background'], foreground='white')
        evaluation.grid(row=1, column=0, columnspan=3)


        #Number Buttons
        button_args = {'font':small_font, 'relief':'flat', 'background':'black', 'foreground':'white', 'activebackground':'grey40'}
        number_padding={'padx':45, 'pady':19}
        button_1 = HoverButton(self.gui, text='1', **number_padding, **button_args, command=lambda: self.clickNumber(1))
        button_2 = HoverButton(self.gui, text='2', **number_padding, **button_args, command=lambda: self.clickNumber(2))
        button_3 = HoverButton(self.gui, text='3', **number_padding, **button_args, command=lambda: self.clickNumber(3))
        button_4 = HoverButton(self.gui, text='4', **number_padding, **button_args, command=lambda: self.clickNumber(4))
        button_5 = HoverButton(self.gui, text='5', **number_padding, **button_args, command=lambda: self.clickNumber(5))
        button_6 = HoverButton(self.gui, text='6', **number_padding, **button_args, command=lambda: self.clickNumber(6))
        button_7 = HoverButton(self.gui, text='7', **number_padding, **button_args, command=lambda: self.clickNumber(7))
        button_8 = HoverButton(self.gui, text='8', **number_padding, **button_args, command=lambda: self.clickNumber(8))
        button_9 = HoverButton(self.gui, text='9', **number_padding, **button_args, command=lambda: self.clickNumber(9))
        button_0 = HoverButton(self.gui, text='0', **number_padding, **button_args, command=lambda: self.clickNumber(0))

        button_dot = HoverButton(self.gui, text='.', padx=45.55, pady=20, **button_args, command=lambda: self.clickNumber('.'))
        button_posneg = HoverButton(self.gui, text=chr(177), padx=44, pady=20, **button_args)

        #Operation Buttons
        operation_args = {'font':small_font, 'relief':'flat', 'background':'grey13', 'foreground':'white', 'activebackground':'grey40'}
        equals_args = {'font':small_font, 'relief':'flat', 'background':'blue4', 'foreground':'white', 'activebackground':'blue2'}
        button_equal    = HoverButton(self.gui, text='=', padx=40, pady=20, **equals_args, command=lambda: self.clickOperation('='))
        button_add      = HoverButton(self.gui, text='+', padx=40, pady=20, **operation_args, command=lambda: self.clickOperation('+'))
        button_minus    = HoverButton(self.gui, text='-', padx=40, pady=20, **operation_args, command=lambda: self.clickOperation('-'))
        button_multiply = HoverButton(self.gui, text='x', padx=40, pady=20, **operation_args, command=lambda: self.clickOperation('x'))
        button_divide   = HoverButton(self.gui, text=chr(247), padx=38, pady=20, **operation_args, command=lambda: self.clickOperation(chr(247)))
        button_inverse  = HoverButton(self.gui, text='1/x', padx=40, pady=20, **operation_args)
        button_square   = HoverButton(self.gui, text='x'+chr(178), padx=40, pady=20, **operation_args)
        button_sqrt     = HoverButton(self.gui, text='Sqrt', padx=36, pady=20, **operation_args)

        #Place buttons
        button_inverse.grid(row=2, column=0)
        button_square.grid(row=2, column=1)
        button_sqrt.grid(row=2, column=2)
        button_divide.grid(row=2, column=3)

        button_7.grid(row=3, column=0)
        button_8.grid(row=3, column=1)
        button_9.grid(row=3, column=2)
        button_multiply.grid(row=3, column=3)

        button_4.grid(row=4, column=0)
        button_5.grid(row=4, column=1)
        button_6.grid(row=4, column=2)
        button_minus.grid(row=4, column=3)

        button_1.grid(row=5, column=0)
        button_2.grid(row=5, column=1)
        button_3.grid(row=5, column=2)
        button_add.grid(row=5, column=3)

        button_posneg.grid(row=6, column=0)
        button_0.grid(row=6, column=1)
        button_dot.grid(row=6, column=2)
        button_equal.grid(row=6, column=3)

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

    def clickNumber(self, number):
        if self.last_click.get() in evaluators:
            self.curr_display_val.set('')
        elif self.last_click.get() == '=':
            self.curr_display_val.set('')
            self.curr_equation.set('')
            self.curr_eval.set('')
        self.curr_display_val.set(self.curr_display_val.get() + str(number))
        self.last_click.set(str(number))

    def clickOperation(self, operation):
        if self.last_click.get() in evaluators:
            return
        elif operation == '=':
            if self.curr_equation.get()[-2] == '=':
                return
            new_equation = self.curr_equation.get()
            new_equation += self.curr_display_val.get()
            self.evaluateExpression(new_equation)
            new_equation += ' = '
            self.curr_equation.set(new_equation)
            self.last_click.set('=')
        else:
            if len(self.curr_equation.get())>0 and self.curr_equation.get().strip()[-1] == '=':
                new_equation = self.curr_eval.get() + ' ' + operation + ' '
                self.curr_eval.set('')
                self.curr_equation.set(new_equation)
            else:
                new_equation = self.curr_equation.get()
                new_equation += self.curr_display_val.get()
                new_equation += ' ' + operation + ' '
                if self.curr_equation.get() != '' and self.curr_equation.get()[len(self.curr_equation.get()) - 2] in evaluators:
                    self.evaluateExpression(new_equation)
                else:
                    self.curr_display_val.set('')

                self.curr_equation.set(new_equation)
            self.last_click.set(operation)

    def evaluateExpression(self, equation):
        """
        evaluates expression currently set in curr_equation
        """

        ops = equation.split(' ')
        value = None
        e = 0
        while e < len(ops):
            if isvalidvalue(ops[e]) is True:
                if value is None:
                    value = float(ops[e])
                    e += 1
                else:
                    pass
            elif ops[e+1] == '':
                e += 2
                pass
            #addition
            elif ops[e] == '+':
                value += float(ops[e+1])
                e += 2
            #subtraction
            elif ops[e] == '-':
                value -= float(ops[e+1])
                e += 2
            #multiplication
            elif ops[e] == 'x':
                value = value * float(ops[e+1])
                e += 2
            elif ops[e] == chr(247):
                value = value / float(ops[e+1])
                e += 2
        if value.is_integer():
            self.curr_eval.set(str(int(value)))
            self.curr_display_val.set(str(int(value)))
        else:
            self.curr_eval.set(str(value))
            self.curr_display_val.set(str(value))



class HoverButton(tk.Button):
    def __init__(self, master, **kw):
        tk.Button.__init__(self,master=master,**kw)
        self.defaultBackground = self["background"]
        self.bind("<Enter>", self.on_enter)
        self.bind("<Leave>", self.on_leave)

    def on_enter(self, e):
        self['background'] = self['activebackground']

    def on_leave(self, e):
        self['background'] = self.defaultBackground



CALC = Calculator()
CALC.start()


