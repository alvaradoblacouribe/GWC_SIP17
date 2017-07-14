start = '''
You wake up one morning and find that you aren't in your bed; you aren't even in your room.
You're in the middle of a giant maze.
A sign is hanging from the ivy: "You have one hour. Don't touch the walls."
There is a hallway to your right and to your left.
'''


print(start)

print("Type 'left' to go left or 'right' to go right.")
user_input = input()

if user_input == "left":
    print("You decide to go left and the walls of the maze start to close in and come dangerously close to touching you.  Do you run or touch the walls?")
    if input() == "touch the walls":
        print("The ivy on the walls of the maze start to reach out and grab you.  You are restrained and unable to move.  A person comes up to you and cuts the vines so that you are freed.  They offer you to lead you out of the maze.  Do you follow them?")
        if input() == "Yes":
            print("The two of you continue through the maze and eventually find an exit.  Your companion seems to be experienced in getting through the maze and finding the exit.  You inquire as to if they've ever been to the maze and they answer that they are tasked with leading people out of the maze yet no one trusts them when they offer help.  With help, you succesfully find the exit.  You win the game.")
        elif input() == "No":
            print("You continue to go through the maze alone.  You unknowingly walk deeper and deeper into the maze and your one hour ends.  Game Over.")

    elif input() == "run":
        print("As you run the walls come closer at a faster pace.  You are unable to outrun them and are consumed by the walls.  Game Over.")

elif user_input == "right":
    print("You choose to go right and come to a crossroad where there ae two signs, one pointing to the left and one pointing to the right.  Both of the signs say exit.  Which direction do you choose?")
    if input() == "left":
        print("You come upon a sphinx who gives a riddle.  You must correctly answer the riddle to continue on the road and you cannot go back.  You also get a clue from the spinx about how to get out if you answer correctly.   The riddle is: What has a tongue, cannot walk, but gets around a lot? ")
        if input() == "shoe":
            print("Correct.  You now are able to pass the sphinx.  The clue the sphinx tells you is to follow the eerie green light that glows in the dark night sky.  You are skeptical to follow the light but do it anyway.  The sphinx was telling the truth and by following the light you find the exit.  You win the game.")
        else:
            print("Incorrect. The sphinx attacks you.  Game Over.")


    elif input() == "right":
        print("You reach a clearing in the maze where a house stands.  The lights are on in the house so it appears that someone or something is in the house.  Do you go inside the house or attempt to walk around it?  Type inside or walk aorund.")
