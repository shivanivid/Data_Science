#Q1
#Employee class

from datetime import datetime


class Employee:
    def __init__(self):
        self.EmployeeID = None
        self.Gender = ""
        self.Salary = 0
        self.PerformanceRating = 0

    def get(self):
        print("\n--- Enter Employee Basic Details ---")
        self.EmployeeID = input("Enter Employee ID: ")
        self.Gender = input("Enter Gender: ")
        self.Salary = int(input("Enter Salary: "))
        self.PerformanceRating = int(input("Enter Performance Rating (1-5): "))

#JoiningDetail class

class JoiningDetail:
    def __init__(self):
        self.DateOfJoining = None

    def getDoJ(self):
        date_str = input("Enter Date of Joining (YYYY-MM-DD): ")
        # Converts the string input into a date object for sorting
        self.DateOfJoining = datetime.strptime(date_str, "%Y-%m-%d")

#Information Class

class Information(Employee, JoiningDetail):
    def __init__(self):
        Employee.__init__(self)
        JoiningDetail.__init__(self)

    def display(self):
        doj_str = self.DateOfJoining.strftime("%Y-%m-%d")
        print(f"ID: {self.EmployeeID} | Gender: {self.Gender} | Salary: {self.Salary} | "
              f"Rating: {self.PerformanceRating}/5 | Joined: {doj_str}")

def readData(employee_list):
    # Calculate top 3 based on Ratings (highest first)
    top_3 = sorted(employee_list, key=lambda x: x.PerformanceRating, reverse=True)[:3]
    
    # Sort these top 3 by Date of Joining (ascending)
    top_3_sorted = sorted(top_3, key=lambda x: x.DateOfJoining)
    
    print("\n--- Top 3 Employees (By Rating, Sorted by DOJ) ---")
    for emp in top_3_sorted:
        emp.display()

if __name__ == "__main__":
    employees = []
    num = int(input("How many employees to enter? "))
    
    for i in range(num):
        emp_obj = Information()
        emp_obj.get()
        emp_obj.getDoJ()
        employees.append(emp_obj)
    
    readData(employees)
    