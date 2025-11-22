class Student():
    
    def __init__(self, name: str, studyProgram: str, age: int, gender: str):
        
        self.name = name
        self.studyProgram = studyProgram
        self.age = age
        self.gender = gender
    
    def printInfo(self):
        
        print(f"Nome: {self.name}\nProgramma: {self.studyProgram}\nEtà: {self.age}\nGenere: {self.gender}\n")
    

student1 = Student("Alice", "Ingegneria Informatica", 18, "Femmina")
student1.printInfo()

student2 = Student("Bob", "Medicina", 19, "Maschio")
student2.printInfo()

student3 = Student("Charlie", "Economia", 20, "Maschio")
student3.printInfo()