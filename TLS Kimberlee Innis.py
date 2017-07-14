start= '''Hello, and welcome to Teenage Love Story.
You can play as any character you wish, make any choice you want and break a misconception made about being a teenager in love!'''

P = '''You decide to lay in bed and stay a few minutes on your phone,
you suddenly recieve a text from Bryce,
your acquaintance since freshman year turned into your favorite person,
the boyfriend that you are dearly in love with, who feels the same.
You reply and tell him goodmorning with corny nicknames and emojis, the morning routine for you two.'''

S = '''You look into the mirror, doing your daily routine of brushing your teeth and washing your face.
You hop into the shower when your water starts to emit mist. You wet your curly kinky hair. Once done you return to your room.
You see your small dog laying on your bed. Your phone lights up with a text from Bryce. He tells you good morning and you say it back.
Continuing the routine that you two haven't broken in a year almost two, cute and corny nicknames with a dash of emoji.'''

print(start)

print ('''You can play as Jay, a black teen from NYC.
Nia, a white teen from NJ.
or Leya, a latina teen from NYC.
Say the name to start the game!''')

user_input = input()

if user_input == "Jay":
    print("You wake up in your bed and you hear the train that is in sync with your alarm for the morning.")
    print('''Do you want to hop straight out of bed or do you want to scroll on your phone?
    P for phone and S for Straight outta bed.''')
    if user_input == "P":
        print(P)
    if user_input == "S":
        print(S)

if user_input == "Nia":
    print('''You wake up to the smell of pancakes, eggs and bacon.
Your mom calls you downstairs from the kitchen for breakfast''')

if user_input == "Leya":
    print("Your mom knocks on your room door to make sure you're up and getting ready for school")
