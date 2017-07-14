start = '''
During lunch one day you see a Pewdiepie lookalike from across the cafeteria talking to a girl. Do you approach the lookalike to tell him he looks like Pewds?

'''


print(start)


print("Type 'Y' to go up to them or 'N' to leave.")
user_input = input()
if user_input == "Y":
    print("He told you to go away. You were rude to interrupt the lookalike and you lost your chance :( .)") # finished the story by writing what happens
    exit()
elif user_input == "N":
    print("You made the polite choice. Yo mama taught you right.")
    print("continue")

firststep = '''
 You see him again! But this time, he's alone. What do you do?
 '''
print(firststep)
print ("Type 'Go' to go up to Pewds or 'Leave' to give up.")
user_input = input()
if user_input == "Go":
    print("He wants to talk to you and chat 😎 .")

elif user_input == "Leave":
    print ("You lost your chance. Leave your dignity in the cafeteria. ")
    exit()
print ("continue")

secondstep = ''' There's an awkward silence. Do you get awkward and walk away or do you fill the silence and continue talking? '''
print(secondstep)
print ("Type 'Walk' to walk away or 'Fill' to fill the silence.")
user_input = input()
if user_input == "Walk":
    print("You walked away from Pewds and lost all your chances. Good job. You have regerts for the rest of your life.")
    exit()

elif user_input == "Fill":
    print ("Pewds is impressed with your confidence and respects you.")

print("continue")

thirdstep= '''You have the idea to take a selfus. Do you ask for it?'''
print(thirdstep)
print("Type 'Pic' to take a selfus or 'No Pic' to not take a selfus")
user_input = input()
if user_input == "Pic":
    print("CONGRATS YOU HAVE NO RAGRETS!! Keep living your life by #yolo 😎")
elif user_input == "No Pic":
    print("You regretted this decision for the rest of your life. Go home and stay home.")
    exit()
