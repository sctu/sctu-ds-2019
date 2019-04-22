
class Employee:
    "所有员工的基类"
empCount = 0
def init (self,name,salary):
    seif.name=name
    self.salary=salary
    
Employee.empCount+=1
def displayCount(self):
    print("Total Employee %d"%Employee.empCount)
def displayEmployee(self):
    print("name:",self.name,",Salary:",self.salary)