from compito6_2 import *

class Course:
    
    def __init__(self, name: str):
        
        self.name: str = name
        self.groups: list[Group] = []
        
    def register(self, student: Student) -> None:
        
        if student.group is not None:
            
            return
    
        for group in self.groups:
            
            if len(group.get_students()) < group.get_limit():
                
                group.add_student(student)
                break 
        
    def get_groups(self) -> list[Group]:
        
        return self.groups
        
    def add_group(self, group: Group) -> None:
        
        if group not in self.groups:
            
            self.groups.append(group)    