"""Send passing students info to companies."""
# By Kamran Bigdely Nov. 2020
# Replace temp variable with query

class Employer:
    """sends graduates information to employer"""
    def __init__(self, name):
        self.name = name

    def some_func(self, students):
        """serves to  pass pylint"""
        self.send(students)

    def send(self, passed):
        """sends contact info"""
        print(passed + "contact info were sent to", self.name + '.')


class Student:
    """collects students gpa"""
    def __init__(self, gpa, name):
        self.gpa = gpa
        self.name = name

    def get_gpa(self):
        """returns gpa"""
        return self.gpa

    def send_congrat_email(self):
        """prints congrats email"""
        print("Congrats", self.name + ". You graduated successfully!")


class School:
    """process graduates"""
    def __init__(self, students) -> None:
        self.students = students
        self.passed_students = []
        self.top_10_percent = []

    def passing_list(self):
        """collects passing students returns array"""
        min_gpa = 2.5 # minimum acceptable GPA
        for student in self.students:
            if student.get_gpa() > min_gpa:
                self.passed_students.append(student)

    def pass_print(self):
        """print student's name who graduated"""
        print('*** Student who graduated *** ')
        for passed in self.passed_students:
            print(passed.name)
        print('****************************')

    def congrats(self):
        """sends congrats emails to each student"""
        for passed in self.passed_students:
            passed.send_congrat_email()

    def get_top_10_percent(self):
        """calculates top 10% of students"""
        self.passed_students.sort(key=lambda s: s.get_gpa())
        percentile = 0.9
        index = int(percentile * len(self.passed_students))
        self.top_10_percent = self.passed_students[index:]

    def send_contacts(self):
        """sends top 10% contacts to large companies"""
        self.get_top_10_percent()
        micro = Employer('Microsoft')
        fsf = Employer('Free Software Foundation')
        google = Employer('Google')
        top_employers = [micro, fsf, google]
        for employer in top_employers:
            employer.some_func(self.top_10_percent)

    def process_graduation(self):
        """runs methods to determine what messages to send out"""
        self.passing_list()
        self.pass_print()
        self.congrats()
        self.send_contacts()



STUDENTS = [Student(2.1, 'Donald'), Student(2.3, 'William'), Student(2.7, 'Toro'),
            Student(3.9, 'Lily'), Student(3.2,'Kami'), Student(3,'Sarah')]
school  = School(STUDENTS)
school.process_graduation()
