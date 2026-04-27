# Create a program in python to demonstrate Polymorphism.
#1. Make use of private and protected members using python name mangling techniques.


class IITExam:
    def __init__(self, student_name, score):
        self._institute = "IIT Delhi"          # Protected member
        self.__base_cutoff = 75                # Private member (Name Mangling)
        self.student_name = student_name
        self.score = score

    def display_result(self):
        # Base method to be overridden
        pass

class Engineering(IITExam):
    def display_result(self):
        # Accessing protected member directly
        # Accessing private member using Name Mangling: _ClassName__variableName
        status = "Qualified" if self.score >= self._IITExam__base_cutoff else "Not Qualified"
        print(f"Student: {self.student_name} | Dept: Engineering | Institute: {self._institute}")
        print(f"Result: {status} (Cutoff: {self._IITExam__base_cutoff})")

class Architecture(IITExam):
    def display_result(self):
        # Architecture has a different interpretation of the same interface
        arch_cutoff = self._IITExam__base_cutoff - 5
        status = "Qualified" if self.score >= arch_cutoff else "Not Qualified"
        print(f"Student: {self.student_name} | Dept: Architecture | Institute: {self._institute}")
        print(f"Result: {status} (Specialized Cutoff: {arch_cutoff})")

# Demonstration of Polymorphism
results = [
    Engineering("Shivam", 82),
    Architecture("Nisha", 74)
]

for student in results:
    student.display_result()
    print("-" * 40)





