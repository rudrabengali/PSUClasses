from user import User
from student import Student
from faculty import Faculty

aFaculty = Faculty("Julia", "111 Sohun Road", "jto532", "Penn State Drive", "333-444-5555")

aStudent = Student("Rudra", "519 Shoemaker Drive", "rsb5526", "Computer Science", "Freshman", aFaculty.name)

Faculty.describe_user(aFaculty)
print("\n")
Student.describe_user(aStudent)