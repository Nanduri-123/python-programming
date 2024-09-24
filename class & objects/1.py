#Create a sample class named Employee with two attributes id and name
class Employee:
    def __init__(self, id, name):
        self.id = id
        self.name = name
    
    def delete_id(self):
        del self.id

emp = Employee(1, 'coder')

emp.delete_id()

has_id = hasattr(emp, 'id')

del emp

try:
    emp_exists = emp
except NameError:
    emp_exists = 'emp has to be deleted'

print({'has_id': has_id, 'emp_exists' : emp_exists})