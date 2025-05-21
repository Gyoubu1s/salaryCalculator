import re

wage_input = (input("Enter your desired wage: (xx.xx for hourly or enter the full amount for yearly)"))


if re.fullmatch(r"\d+(\.\d{1,2})?", wage_input):
    wage = float(wage_input)
    if wage < 1000:
        weekly_wage = 40 * wage
        yearly_wage = weekly_wage * 52
        monthly_wage = yearly_wage / 12
        print(f"Your yearly is: ${yearly_wage:.2f}")
        print(f"Your monthly is ${monthly_wage:.2f}")
    else:
        yearly_wage = wage
        weekly_wage = yearly_wage / 52
        hourly_wage = weekly_wage / 40
        monthly_wage = yearly_wage /12
        print(f"Your hourly is ${hourly_wage:.2f}")
        print(f"Your monthly is ${monthly_wage:.2f}")
else:
    print("Check your value.")
