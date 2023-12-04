class Employee:
  def __init__(self, name, salary):
      self.name = name
      self.salary = salary

  def display_info(self):
      print(f"Name: {self.name}, Salary: ${self.salary}")


class Manager(Employee):
  def __init__(self, name, salary):
      super().__init__(name, salary)

  def long_term_bonus(self):
      return 0.4 * self.salary

if __name__ == "__main__":
  # Instantiate an Employee
  employee = Employee("John Doe", 50000)
  employee.display_info()

  # Instantiate a Manager
  manager = Manager("Jane Smith", 80000)
  manager.display_info()

  # Calculate and display the long-term bonus for the Manager
  manager_bonus = manager.long_term_bonus()
  print(f"{manager.name}'s Long-Term Bonus: ${manager_bonus}")

