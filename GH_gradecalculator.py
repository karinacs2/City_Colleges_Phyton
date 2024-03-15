#Input user
full_name = input("Students full name: ")
exam_score_1 = float(input("Exam score 1 (out of 100):" ))
exam_score_2 = float(input("Exam Score 2 (out of 100):" ))
exam_score_3 = float(input("Exam Score 3 (out of 100):" ))
attendance_percentage = float(input("Attendance Percentage (out of 100%): "))

#Values validation
if exam_score_1 < 0 or exam_score_2 < 0 or exam_score_3 < 0 or attendance_percentage < 0:
    print("Invalid value added, please return and check the data")
    exit()
if exam_score_1 > 100 or exam_score_2 > 100 or exam_score_3 > 100 or attendance_percentage > 100:
    print("Invalid value added, please return and check the data")
    exit()

#Avarage exam score
avarage_exam_score = float(exam_score_1 + exam_score_2 + exam_score_3) / 3

#Students initials 
initials = "".join([name[0].upper()for name in full_name.split()])

#Students second name  
second_name = full_name.split()[-1]

#Students overal grade 
if attendance_percentage < 75:
    print("Students overal grade: F")
elif avarage_exam_score >= 85: 
    print("Students overal grade: A")
elif avarage_exam_score >= 70:
    print("Students overal grade: B")
elif avarage_exam_score >= 55:
    print("Students overal grade: C")
elif avarage_exam_score >= 40:
    print("Students overal grade: D")
else:
    print("Students overal grade: F")

#Convert average exam score to GPA (rule of three)
score_GPA = float(avarage_exam_score*4)/100

#Results
print("Avarage Exam Score: ", avarage_exam_score)
print("The students initials: ", initials)
print("The students second name: ", second_name)
print("Student GPA:", score_GPA)