from user import User


class Faculty(User):
  """Faculty Class"""

  def __init__(self,name, address, psu_id, office_address, office_phone):
    """Initializing Variables"""
    super().__init__(name, address, psu_id)
    self.office_address = office_address
    self.office_phone = office_phone
  
  def describe_user(self):
    """Method describing faculty member"""
    print(f"This faculty's name is {self.name}, their address is {self.address}, their PSU id is {self.psu_id}, their office address is {self.office_address}, and their phone extension is {self.office_phone}.")

diff --git a/student.py b/student.py
