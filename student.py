from user import User

class Student(User):
  """Student Class"""

  def __init__(self, name, address, psu_id, major, school_year, advisor):
    super().__init__(name, address, psu_id)
    self.major = major
    self.school_year = school_year
    self.advisor = advisor
  
  def describe_user(self):
    print(f"This student's name is {self.name}, their address is {self.address}, their PSU id is {self.psu_id}, their major is {self.major}, they are a {self.school_year}, and their advisor is {self.advisor}.")


