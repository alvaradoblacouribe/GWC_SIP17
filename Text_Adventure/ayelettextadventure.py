start = '''
You're walking down a street and you see an old man fall down. Do you go back to help or continue walking to get home as soon as possible?
'''


print(start)


print("Type 'left' to go back or type 'right' to continue walking.")
user_input = input()
if user_input == "left":
    print("You decided to go left and help the old man. You are a nice person!") # finished the story by writing what happens

elif user_input == "right":
    print("You decided to continue walking so that you'll get home quickly") # finished the story writing what happens

girl = "You continue your pathway home and you see a little girl being abused by a random person on the street. What will you do? Will you stop the person or just walk by "
print(girl)
print("Type 'left' to stop the person or type 'right' to continue walking")
user_input = input()
if user_input == "left":
    print("How brave of you! You decided to stop the man and you succeeded")
elif user_input == "right":
    print ("You decided to continue walking. Maybe next time you will be brave enough to stand up.")
print("You made it home on time!")
