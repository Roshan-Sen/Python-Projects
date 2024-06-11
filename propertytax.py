starting_year = 2023 #starting year
time = 15 #years to print property tax rate
tax_rate = 2 #property tax rate in percent
initial_home_value = 100000 #initial home value
home_value_increment = 2 #rate at which property value increases in percent

def display_entry(year, assessed_value, property_tax):
    print(f'{year},{assessed_value:.2f},{property_tax:.2f}')

if __name__ == '__main__':
    print(f'Home Value Appreciation Rate: {home_value_increment:.4f}%')
    print(f'Property Tax Rate: {tax_rate:.4f}%\n')
    print("Year,AV,PT")#year, assessed value, property tax
    running_home_value = initial_home_value
    current_year = starting_year
    for i in range(time + 1):
        display_entry(current_year, running_home_value, tax_rate / 100 * running_home_value)
        current_year += 1
        running_home_value = running_home_value * (1 + home_value_increment / 100)