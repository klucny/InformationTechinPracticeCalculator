from sympy.solvers import solve
from sympy import symbols
class Calculator():
    def __init__(self,benefits, costs, initial_project_costs, discount_rates):
        self.benefits = benefits
        self.costs = costs
        self.discount_rates = discount_rates
        self.initial_project_costs = initial_project_costs
        # convert all values to float
        self.to_float()
        self.benefits_costs_ratio = self.calc_benefit_cost_ratio(self.benefits, self.costs)
        self.net_benefits = self.calc_net_benefits(self.benefits, self.costs)
        self.pay_back_time_avg = 0
        self.NPV = 0
        self.irr_value = 0
        self.pay_back_time = 0

        self.calc_pay_back_time()
        self.calc_pay_back_time_avg()
        self.calc_NPV()
        self.calc_IRR()


    def to_float(self):
        for idx in range(len(self.benefits)):
            self.benefits[idx] = float(self.benefits[idx])
            self.costs[idx] = float(self.costs[idx])
            self.discount_rates[idx] = float(self.discount_rates[idx])
        self.initial_project_costs = float(self.initial_project_costs)
    def calc_benefit_cost_ratio(self, benefits, costs):
        tot_benefit = 0
        tot_costs = 0

        for benefit in benefits:
            tot_benefit += float(benefit)
        for cost in costs:
            tot_costs += float(cost)

        return tot_benefit / tot_costs

    def calc_net_benefits(self, benefits, costs):
        net_benefits = []

        for idx in range(len(benefits)):
            net_benefits.append(benefits[idx] - costs[idx])

        print("Net Benefits: "+ str(net_benefits))
        return net_benefits

    def calc_pay_back_time_avg(self):
        total = 0
        for net_benefit in self.net_benefits:
            total += net_benefit
        self.pay_back_time_avg = self.initial_project_costs/(total/len(self.net_benefits))

    def calc_pay_back_time(self):
        pass

    def calc_NPV(self):
        for idx in range(len(self.net_benefits)):
            self.NPV += self.net_benefits[idx] / (1 + self.discount_rates[idx])**(idx+1)
        return self.NPV

    def NPV_for_IRR(self, rate):
        total = 0
        for idx in range(len(self.net_benefits)):
            total += self.net_benefits[idx] / ((1 + rate) ** (idx+1))
        return total

    # implementation might be incorrect
    def calc_IRR(self):
        rate = symbols('rate', real = True)
        npv_equation = self.NPV_for_IRR(rate)
        self.irr_value = solve(npv_equation, rate)




# calc = Calculator([100, 200, 300], [50, 100, 150], [0.1, 0.1, 0.1])
# calc1 = Calculator([100], [50], [0.1])
# print(calc.calc_NPV())
# print(calc.calc_IRR())