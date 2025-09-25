from employees import Employee

class Developer(Employee):
  def __init__(self, name, salary, language):
    super().__init__(name, salary)
    self.language = language


    def show_details(self):
      super().show_details()
    print(f"Language: {self.language}")


    def calculate_bonus(self):
      return self.salary * 0.08