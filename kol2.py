# Class diary  
#
# Create program for handling lesson scores.
# Use python to handle student (highscool) class scores, and attendance.
# Make it possible to:
# - Get students total average score (average across classes)
# - get students average score in class
# - hold students name and surname
# - Count total attendance of student
# The default interface for interaction should be python interpreter.
# Please, use your imagination and create more functionalities. 
# Your project should be able to handle entire school.
# If you have enough courage and time, try storing (reading/writing) 
# data in text files (YAML, JSON).
# If you have even more courage, try implementing user interface.


class Student(object):
	average = 0
	name = ""
	surname = ""
	hclass = ""

	def __init__(self, name, surname, average, hclass):
		self.average = average
		self.name = name
		self.surname = surname
		self.hclass = hclass
		self.hclass.add_student(self)

#holds a number of hclasses. hclass can be added
class Highschool(object):
	nstudents = 0
	nclasses = 0
	classes = []

	def __init__(self):
		self.nstudents = 0
		self.nclasses = 0
		self.classes = []

	def add_class(self, hclass):
		self.classes.append(hclass)
		self.nclasses = self.nclasses+1
		self.nstudents = self.nstudents+hclass.nstudents	

#	def calculate_schoolaverage(self):
		 

#holds a number of students that can be added or removed
class Hclass(object):
	nstudents = 0
	students = []
	school = ""

	def __init__(self, school):
		self.nstudents = 0
		self.students = []
		self.school = school
		self.school.add_class(self)

	def add_student(self, student):
		self.nstudents = self.nstudents+1
		self.students.append(student)
		student.hclass = self
		self.school.nstudents = self.school.nstudents+1

#to do: only whole number of average can be printed, modify for decimal
	def calculate_studentaverage(self):
		average = 0
		for student in self.students:
			average = average+student.average
		average = average/self.nstudents
		return average

myschool = Highschool()
myclass = Hclass(myschool)
print "number of students before: " + str(myschool.nstudents)
student1 = Student("Jan", "Kowalski", 3, myclass)
student2 = Student("Anna", "Kowalski", 4, myclass)
average = myclass.calculate_studentaverage()
print "The classes average is: " + str(average)
print "number of students after: " + str(myschool.nstudents)		
	
