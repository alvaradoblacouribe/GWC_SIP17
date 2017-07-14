start = '''
You are a 18 year old escaping Syria and on your way to Turkey. In the hopes of starting a new life.
Your family is hoping that you will be out of danger and successful in Turkey, so one day you can help them.
In order to get to Turkey you need to travel miles by foot to get to the boat dock that will take you to Turkey.
In order to leave you need to pay a smuggler $950 to transport you to the boat dock.
To raise this money you can do option 1 which is steal money from your neighbor or option 2 which is to work 18 hours a day for two weeks.
'''


print(start)


print("Type 'option 1' to steal money or 'option 2' to go wait two weeks more.")
user_input = input()
if user_input == "option 1":
    print("You decide to steal money and you get caught and get beaten to death.")

elif user_input == "option 2":
    start2 = '''You wait two more weeks and you have enough money to pay the smuggler and start your journey to Turkey.
    On the journey you come across a starving family that would really apprecite your loaf of bread which is also your food ration for a day.
    You can give your loaf of bread to the family which is option 1 or keep the bread for yourself which is option 2. Which
    option do you pick? '''
    print (start2)

    print("Do you choose option 1 or option 2? ")
    user_input = input()
if user_input == "option 1":
    bread = ''' You starved yourself for a day, but you have safely made it to the dock where a boat is waiting for refugees.'''
    print(bread)
    starve = ''' You are now on a boat that will take you to Turkey. A couple of hours into the ride
        the ship is about to sink. There is a little girl next to you who cannot find her parents and is in need
        of a life jacket. You can try to swim but the storm is ruthless. Option 1 is to first put your lifejacket on the little girl and you have to try to swim.
        Option 2 is to put the lifejacket on yourself and leave the little girl to fend for herself.'''
    print(starve)

    print("Do you keep the lifejacket (if you're are type keep, if you're giving it to the little girl type give?")
    user_input = input()
if user_input == "give":
                hea= ''' Miraculosly you and the little girl both survive and make it to Turkey.'''
                print(hea)

elif user_input == "keep":
                khea= '''You survive but have to live with the guilt of letting a little girl drown.'''
                print(khea)


elif user_input == "option 2":
    eat = ''' You have filled your stomach, but unfortunately militant truck finds the van kills all passengers'''
    print(eat)



# finished the story writing what happens
