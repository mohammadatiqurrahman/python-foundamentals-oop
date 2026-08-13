class Employee:
    def __init__(self, name, hourly_wage):
        self.name = name
        self.hourly_wage = hourly_wage

yuki = Employee("Yuki", 1500)
kenta = Employee("Kenta", 1550)

print(f"Name: {yuki.name}, Hourly Wage: {yuki.hourly_wage}")
print(f"Name: {kenta.name}, Hourly Wage: {kenta.hourly_wage}")