import tkinter as tk
from tkinter import messagebox
from calculator import Calculator
from style_templates import Button1, Label1, Entry1

class App(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.master.geometry("250x50")
        self.master.title("Home")
        self.master.configure(background="#ffffff")
        self.frame_NPV = tk.Frame()
        # self.years_entry_field = self.make_NPV_calulator()
        self.make_get_NPV_entry_field_button()

        self.frame_NPV.pack()

        self.pack()


    def make_NPV_calulator(self):
        # NPV
        NPV_label = Label1(master=self.frame_NPV, text="NPV Calculator")
        NPV_label.pack()
        # NPV_label1 = Label1(master=self.frame_NPV, text="Enter time (in years)")
        # NPV_label1.pack()
        # years_NPV = Entry1(master=self.frame_NPV, bg="grey", width=50)
        # years_NPV.pack()


    def make_get_NPV_entry_field_button(self):
        npv_calc_button = Button1(master=self.frame_NPV, text="Calc new NPV", width=20, height=3,command=lambda: self.calc_new_NPV())
        npv_calc_button.pack()


    def calc_new_NPV(self):
        self.create_NPV_window()
    #     years = self.years_entry_field.get()
    #     if(years.isdigit()):
    #         self.create_NPV_window(years)
    #     else:
    #         print("years is not an integer")

    def create_NPV_window(self):
        self.npv_window = tk.Toplevel(self)
        self.npv_window.configure(background="#abc8f5")
        self.npv_window.geometry("500x800")
        self.npv_window.title("NPV Calculator")
        self.frame_results = tk.Frame(self.npv_window)

        self.profits_entry_field_label = Label1(self.npv_window, text="Enter Benefit Values for each year (seperated by space)")
        self.profits_entry_field = Entry1(self.npv_window )
        self.costs_entry_field_label= Label1(self.npv_window, text="Enter Losses Values for each year (seperated by space)")
        self.costs_entry_field = Entry1(self.npv_window)
        self.initial_costs_entry_label = Label1(self.npv_window, text="Enter Inital Costs (one value)")
        self.initial_costs_entry_field = Entry1(self.npv_window)
        self.discount_rate_entry_field_label = Label1(self.npv_window, text="Enter Discount Rate (in percent)")
        self.discount_rate_entry_field = Entry1(self.npv_window)

        # frame_results.destroy()
        make_calc_NPV_button = Button1(self.npv_window, text="Calc NPV", command=lambda: self.get_profit_costs(self.npv_window))

        self.profits_entry_field_label.pack()
        self.profits_entry_field.pack()
        self.costs_entry_field_label.pack()
        self.costs_entry_field.pack()
        self.initial_costs_entry_label.pack()
        self.initial_costs_entry_field.pack()
        self.discount_rate_entry_field_label.pack()
        self.discount_rate_entry_field.pack()

        make_calc_NPV_button.pack()

        self.npv_window.mainloop()

    # def make_calc_NPV_button(self):
    #     npv_calc_button = tk.Button(master=self.frame_NPV, bg="green", text="Calc NPV",width=8,height=1,command=lambda: self.get_profit_costs())
    #     npv_calc_button.pack()

    def get_profit_costs(self, current_window):
        #delete frame results if it exists
        self.frame_results.destroy()
        self.frame_results = tk.Frame(self.npv_window)

        profits = self.profits_entry_field.get()
        costs = self.costs_entry_field.get()
        initial_costs = self.initial_costs_entry_field.get()
        discount_rates = self.discount_rate_entry_field.get()

        profits = profits.split(" ")
        costs = costs.split(" ")
        discount_rates = discount_rates.split(" ")
        # print(profits)
        # print(costs)
        # print(discount_rates)


        #check if all input values are numbers
        if(self.input_checker(profits, costs, initial_costs, discount_rates)):
            calculator = Calculator(profits, costs,initial_costs, discount_rates)

            net_benefits = Label1(self.frame_results, text="Net Benefits: " + str(calculator.net_benefits))
            net_benefits.pack()

            ratio = calculator.benefits_costs_ratio
            text = "Benefit/Cost ratio: " + str(ratio) + "\n"
            if ratio < 1:
                text += """Benefit cost ratio is less than 1, this project is not worth investing in. This is no good"""
            elif ratio == 1:
                text += """Benefit cost ratio is equal to 1, this project will have no return but also no loss. This might be okay"""
            else:
                text += """Benefit cost ratio is greater than 1, this project is worth investing in. Great success"""

            benefits_cost_ratio = Label1(self.frame_results, height=2, text=text)
            benefits_cost_ratio.pack()

            pay_back_time = Label1(self.frame_results, text="Pay Back Time (avg): " + str(calculator.pay_back_time_avg) + " time steps")
            pay_back_time.pack()

            NPV = Label1(self.frame_results, text="NPV (without inital costs): " + str(calculator.NPV))
            NPV.pack()

            NPV_initial_costs = Label1(self.frame_results, text="NPV with inital costs: " + str(calculator.NPV_with_initial_costs))
            NPV_initial_costs.pack()

            IRR = Label1(self.frame_results, text="IRR: " + str(calculator.irr_value)+ "%")
            IRR.pack()

            self.frame_results.pack()


    def is_float(self, n):
        try:
            float_n = float(n)
        except ValueError:
            return False
        else:
            return True

    # function checks if all input values are numbers
    def input_checker(self, benefits, costs, inital_costs, discount_rates):
        for benefit in benefits:
            if(not self.is_float(benefit)):
              tk.messagebox.showwarning("Error", "Benefit values must be numbers. " + benefit + " is not a number")
              return False

        for cost in costs:
            if(not self.is_float(cost)):
                tk.messagebox.showwarning("Error", "Cost values must be numbers")
                return False
        for discount_rate in discount_rates:
            if(not self.is_float(discount_rate)):
                tk.messagebox.showwarning("Error", "Discount rates must be numbers")
                return False
        if(not self.is_float(inital_costs)):
            tk.messagebox.showwarning("Error", "Initial costs must be a number")
            return False

        if(len(benefits) != len(costs) or (len(benefits) != len(discount_rates) and len(discount_rates) != 1)):
            tk.messagebox.showwarning("Error", "Number of benefits, costs and discount rates must be equal (Exception: discount rate can also be one value)")
            return False

        return True

home = App()



home.mainloop()
