start = '''
You are getting ready to leave work one day and everything is normal, you had a good day and
your ready to just go home and watch some netflix in your favoriate pajamamas with a
large bowl of ice cream.Your co-worker offers you a ride home but you decline because
excersize is good. After exiting the building you must decide if you are taking your usual
route through the alley with alot of foot traffic (left) or a different through the empty
highway (right)
'''

print(start)


print("Type 'left' to go left or 'right' to go right.")
user_input = input()
if user_input == "left":
    print("You decide to go left and go about minding your business in the alley until you feel an intense stare on the back of your head.You must make the decision to walk faster and call a friend or ignore it because it's probably nothing. ")
    print("Type 'ignore' to ignore it or 'speed up' to walk faster and contact a friend.")
    user_input = input()
    if user_input == 'ignore':
            print("Your friend is on their way to pick you up, but it should take up to 10 minutes. The person is approaching you from behind, but you have your trusty taser from your Dad. As the approacher comes closer you see that he is a middle aged man in his late 30's in a large hoodie and ripped jeans. He begins to follow behind you very closely and the people around you don't seem to notice.He is so close that his breath causes goosebumps to run down your back. You pull out the taser and tase him until he falls to the ground.Do you stay and wait for the police to arrive or run to the meeting place.")
            print("Type 'stay' to wait for the police or 'leave' to meet your friend.")
            user_input = input()
            if user_input == 'leave':
                print("Congrats you made it to your friends safely even though you will have to make a police statement tommorow your safe and you escaped a very frightening situation")
            if user_input == 'stay':
                print("Your attacker wakes up and you are unable to escape this time. You go unconscious and are never seen by your family again.")
            if user_input == 'speed up':
                print("You begin to speed up and although his legs are longer than yours you seem to have lost him in the crowd.Good decision you say in relief as you reach your apartment but you should take a different route tommorow just in case.")
elif user_input == "right":
    print("You choose to walk on the highway and you encounter a large group of guys all of them seemingly drunk. Do you turn around to avoid the encounter or continue walking because you don't think they will do anything?")
    print("Type 'continue' to continue on this pass or 'go back' to return to the building.")
    user_input = input()
    if user_input == 'continue':
        print("You disapper that day only to be found dead in the woods a month a later. A tragic occurance tha could have been avoided make the right decisions to prolong your life. Women are the victims of sexual harassment all the time and they always occur from a bad decision")
    if user_input == 'go back':
        print(" You turn back to walk back to your work place. As you turn the corner you still hear the foot steps of the men and try to speed up.They call out to you and one grabs your arm to stop you, Do your spray him or scream bloody murder until someone finds you? ")
        print("Type 'scream' to alert someone about your desperate situation or 'spray' to attack your pursuer")
        user_input = input()
        if user_input == 'scream':
            print("He covers your mouth with his large hand, you bite down hard on his finger as his friends laugh at his shout. You don't wait to see what happens next instead you run as fast as you can to your office building fumbling with the key until the door opens. You hear them outside your building but the door is locked. Your only option is to wait until morning when there are more people coming in from work. You'll look absolutely horrific with your bed head but at least you'll make it home alive.")
        if user_input == 'spray':
            print("Your pepper spray does its job on the first guy but the others respond to his yell that was painstakingly loud. You have no more pepper spray, will this be your last night? Maybe, but as you continue to run you realize that you lent your key to the building to your coworker who was working late. As you bend the corner to your building you see said co-worker locking up the doors for the night.You begin to yell his name but he still has his headphones on and can't seem to see you. You are left without options as he drives away without looking back. Your cornered by your pursuers and are unable to escape. Your left next to garbage that night and found unmoving the next morning.Your family is devastated and can't cope in the same house so they move away after the funeral.While there is an ongoing investagation to fing the guys that were responsible.")
