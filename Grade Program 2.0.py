current = int(input("Current Semester Grade: "))
final_exam = int(input("Final Exam Grade: "))
exam_weight = int(input("Final Exam Weight: "))

final_grade=(((100-exam_weight)*current+(exam_weight*final_exam))/100)
print (final_grade)

if final_grade >= 90 and final_grade <= 100:
    print ("A")

if final_grade >= 80 and final_grade < 90:
    print ("B")

if final_grade >= 70 and final_grade < 80:
    print ("C")

if final_grade >= 60 and final_grade < 70:
    print ("D")

if final_grade >= 0 and final_grade < 60:
    print ("F... Transfer to Johnston")
