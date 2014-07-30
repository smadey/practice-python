class SchoolMember:
    '''Represents any school member.'''
    def __init__(self, name, age):
        self.name = name
        self.age = age

        print('(Initialized SchoolMember: %s)' % self.name)

    def tell(self):
        '''Tell my details.'''
        print('Name: %s Age: %d' % (self.name, self.age), end = ' ')

class Teacher(SchoolMember):
    '''Represents a teacher.'''
    def __init__(self, name, age, salary):
        SchoolMember.__init__(self, name, age)
        self.salary = salary

        print('(Initialized Teacher: %s)' % self.name)

    def tell(self):
        SchoolMember.tell(self)
        print('Salary: %s' % self.salary)

class Student(SchoolMember):
    '''Represents a student.'''
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks

        print('(Initialized a student: %s)' % self.name)

    def tell(self):
        SchoolMember.tell(self)
        print('Marks: %s' % self.marks)

print()

t = Teacher('Mrs. Bob', 40, 30000)
s = Student('Smadey', 22, 75)

print()

members = [t, s]
for member in members:
    member.tell()
