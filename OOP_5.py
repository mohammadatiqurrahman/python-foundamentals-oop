class Employee:
    def __init__(self, name, hours_worked_list):
        self.name = name
        self.hours_worked_list = hours_worked_list

    def get_total_hours(self):
        total_hours = sum(self.hours_worked_list)
        print(f"{self.name} worked a total of {total_hours} hours.")

employee1 = Employee("Yuki", [8, 7, 9, 8, 6])
employee2 = Employee("Kenta", [8, 8, 8, 8, 8])
employee3 = Employee("Aiko", [6, 7, 8, 7, 6])
employee4 = Employee("Haruto", [9, 8, 10, 7, 8])

employee1.get_total_hours()
employee2.get_total_hours()
employee3.get_total_hours()
employee4.get_total_hours()