class Person:
    
    def __init__(self, cf: str, name: str, surname: str, age: int):

        self.cf: str = cf
        self.name: str = name
        self.surname: str = surname
        self.age: int = age
        
       
class Student(Person):
    
    def __init__(self, cf: str, name: str, surname: str, age: int, group = None):
        
        super().__init__(cf, name, surname, age)
        self.group: Group = group
        
    def set_group(self, group) -> None:
        
        self.group: Group = group
      
      
class Lecturer(Person):
    
    def __init__(self, cf: str, name: str, surname: str, age: int):
        
        super().__init__(cf, name, surname, age)
    
    
class Group:
    
    def __init__(self, name: str, limit: int):
        
        self.name: str = name
        self.limit: int = limit
        self.students: list[Student] = []
        self.lecturers: list[Lecturer] = []
        
    def get_name(self) -> str:
        
        return self.name
    
    def get_limit(self) -> int:
        
        return self.limit
    
    def get_students(self) -> list[Student]:
        
        return self.students
    
    def get_lecturers(self) -> list[Person]:
        
        return self.lecturers
    
    def get_limit_lecturers(self) -> int:
        
        if len(self.students) <= 10:
            
            return 1
        
        else:
            
            return len(self.students) // 10
            
    def add_student(self, student: Student) -> None:
        
        if student not in self.students and len(self.students) < self.limit:
            
            self.students.append(student)
            student.set_group(self)
            
    def add_lecturer(self, lecturer: Person) -> None:
        
        if lecturer not in self.lecturers and len(self.lecturers) < self.get_limit_lecturers():
            
            self.lecturers.append(lecturer)