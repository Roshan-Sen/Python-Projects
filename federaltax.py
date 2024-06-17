#Federal tax calculator
import sys
import argparse

#Setup argument parser
parser = argparse.ArgumentParser(description = 'Calculates total federal income tax given an inputted income')
#Arguments
parser.add_argument('earned_income', type = float, metavar = '<float>', help='Input income, default = 100000')
#Finalize
arg = parser.parse_args()

class Tax_Bracket:
    def __init__(self, rate, low, high):
        self.tax_rate = rate #tax rate in decimal value
        self.min = low #low end of income taxed at the bracket
        self.max = high #high end of income taxed at the bracket
    def calculate_tax(self, income): #income is the total taxable federal income
        if income <= self.min:
            return 0
        return min(self.tax_rate * (self.max - self.min), self.tax_rate * (income - self.min))

if __name__ == '__main__':
    if len(sys.argv) != 2:
        sys.exit()
    earned_income = (float) (sys.argv[1])
    all_brackets = [Tax_Bracket(0.1, 0.0, 11000.00), Tax_Bracket(0.12, 11000.00, 44725.00), Tax_Bracket(0.22, 44725.00, 95375.00), Tax_Bracket(0.24, 95375.00, 182100.00), Tax_Bracket(0.32, 182100.00, 231250.00), Tax_Bracket(0.35, 231251.00, 578125.00), Tax_Bracket(0.37, 578126.00, sys.float_info.max)]
    total_tax = 0
    for bracket in all_brackets:
        temp = bracket.calculate_tax(earned_income)
        if temp == 0:
            break
        else:
            total_tax += temp
    print(f'Total Income Tax Payment: ${total_tax:.2f}')
    percentage = total_tax / earned_income * 100
    print(f'This is {percentage:.2f}% of your income of ${earned_income:.2f}')
