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
    print("You go left and you spot a spot a sliver of light peeking under a crack")
    print("in the wall. Do you go foward and inspect the cracks?")
    print("Type 'yes' or 'no'.")
    user_input = input()
    if user_input == "yes":
        print("You brush your fingers over the crack and the wall crumbles.")
        print("Blinding white light gapes from where the wall once was. You can't")
        print("see anything, but hear the walls crumbling around you.")
        print("Do you 'curl up into a ball' or 'walk forward'?")
        user_input= input()
        if user_input== "curl into a ball":
            print("Good job fam. As the walls crumble the debris buries you alive.")
            print("Fun! But you lost.")
            print("END GAME")
            user_input==input()
        if user_input== "walk forward":
            print("Your eyes are tearing and the ground feels shaky under you,")
            print("but you take a step foward. The floor collapses under you.")
            print("The drop is short and you land in a dark field. You see a")
            print("glowing white light approaching you.")
            print("You hear a murmuring sound and realize it's coming from the")
            print("white light. You make out a gravelly voice:")
            sys.stdout.isatty()
            def hilite(string, status, bold):
                attr = []
                if status:
                    # green
                    attr.append('32')
                else:
                    # red
                    attr.append('31')
                if bold:
                    attr.append('1')
                return '\x1b[%sm%s\x1b[0m' % (';'.join(attr), string)
            print("If a man carried my burden he would break his back. I am not")
            print("big but leave silver in my tracks.")
            print("What am I?")
            user_input = input()
            if user_input == "snail" or "Snail":
                def hilite(string, status, bold):
                    attr = []
                    if status:
                        # green
                        attr.append('32')
                    else:
                        # red
                        attr.append('31')
                    if bold:
                        attr.append('1')
                    return '\x1b[%sm%s\x1b[0m' % (';'.join(attr), string)
                print("...alright. ")
                print("The light turns off and you are greated by a giant slimy")
                print("snail hovering over you. Its red eyes gleam at you through")
                print("the dark. Challenge it to a battle? Type 'y' or 'n'")
                    user_input = input()
                    if user_input=="y":
                        print("You search your pockets for some sort of weapon")
                        print("You find a 'gum wrapper' and a 'pen'. Which one do you choose?")
                            user_input=input()
                            if user_input=="gum wrapper":
                                print("Honestly, what are you expecting? You are dead meat hon")
                                END GAME
                                exitonclick
                            if user_input=="pen"
                                print("Your hands are clammy and you have no idea how you're")
                                print("supposed to win this fight. You uncap the pen and almost")
                                print("slice yourself on the giant sword that materializes. The")
                                print("pen is gone, and in your hand is a jewel-encrusted base to")
                                print("a sword. Emblazoned across the base is the word 'Riptide'.")
                                
            else


                    if user_input=="n":
                        print("The snail eyes you hungrily and starts to close in")
                        print("on you. You sit there in shock as the snail crawls")
                        print("over you and eats you.")
                        END GAME
                        exitonclick


    elif user_input == "no":
        print("You continue down the brazier-lit corridor and feel the air get")
        print("danker--water drips down the walls and the ground gets mossier.")
        print("All of a sudden, the braziers go out. You feel your way along the")
        print("left side of the corridor until the wall ends.")
    # finished the story by writing what happens
elif user_input == "right":
    print("You choose to go right and fall into a giant hole in the ground.")
    print("Do you 'scream' or 'cry'?")
    user_input = input()
    if user_input == "scream":
        print("No one hears or cares about your screams. u ded bitch")
        END GAME
        exitonclick
    if user_input == "cry":
        print("Giant talons tug at the back of your shirt. You look up and see")
        print("a giant bird holding you and flying up out of the hole.")
        print("You soar up and up, past the entrance of the hole. You gape in awe")
        print("wreckage of the walls around you and barely notice when the bird")
        print("drops you. You land on a large brazier against the wall that has")
        print("a measly nest built into it. You hear feather rustling all around")
        print("you. You make out three baby chicks the size of cars circling around.")
        print("your heart skips a beat. They cry out and poke at with their sharp beaks.")
        print("Dinner has arrive! Hope you taste good!")
        END GAME
        exitonclick


 # finished the story writing what happens
elif user_input== " ":
    print("Congrats man! You do nothing but stand there and in the blink of an"
    print("eye you find yourseld back in your bed. No flesheating slugs or hungry")
    print("hawks for you!")
    END GAME
