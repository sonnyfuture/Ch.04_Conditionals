'''
QUIZ MASTER PROJECT
-------------------
The criteria for the project are on the website. Make sure you test this quiz with 
two of your student colleagues before you run it by your instructor.
'''



score = 0
total = 0

question_1=(input("What is 1+1? "))
total+=1
if question_1 == "2":
    print ("Congrats on knowing basic math.")
    score+=1
else:
    print ("HOW COULD YOU EVEN MESS THAT UP?")

question_2=(input("Who is Naruto's son? "))
total+=1
if question_2.lower() == "boruto":
    print ("You are a man of culture.")
    score += 1
else:
    print ("If you haven't seen Naruto you HAVE NOT LIVED. The correct answer is Boruto.")

question_3=(input("What is the best Star Wars movie? A) Episode 4: A New Hope B) Episode 5: The Empire Strikes Back C) Episode 6: Return of the Jedi or D) Episode 8: The Last Jedi? "))
total+=1
if question_3.lower() == "a":
    print ("Ehh, maybe. A better answer would be The Empire Strikes Back.")
elif question_3.lower() == "b":
    print ("Yeah, Probably.")
    score += 1
elif question_3.lower() == "c":
    print ("Probably most definitely not. A better answer would be The Empire Strikes Back.")
elif question_3.lower() == "d":
    print ("Why do you feel this way? Get some help. A better answer would be The Empire Strikes Back.")

question_4=(input("What is the name of the most common commercially sold banana? "))
total+=1
if question_4.lower()=="cavendish":
    print("You is banana god.")
    score+=1
else:
    print("No. It is a Cavendish.")

question_5=(input("How long was the longest government shutdown? "))
total+=1
if question_5=="35":
    print("You are a god of government.")
    score+=1
else:
    print("TAKE GOV (the correct answer is 35)!!!!!!!!!!!")

print((score/total)*100,"% Correct")


