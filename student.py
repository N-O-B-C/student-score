"""
This creates a student object.
"""

class Student:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        self.subjects = {}
        
        
    def enter_score(self):
        
        number_of_subjects = int(input(f"\nHow many subjects do you want to register for {self.name}? "))
        
        for i in range(number_of_subjects):
            subject_name = input(f"\nEnter name of subject - {i+1}: ")
            subject_score = int(input(f"Enter score for {subject_name}: "))
            total = sum(subject_score)
            self.subjects[subject_name] = subject_score 
        print(total)
