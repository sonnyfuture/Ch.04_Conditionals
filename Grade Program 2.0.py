current = int(input("Current Semester Grade: "))
final_exam = int(input("Final Exam Grade: "))
exam_weight = int(input("Final Exam Weight: "))

final_grade=(((100-exam_weight)*current+(exam_weight*final_exam))/100)
print (final_grade)

if final_grade >= 90:
    print ("A")

elif final_grade >= 80:
    print ("B")

elif final_grade >= 70:
    print ("C")

elif final_grade >= 60:
    print ("D")

else:
    print("F... Transfer to Johnston.")
