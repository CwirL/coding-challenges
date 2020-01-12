class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    def __init__(self, firstname, lastname, idNumber, scores):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber
        self.scores = scores

    def grading(self, a):
        if (a<=100 and a>=90):  
            return 'O'
        if (a<90 and a>=80):
            return 'E'
        if (a<80 and a>=70):
            return 'A'
        if (a<70 and a>=55):
            return 'P'
        if (a<55 and a>=40):
            return 'D'
        if (a<40):
            return 'T'

    def calculate(self):
        sum = 0
        for score in self.scores:
            sum += score
        average = sum/len(self.scores)
        grade = self.grading(average)
        return grade

    


file = open('./data.txt', 'r')
fileLines = file.read().split("\n")
line = fileLines[0].split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = fileLines[1]
scores = list( map(int, fileLines[2].split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())