from employees import Employee

#inheritance is used for code reusability

class Manager(Employee):
  def __init__(self, name, salary, department):
    super().__init__(name, salary)
    self.department = department

  def show_details(self):
    super().show_details()
    print(f"Department: {self.department}")

  def calculate_bonus(self):
    return self.salary * 0.10
