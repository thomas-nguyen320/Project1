from tkinter import *
import formulas

class GUI:
    def __init__(self, window) -> None:
        '''
        Constructor to create initial state of a GUI object.
        :param window: This will help create the GUI window.
        '''
        self.added_num = ''
        self.num_li = []

        self.window = window
        self.frame_operator = Frame(self.window)
        self.label_operator = Label(self.frame_operator, text='Operator:')
        self.operator_entry = Entry(self.frame_operator)
        self.label_operator.pack(side='left',padx=5)
        self.operator_entry.pack(pady=5)
        self.frame_operator.pack()

        self.frame_valid_operators = Frame(self.window)
        self.label_valid_operators = Label(self.frame_valid_operators, text='Valid Operators: Add,Subtract,Multiply,Divide')
        self.label_valid_operators.pack(side='left', padx=5)
        self.frame_valid_operators.pack(pady=5)

        self.frame_numsRow1 = Frame(self.window)
        self.one_btn = Button(self.frame_numsRow1,text ='1', command=lambda: self.setup_num('1'))
        self.two_btn = Button(self.frame_numsRow1, text='2', command=lambda: self.setup_num('2'))
        self.three_btn = Button(self.frame_numsRow1, text='3', command=lambda: self.setup_num('3'))
        self.one_btn.pack(side='left',padx=5)
        self.two_btn.pack(side='left', padx=5)
        self.three_btn.pack(side='left', padx=5)
        self.frame_numsRow1.pack(pady=5)

        self.frame_numsRow2 = Frame(self.window)
        self.four_btn = Button(self.frame_numsRow2, text='4', command=lambda: self.setup_num('4'))
        self.five_btn = Button(self.frame_numsRow2, text='5', command=lambda: self.setup_num('5'))
        self.six_btn = Button(self.frame_numsRow2, text='6', command=lambda: self.setup_num('6'))
        self.four_btn.pack(side='left', padx=5)
        self.five_btn.pack(side='left', padx=5)
        self.six_btn.pack(side='left', padx=5)
        self.frame_numsRow2.pack(pady=5)

        self.frame_numsRow3 = Frame(self.window)
        self.seven_btn = Button(self.frame_numsRow3, text='7', command=lambda: self.setup_num('7'))
        self.eight_btn = Button(self.frame_numsRow3, text='8', command=lambda: self.setup_num('8'))
        self.nine_btn = Button(self.frame_numsRow3, text='9', command=lambda: self.setup_num('9'))
        self.seven_btn.pack(side='left', padx=5)
        self.eight_btn.pack(side='left', padx=5)
        self.nine_btn.pack(side='left', padx=5)
        self.frame_numsRow3.pack(pady=5)

        self.frame_numRow4 = Frame(self.window)
        self.neg_btn = Button(self.frame_numRow4,text='-', command=lambda : self.setup_num('-'))
        self.zero_btn = Button(self.frame_numRow4, text='0',command=lambda: self.setup_num('0'))
        self.decimal_btn = Button(self.frame_numRow4,text='.', command=lambda: self.setup_num('.'))
        self.neg_btn.pack(side='left',padx=5)
        self.zero_btn.pack(side='left',padx=5)
        self.decimal_btn.pack(side='left',padx=5)
        self.frame_numRow4.pack(pady=5)

        self.frame_addNum = Frame(self.window)
        self.add_num_btn = Button(self.frame_addNum, text='Add Number', command=self.add_num_to_calc)
        self.add_num_btn.pack(pady=5)
        self.frame_addNum.pack(anchor='center')

        self.current_num_label= Label(self.window,text='Num: ')
        self.current_num_label.place(x=280,y=100)

        self.frame_buttons = Frame(self.window)
        self.submit_btn = Button(self.frame_buttons, text='Submit',command=self.submit)
        self.reset_btn = Button(self.frame_buttons, text='Reset',command=self.reset)
        self.submit_btn.pack(side='left',padx=5)
        self.reset_btn.pack(side='left',padx=5)
        self.frame_buttons.pack(side='bottom',pady=20)

        self.frame_answer = Frame(self.window)
        self.label_answer = Label(self.window, text='Add numbers to start')
        self.label_answer.pack(side='bottom',anchor='center',pady=5)
        self.frame_answer.pack(anchor='center')


    def setup_num(self,num: float) -> None:
        '''
        This will help the user visualize what number they are inputting in the GUI application
        This will also store the number the user inputted until it's added to the list
        :param num: This parameter will add the number pressed to a variable
        '''
        self.added_num += num
        self.current_num_label.config(text=f'Num: {self.added_num}')


    def add_num_to_calc(self) -> None:
        '''
        This method will add the number inputted by the user to a list for calculation purposes
        This will also show the list of current numbers in the GUI
        '''
        try:
            self.num_li.append(self.added_num)
            self.num_li = [float(i) for i in self.num_li]
            self.label_answer.config(text=f'Current Numbers:{self.num_li}')
            self.current_num_label.config(text='Num: ')
            self.added_num = ''
        except ValueError:
            self.num_li.pop()
            self.added_num = ''
            self.current_num_label.config(text='Enter a Number')


    def submit(self) -> None:
        '''
        This method will check the operator and numbers the user has inputted.
        If they are valid, then it will do the calculations according to the operator.
        '''
        try:
            valid_operators = ['add','subtract','multiply','divide']
            num_op_list = []
            operator = self.operator_entry.get().strip().lower()
            num_op_list.append(operator)
            num_op_list.extend(self.num_li)
            if operator in valid_operators:
                if len(num_op_list[1::]) > 1:
                    if num_op_list[0] == 'add':
                        answer = formulas.add(num_op_list[1::])
                        self.label_answer.config(text=f'Answer: {answer:.2f}')
                    elif num_op_list[0] == 'subtract':
                        answer = formulas.subtract(num_op_list[1::])
                        self.label_answer.config(text=f'Answer: {answer:.2f}')
                    elif num_op_list[0] == 'multiply':
                        answer = formulas.multiply(num_op_list[1::])
                        self.label_answer.config(text=f'Answer: {answer:.2f}')
                    elif num_op_list[0] == 'divide':
                        try:
                            answer = formulas.divide(num_op_list[1::])
                            self.label_answer.config(text=f'Answer: {answer:.2f}')
                        except ZeroDivisionError:
                            self.label_answer.config(text='Cannot divide by zero')
                else:
                    self.label_answer.config(text='Enter more than 1 number')
            else:
                raise TypeError

        except TypeError:
            self.added_num = ''
            self.label_answer.config(text='Please enter add,subtract,multiply, or divide for operator')
            self.current_num_label.config(text='Num: ')

        self.operator_entry.delete(0, END)
        self.operator_entry.focus()

    def reset(self) -> None:
        '''
        This will reset the labels to its default values and make the cursor focused on the first input box.
        '''
        self.operator_entry.delete(0,END)
        self.num_li = []
        self.label_answer.config(text='Add numbers to start')
        self.current_num_label.config(text='Num: ')
        self.added_num = ''
        self.operator_entry.focus()