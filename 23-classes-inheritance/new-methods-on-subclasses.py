class Employee():
    def do_work(self):
        print("Im working")
        
class Manager(Employee):
    def waste_time(self):
        print("Wow, this YouTube video is fun!")
        
class Director(Manager):
    def fire_employee(self):
        print("You are fired!")
        
e = Employee()
m = Manager()
d = Director()

e.do_work()
# e.waste_time() # AttributeError: 'Employee' object has no attribute 'waste_time'

m.do_work()
m.waste_time()
# m.fire_employee()

d.do_work()
d.waste_time()
d.fire_employee()