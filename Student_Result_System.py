name = input("Student name: ")
subjects =[]
no_of_subjects = int(input("Number of subjects: "))
while no_of_subjects >5 or no_of_subjects < 1:
    print("Invalid")
    no_of_subjects = int(input("Number of subjects: "))
for i in range(no_of_subjects):
    subjects_offering = input("What are the subjects you are offering: ")
    subjects.append(subjects_offering)
scores = []
for i in range(no_of_subjects):
    score = float(input( subjects[i] + " score: "))
    while score > 100 or score < 0:
        print("Invalid score: enter a number between 0 and 100")
        score = float(input( subjects[i] + " score: "))
    scores.append(score)
total = sum(scores)
average = total / no_of_subjects
print("STUDENT RESULT SYSTEM")
print(name)
for i in range(no_of_subjects):
    print(subjects[i] , " score: " , scores[i])
print(f"Total score: {total}")
print(f"Average score: {average}")
if average < 50:
    print("Grade: C")
elif average <= 70:
    print("Grade: B")
else:
    print("Grade: A")