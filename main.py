from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.uix.spinner import Spinner
from openpyxl import Workbook
import datetime


class BudgetTrackerApp(App):
    def build(self):
        self.title = "My Budget Tracker"
        self.root = BoxLayout(orientation='vertical', padding=10, spacing=10)
        
        # Title Label
        title_label = Label(text="Welcome to My Budget Tracker", font_size='50sp', color=(1, 1, 1, 1))
        self.root.add_widget(title_label)
        
        # Instruction Label
        instruction_label = Label(text="Please choose either income or expense", font_size='30sp', color=(1, 1, 1, 1))
        self.root.add_widget(instruction_label)
        
        # Spinner for choosing income or expense
        type_set = {'Income', 'Expense'}
        self.type_spinner = Spinner(
            text='Select Type',
            font_size='30sp',
            values=type_set,
            size_hint=(None, None),
            size=(300, 50),
            pos_hint={'center_x': .5}
        )
        self.root.add_widget(self.type_spinner)
        # Spinner for choosing income source aligned to the type spinner
        inc_cat_set = {'Salary', 'Business', 'Investment', 'Other'}
        self.inc_cat_spinner = Spinner(
            text='Select Source',
            font_size='30sp',
            values=inc_cat_set,
            size_hint=(None, None),
            size=(300, 50),
            pos=(100, 100),
            pos_hint={'center_x': .5}
        )
        self.root.add_widget(self.inc_cat_spinner)
        

        # Spinner for choosing category aligned to the type spinner
        exp_cat_set = {'Food', 'Transport', 'Entertainment', 'Other'}
        self.exp_cat_spinner = Spinner(
            text='Select Category',
            font_size='30sp',
            values=exp_cat_set,
            size_hint=(None, None),
            size=(300, 50),
            pos=(300, 100),
            pos_hint={'center_x': .5}
        )
    
        self.root.add_widget(self.exp_cat_spinner)
        

        # TextInput for amount
        self.amount_input = TextInput(hint_text='Enter amount', multiline=False, font_size='30sp', size_hint=(None, None), size=(300, 50), pos_hint={'center_x': .5})
        self.root.add_widget(self.amount_input)
        
        # Button to submit
        self.submit_button = Button(text='Submit', on_press=self.on_submit, size_hint=(None, None), size=(200, 44), pos_hint={'center_x': .5})
        self.root.add_widget(self.submit_button)
        
        self.type_spinner.bind(text=self.change_spinner)

        return self.root

    def change_spinner(self, spinner, value):

        #only one spinner should appear at a time
        if value == 'Income':
            self.inc_cat_spinner.disabled = False
            self.exp_cat_spinner.disabled = True
        elif value == 'Expense':
            self.inc_cat_spinner.disabled = True
            self.exp_cat_spinner.disabled = False
    def on_submit(self, instance):
        self.trans = my_app.type_spinner.text
        self.income = my_app.inc_cat_spinner.text
        self.expense = my_app.exp_cat_spinner.text
        self.amount = my_app.amount_input.text

        workbook = Workbook()
        sheet = workbook.active
        sheet.title = "Budget Tracker"
        sheet.append(["id","date" ,"Transaction Type", "Category", "Amount"])

        if self.trans == 'Income':
            sheet.append([1, datetime.datetime.now().strftime("%Y-%m-%d"), self.trans, self.income, self.amount])
        elif self.trans == 'Expense':
            sheet.append([1, datetime.datetime.now().strftime("%Y-%m-%d"), self.trans, self.expense, self.amount])

        workbook.save("data.xlsx")

my_app = BudgetTrackerApp()
my_app.run()

