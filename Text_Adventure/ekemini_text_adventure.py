start = '''
You wake up one morning and find that you aren't in your bed. You aren't even in your room.
You're in the middle of a giant maze.
A sign is hanging from the ivy: "You have one hour. Don't touch the walls."
There is a hallway to your right and to your left.
'''

light = '''
You have chosen the path of light.

The hallway widens as you walk further. Glowing fireflies appear one by one, illuminating the long stretch ahead. Eventually, you find yourself in a warm and open space. The roots of an ancient tree in the center curl outward in intricate patterns, stopping at your feet. A breeze passes through your hair. It shifts the leaves just enough to reveal a woman in a long, white gown.

"Can you help me?" she asks.
'''

darkness = '''
You have chosen the path of darkness.

As you walk down the hallway, you notice it getting tighter and tighter. You soon find yourself crawling on your hands and knees just to fit through the small space. Just when it feels like you're running out of air, you suddenly tumble down into a cramped chamber. The walls and floors are lined with wood, giving the room an "attic" kind of vibe. Sitting within arms reach is a man shrouded in a black cloth that reminds you of... curtains?

He glances up at you. "I have a job for you."
'''

print(start)

print("Choose 'left' or 'right'.")
user_input = input()
if user_input == "left":
    print(light)
    light_input = input("Say, 'Sure. How?' or 'No way!'. ")
elif user_input == "right":
    print(darkness)
    dark_input = input("Say 'What is it?' or 'Get me out of here!'. ")
else:
    print("That's not an option.")

powers = '''
She breathes a sigh of relief. "You made the right choice coming here. Before you, we had mortal protectors to guard this place from harm. But over the years, their powers proved to be no match for what we're up against. I am the last of the heroes, and I've become too weak. Now our world needs a new one."

Birds scatter from behind her as she overturns her palms towards you. In each lies a sphere of swirling colors.

"I won't make the same mistake as the ones who chose us. This time, I'll give you the strength we never had. I have two special abilities for you. Would you rather control the elements? Or be able to fly?"
'''

#uhhh i didn't finish, but the villain was going to give telekinesis or the power to manipulate others

fail1 = '''

'''

villain = '''

'''

fail2 = '''

'''


if light_input == "Sure. How?":
    print(powers)
    light_input = input("Your options are 'left palm' and 'right palm'. ")
elif light_input == "No way!":
    print(fail1)
else:
    print("That's not an option.")

if dark_input == "What is it?":
    print(villain)
    dark_input = input("Your options are '___' and '___'. ")
elif dark_input == "Get me out of here!":
    print(fail2)
else:
    print("That's not an option.")
