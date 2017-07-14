start = '''
You walk into a party and you see a bunch of friends; You see your best friend with a group of girls on the right side of the room and the girls has asked you to drink.
There is also another group on the left side that your less familiar with but doesn't asking you to drink.
You start to feel uncomfortable.
You see your best friend making bad decision.
'''
part left = '''
You start to make a lot of friends and end up having such a good time. You leave the party
and a guy named tyler asked if you wanted a ride. you've seen him drinking.
'''
part right = ''' you start to feel uncomfortable, but your best friend tells you to stay. You leave the party
and a guy named tyler asked if you wanted a ride. you've seen him drinking.
'''



print(start)


print("Type 'left' to go left or 'right' to go right.")
user_input = input()
if user_input == "left":
    print("You choose to go left and they hand you a coca cola. You have a fun night, and end up making a lot of cool friends.") # finished the story by writing what happens

elif user_input == "right":
    print("You choose to go right with the party group, and they pressure you to have a beer. You end up getting caught and throwing up so much. You feel embarassed and ashamed of yourself. Always remember to never fall into peer pressure!") # finished the story writing what happens

print ("Type 'yes' to say yes or 'no' to say no.")
user_input = input(part left)
if user_input == "yes":
    print("You get in the car. You open your phone and see a lot of missed calls but your too drunk to call her back. You end up getting into a car accident. you wake up in the hospital with a few broken ribs. you could have died. Never fall for peer pressure!")

elif user_input == "no"
    print("")
