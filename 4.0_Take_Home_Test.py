'''
HONOR CODE: I solemnly promise that while taking this test I will only use PyCharm or the Internet,
but I will definitely not ask another person except the instructor. Signed: Eddie H. Agic


  1. What is missing from this code?
     
     midichlorians = float(input("Enter midichlorian count: ")
     if midichlorians > 10000:
         print("You have serious Jedi potential")
     else:
         print("Jedi, you will never be.")
'''

midi=float(input("Enter midichlorian count: "))
if midi > 10000:
    print("You have serious Jedi potential.")
else:
    print("Jedi, you will never be.")

    #Add a parenthesis after the midichlorian count
     
'''
  2. This runs, but there is something wrong. What is it?
     
     user_input = input("R2D2 is a: ")
     print("A. Droid")
     print("B. Storm Trooper")
     if user_input.upper() == "A":
         print("Correct!")
     else:
         print("Incorrect.")
'''

print("A. Droid")
print("B. Storm Trooper")
user_input=input("R2D2 is a: ")
if user_input.upper() == "A":
    print("Correct!")
else:
    print("Incorrect.")

    #The answer options have to show up above the user input or else the person inputting won't know what to put.

'''
     
  3. There are two things wrong with this code that tests if x is set to a
     positive value. One prevents it from running, and the other is subtle.
     Make sure the if statement works no matter what x is set to.
     Identify both issues. 
     
     x == 4
     if x >= 0:
         print("x is positive.")
     else:
         print("x is not positive.")
 '''

x=float(input("Number: "))
if x > 0:
    print("x is positive.")
else:
    print("x is not positive.")

    #one equals sign and 0 is not a positive number so it should not be included.
 
'''
  4. What three things are wrong with the following code?
     
     x = input("Enter a number: ")
     if x = 3
         print("You entered 3")
 '''

 #1. It is not asking for an integer or a float, 2. Missing a colon after the if statement, 3. If statement should have two equals signs.
 
'''
  5. There are four things wrong with this code. Identify all four issues. 
     
     answer = input("What is the name of Poe Dameron's Droid? ")
     if a = "BB8":
         print("Correct!")
         else
         print("Incorrect! It is BB8.")
'''

answer = input("What is the name of Poe Dameron's Droid? ")
if answer == "BB8":
    print("Correct!")
else:
    print("Incorrect! It is BB8.")

#2 equal signs

'''
  6. This program doesn't work correctly. What is wrong?
     
     x = input("Who are the top 3 greatest Jedi?")
     if x == "Yoda" or "Luke Skywalker" or "Obi-Wan Kenobi":
         print("That is correct!")
'''

x = input("Who are the top 3 greatest Jedi?")
if x == "Yoda" or x=="Luke Skywalker" or x=="Obi-Wan Kenobi":
    print("That is correct!")
else:
    print("WRONG!")


#all three of the answers have to be == to x

'''
  7. Look at the code below. Write your best guess here on what it will print.
     Next, run the code and see if you are correct.
     Clearly label your guess and the actual answer.
     
     x = 5
     y = x == 6
     z = x == 5
     print("x=", x)
     print("y=", y)
     print("z=", z)
     if y:
         print("Star Wars Episodes 1,2,3 are the best!")
     if z:
         print("Star Wars Episodes 4,5,6 are the best!")
'''



x = 5
y = x == 6  # since x==6 is false this sets y to false
z = x == 5   #since x==5 is true this sets z to true.
print("x=", x)
print("y=", y)
print("z=", z)
if y:
    print("Star Wars Episodes 1,2,3 are the best!")
if z:
    print("Star Wars Episodes 4,5,6 are the best!")

#ANSWER: It outputs "Star Wars Episodes 4,5,6 are the best!"  This happens because the code is asking for y to be assigned to x which is equal to 6, but that is not true.  Meanwhile z IS true, so it outputs the second answer.


'''
 8. Look at the code below. Write you best guess on what it will print.
     Next, run the code and see if you are correct. 
     
     x = 5
     y = 10
     z = 10
     print(x < y)
     print(y < z)
     print(x == 5)
     print(not x == 5)
     print(x != 5)
     print(not x != 5)
     print(x == "5")
     print(5 == x + 0.00000000001)
     print(x == 5 and y == 10)
     print(x == 5 and y == 5)
     print(x == 5 or y == 5)
'''


x = 5 #yes
y = 10 #yes
z = 10 #yes
print(x < y) #true
print(y < z) #false
print(x == 5) #true
print(not x == 5) #false
print(x != 5) #false
print(not x != 5) #error..
print(x == "5") #false
print(5 == x + 0.000000) #true
print(x == 5 and y == 1) #false
print(x == 5 and y == 5) #false
print(x == 5 or y == 5) #true


#ANSWER: I got them all right except for not x != 5
'''
 9. Look at the code below. Write you best guess on what it will print.
     Next, run the code and see if you are correct. (HINT: when comparing strings, ASCII codes are used. https://www.ascii-code.com/)
     
     print("3" == "3")
     print(" 3" == "3")
     print(3 < 4)
     print("3" < "4")
     print("3" < 4)
     print("<" < ">")
     print((2 == 2) == "True")
     print((2 == 2) == True)
     print("?"<"!")
'''

#GUESS: It will say whether or not each statement is true or false and will check the strings using ASCII codes.

print("3" == "3") #True
print(" 3" == "3") #False
print(3 < 4) #True
print("3" < "4") #True
print("3" < 4) #Error...
print("<" < ">") #True
print((2 == 2) == "True") #False
print((2 == 2) == True) #True
print("?"<"!") #False

#ANSWER: 100% I'm a god



'''
 10. What things are wrong with this section of code?
     The programmer wants to set the force sensitivity variable according to the character the user selects.
     
     print("Welcome to the Jedi Academy!")

     print("A. Jedi Master")
     print("B. Sith Lord")
     print("C. Droid")

     user_input = input("Choose a character?")

     if user_input = A:
         money = 1000
     else if user_input = B:
         money = 900
     else if user_input = C:
         money = 0
'''

#Elif, should use .lower(), == not =, Should also be quotes around A, B, C

