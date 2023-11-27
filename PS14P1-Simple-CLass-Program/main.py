class Employee:
  def __init__(self, name, salary):
      self.name = name
      self.salary = salary

  def calculate_bonus(self, bonus_rate):
      bonus = self.salary * bonus_rate
      return bonus

# Example usage of Employee class
employee1 = Employee("John Doe", 50000)
bonus_rate = 0.1  # You can change this rate as needed
bonus = employee1.calculate_bonus(bonus_rate)
print(f"{employee1.name}'s bonus is: ${bonus:.2f}")

class Student:
  def __init__(self, first_name, last_name, district_code, enrolled_credits):
      self.first_name = first_name
      self.last_name = last_name
      self.district_code = district_code
      self.enrolled_credits = enrolled_credits

  def compute_tuition_owed(self):
      if self.district_code == 'I':
          tuition_owed = self.enrolled_credits * 250.00
      else:
          tuition_owed = self.enrolled_credits * 500.00
      return tuition_owed

# Example usage of Student class
student1 = Student("Alice", "Smith", "I", 12)
tuition_owed = student1.compute_tuition_owed()
print(f"{student1.first_name} {student1.last_name} owes ${tuition_owed:.2f} in tuition.")
