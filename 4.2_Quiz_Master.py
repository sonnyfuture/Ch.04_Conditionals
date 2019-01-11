'''
QUIZ MASTER PROJECT
-------------------
The criteria for the project are on the website. Make sure you test this quiz with 
two of your student colleagues before you run it by your instructor.
'''

question_1=int(input("What is 1+1? "))
if question_1 == 2:
    print ("Congrats on knowing basic math.")
else:
    print ("HOW COULD YOU EVEN MESS THAT UP?")

question_2=(input("Who is Naruto's son? "))
if question_2.lower() == "boruto":
    print ("You are a man of culture.")
else:
    print ("If you haven't seen Naruto you HAVE NOT LIVED.")

question_3=(input("What is the best Star Wars movie? A) Episode 4: A New Hope B) Episode 5: The Empire Strikes Back C) Episode 6: Return of the Jedi or D) Episode 8: The Last Jedi? "))
if question_3.lower() == "a":
    print ("Ehh, maybe.")
if question_3.lower() == "b":
    print ("Yeah, Probably.")
if question_3.lower() == "c":
    print ("Probably most definitely not.")
if question_3.lower() == "d":
    print ("Why do you feel this way? Get some help.")