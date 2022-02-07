class User():
  """User Class"""

  def __init__(self, name, address, psu_id):
    """Initialize Variables"""
    self.name = name
    self.address = address
    self.psu_id = psu_id

  
  def describe_user(self):
    """Method to describe user"""
    print(f"This user's name is {self.name}, their address is {self.address}, and their PSU id is {self.psu_id}.")
  