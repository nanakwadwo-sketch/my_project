import uuid
import csv

# with open ("proposal.txt", mode ="r") as file:
#     content = file.read()
#     print(content)

# with open ("patient.json", mode ="w") as file:
#     content =file.write("name: Richard Osei, age: 15, hometown: Abetifi")
#     print(content)

# with open ("patient.json", mode ="r") as file:
#     content=file.read()
#     print(content)

# class Patient:
    
#     def __init__(self, first_name, last_name, age, phone_number):
#         self.first_name = first_name
#         self.last_name = last_name
#         self.age = age
#         self.phone_number = phone_number
    
#     def getPatientInfo(self):
#         return f"First Name: {self.first_name}, Last Name: {self.last_name}, Age: {self.age}, Phone Number: {self.phone_number}"
    
#     def to_dict(self):
#         return {
#             "First Name": self.first_name,
#             "Last Name": self.last_name,
#             "Age": self.age,
#             "Phone": self.phone_number
#         }
    
#     @staticmethod
#     def capture_patient():
#         first_name = input("Enter your first name: ")
#         last_name = input("Enter your last name: ")

#         while True:
#             try:
#                 age = int(input("Enter your age: "))
#                 if age < 0:
#                     raise ValueError("Age cannot be negative.")
#                 break
#             except ValueError:
#                 print("Please enter a valid positive number for age.")

#         phone_number = input("Enter your phone number: ")
#         return Patient(first_name, last_name, age, phone_number)


# # List to store patient objects
# patients = []

# #captured patient is added to the empty list as a dictionary
# patient = Patient.capture_patient()  
# patients.append(patient)

# # Display patient details
# print("\nPatient Details")

# print("********************")
# for patient in patients:
#     print(patient.to_dict())



class Student:
    def __init__(self, first_name: str, last_name: str, age: int, student_id: int, grade_level:str):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.student_id = student_id
        self.grade_level = grade_level
# a function to display student information
    def get_student_details(self):
        return f"Name: {self.first_name} {self.last_name}, Age: {self.age}, id: {self.student_id}, grade: {self.grade_level}"
#a fucntion to get user input and validate some of the inputs
    @staticmethod
    def register_student():
        first_name: str = input("Enter your first name: ")
        last_name: str = input("Enter your last name: ")
        while True: 
            try:
                age = int(input("enter your age: "))
                if age < 0:
                    raise ValueError
                break
            except ValueError:
             print("Please enter a valid positive number for age.")

        grade_level = input("enter grade level: ")
#auto generate the student id and slice it to a shorhand id (8digits)
        student_id = str(uuid.uuid4())[:8]
        return Student(first_name, last_name, age, student_id, grade_level)

# a function to run the system depending on the user choice
def main():
    students =[]
    while True:
        print("\n1. Register Student")
        print("2. Display Student Details")
        print("3. save student info in csv")
        print("4. exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            student =Student.register_student()
            students.append(student)
            print("Student registered successfully!")
        elif choice == "2":
            for student in students:
                print(student.get_student_details())
        elif choice == "3":
            with open('students.csv', mode='w', newline='') as file:
                fieldnames = ['first_name', 'last_name', 'age', 'student_id', 'grade_level']
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                writer.writeheader()
                for student in students:
                    writer.writerow({'first_name': student.first_name, 'last_name': student.last_name, 'age': student.age, 'student_id':student.student_id, 'grade_level': student.grade_level})
                    print("Student info saved in csv file!")
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please choose a valid option.")







if __name__ =='__main__':
  main()

       



