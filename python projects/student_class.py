class Student:
    def __init__(self, fname, lname, id, energy_level):
        self.fname=fname
        self.lname=lname
        self.id=id
        self.energy_level=energy_level
    
    def __str__(self):
        return self.fname + ' ' + self.lname + "'s id is " + self.id + ' and their energy level is ' + self.energy_level
    
    def greeting (fname):
        return 'Hello, ', fname
    
