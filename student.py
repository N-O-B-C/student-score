"""
this creates students object.
"""
class Student:
    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender
        self.subjects = {}

    def enter_score(self):
        number_of_subjects = int(input(f"How many subjects do you want to offer {self.name} : "))

        for i in range(number_of_subjects):
            subject_name = input(f"\nEnter name of subject - {i+1}: ")
            number_of_scores = 5
            score_list = []

            for z in range(number_of_scores):
                score = int(input(f"Enter score {z+1} for {subject_name}: "))
                score_list.append(score)

            total = sum(score_list)
            score_list.append(total)


            self.subjects[subject_name] = score_list
            
        
    
