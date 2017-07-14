start = '''
Welcome to "Them," a life sim with choices.
You will play through two days of a life- whether they're eventful is up to you!
I encourage you to replay this and try different combinations and choices for different outcomes.
In any case,
'''


print(start)


print("Who will you be this time, a boy or a girl?")
you = input()
#print("What will your name be?")
#name= input()
#print=("What a beautiful name! Let us begin.")
print=("Alright, let us begin.")
print=("It's a warm summer morning. You've woken up and found that you have nothing to do at all- you're free all day!")
print=("You decide to take advantage of your free time and enjoy the lovely weather; you're gonna go for a walk. ")
print=("You leave home and walk to the intersection by your apartment, intending to go to your favorite park, but the road is blocked for city work. Seems like you'll have to explore instead.")
print=("Will you go right or left?")
location = input()

if location == "right" :
    print=("You decide to go right. You walk for quite a while, taking stock of interesting stores to visit on another day, but though the weather was pleasant earlier it's starting to get hotter.")
    print=("You're getting tired and thirsty, but you don't want to walk all the way home for a drink. Luckily, you spot a quaint little cafe across the street- you can get something there!")
    print=("You push open the wooden doors, noting the unique doorknob. There's ac inside (thankfully) and it's not too full. It feels comfortable, for some reason. You decide to stay for a while.")
    print=("As you walk up to the counter to choose your drink, you notice one of the two baristas working the cappuccino machine. While you're perplexed by the fact that anyone would get a hot drink on a day like today, you barely spare the peculiar order a thought...")
    print=("Instead, you're captivated by the barista cradling the cup as they cap it... They're...")
    print=("(...What are they? (boy or girl))")
    them = input()

    if them == "boy":
        print=("...They're the most beautiful boy you've ever seen.")
        print=("You try not to be That Creepy Customer but you can't stop staring. Eventually he wraps up the order and turns to face you, catching you off guard. You're next in line and haven't even picked a drink!")
        print=("He doesn't notice your staring and instead smiles brightly at you, cheerily saying 'Welcome to Jimmy's Java! What would you like today?'")
        print=("You haven't even glanced at the menu yet, so you say the first thing that comes to mind. 'I actually don't know... I just want something sweet and cold. What would you recommend?'")
        print=("The barista grins again, and lists a few things on the menu. When he's done, he says 'My personal favorite is the chai, though. So, which do you want?' and awaits your response.")
        print=("You decide you trust his judgement and order an iced chai. You don't admit to yourself that maybe it's because you want to impress him, or maybe make him like you...? Argh.")
        print=("Turns out it worked though. As he passes you your cup, he whispers that he's glad you listened to him. Most people make fun of him for liking chai's, stating that they're 'girly,' and he's relieved you didn't. He thinks you're quite cute- it'd suck if you turned out to be rude!")
        print=("You're shocked by his direct admission of his attraction to you, and barely register his face falling as he apologizes for making you uncomfortable. When you do, you quickly assure him he didn't, not at all, and somehow ask him out on a date in your flustered rant.")
        print=("He slowly smiles again, and tells you when he's free. Together you arrange a date - tomorrow - and meeting place- right here, actually- and exchange numbers. You're waving goodbye much sooner than you'd like, but the thought of seeing him again tomorrow makes it worth it.")
        print=("You think of him as you sip your chai on the way home.")

    elif them== "girl":
        print=("...They're the most beautiful girl you've ever seen.")
        print=("You try not to be That Creepy Customer but you can't stop staring. Eventually she wraps up the order and turns to face you, catching you off guard. You're next in line and haven't even picked a drink!")
        print=("She doesn't notice your staring and instead smiles brightly at you, cheerily saying 'Welcome to Jimmy's Java! What would you like today?'")
        print=("You haven't even glanced at the menu yet, so you say the first thing that comes to mind. 'I actually don't know... I just want something sweet and cold. What would you recommend?'")
        print=("The barista grins again, and lists a few things on the menu. When she's done, she says 'My personal favorite is the vanilla frappuccino, though. So, which do you want?' and awaits your response.")
        print=("You decide you trust her judgement and order an iced chai. You don't admit to yourself that maybe it's because you want to impress her, or maybe make her like you...? Argh.")
        print=("Turns out it worked though. As she passes you your cup, she whispers that he's glad you listened to him. Most people make fun of him for liking chai's, stating that they're 'childish,' and she's relieved you didn't. She thinks you're quite cute- it'd suck if you turned out to be rude!")
        print=("You're shocked by her direct admission of her attraction to you, and barely register her face falling as she apologizes for making you uncomfortable. When you do, you quickly assure her she didn't, not at all, and somehow ask her out on a date in your flustered rant.")
        print=("She slowly smiles again, and tells you when she's free. Together you arrange a date - tomorrow - and meeting place- right here, actually- and exchange numbers. You're waving goodbye much sooner than you'd like, but the thought of seeing her again tomorrow makes it worth it.")
        print=("You think of her as you sip your chai on the way home.")

elif input == "left":
    print=("You decide to go left. You walk far, no longer recognizing any faces at all as you leave your neighborhood, but nonetheless feeling content.")
    print=("As you turn to watch a fluffy dog walk by, you fail to notice someone standing right in front of you, and you walk right into them! You apologize profuseley, but find your words dying on your lips when they finally turn to face you. Theyre...")
    print=("(What are they? (boy or girl?))")
    them= input()

    if them == "boy":
            print=("...They're the most beautiful boy you've ever seen. And you just rammed into him! Argh!")
            print=("You're mortified and resume mumbling apologies, but he waves it off and laughs, saying it was partly his fault too- he saw you coming, but he was too distracted to move out of the way.")
            print=("'I was too busy watching you stare at that dog thinking 'Wow, that's so cute' to move!' and then he laughs again. 'Speakign of which...can I take you out on a date sometime? I'm free tomorrow!'")
            print=("You're stunned for a moment, but you quickly agree, nodding your head furiously. He smiles at you and you exchange numbers, agreeing to meet here again the next day.")
            print=("You're waving goodbye much sooner than you'd like (he's got to run), but the thought of seeing him again tomorrow makes it worth it.")
            print=("You continue on your walk, thinking of him all the while...")

    if them == "girl":
            print=("...They're the most beautiful girl you've ever seen. And you just rammed into her! Argh!")
            print=("You're mortified and resume mumbling apologies, but she waves it off and laughs, saying it was partly her fault too- she saw you coming, but she was too distracted to move out of the way.")
            print=("'I was too busy watching you stare at that dog thinking 'Wow, that's so cute' to move!' and then she laughs again. 'Speakign of which...can I take you out on a date sometime? I'm free tomorrow!'")
            print=("You're stunned for a moment, but you quickly agree, nodding your head furiously. She smiles at you and you exchange numbers, agreeing to meet here again the next day.")
            print=("You're waving goodbye much sooner than you'd like (she's got to run), but the thought of seeing her again tomorrow makes it worth it.")
            print=("You continue on your walk, thinking of her all the while...")

print=("""You were barely able to sleep that night in your excitement. You picked an outfit MUCH earlier than necessary, triple-checked the location and time, and lay in bed for quite some time trying not to melt before finally falling asleep. Now, it’s morning- time to get ready for your date! Though, it’s not for a few hours.""")

if direction == "right":

    print=("""You head to the right again. You walk past places that are starting to look familiar with a goofy grin and a skip in your step, and you’re practically vibrating when you make it to the Cafe.""")

    if you == them:
	       print=("""You notice a rectangular rainbow sticker in the window and a flag you hadn’t seen before. You must have missed them on your first visit, but now they give you a sense of comfort. You’ll be safe here.""")

    print=("""You’re a little early so you decide to order and find a table. You order two of your date’s favorite (which is now also your favorite) from the barista -the same one that was working with your date yesterday. She gives you a knowing smile before passing you the cups.""")

    print=("""You don’t have to wait long; the ice has barely melted when your date swings open the door and spots you, excitedly making their way over to meet you.""")

    print=("""You spend your date enthusiastically listening to stories about friends, family, interests and the like, interjecting every now and then to contribute little pieces of your own, by which your date is fully enraptured.""")

    print=("""There’s never an awkward silence; whenever you don’t know what to say they ask about you, and whenever you can’t answer the two of you simply laugh and move on. It’s all too soon when you have to say goodbye again, although not without promising to text and meet up again as soon as possible.""")

    if you == them:
	       print=("""You didn’t hold hands for the short part of the way home where you were headed in the same direction, for safety, but they had given your hand a squeeze before turning down an avenue, and you can still feel it.""")

    print=("""After a bit of walking alone, you note that you feel lighter than air. You haven’t felt this giddy in quite some time! More than anything though, you’re incredibly glad that you went for a walk yesterday.""")

# to the LEFT to the LEFT

elif direction == "left":
    print=("You head to the left again. You walk past places that are starting to look familiar with a goofy grin and a skip in your step, and you’re practically vibrating when you make it to the meeting place.")

    print=("You're a little early so you decide to find some shade under an awning while you wait, though it's not long-barely five minutes have passed before you spot them walking down the sidewalk with a goofy grin to match your own. They haven't even noticed you yet!")

    print=("When they do, their grin gets impossibly wider. You feel your own smile stretch to match without your even intending it. What a pair!")

    print=("After greeting each other, you take one another's hands and start down the block towards a bookstore they swear is even homier than their workplace (which is hard to believe).")

if you == them:
    if you == "girl":

        print=("About halfway down the block, you pass by a man and he wolf whistles at the two of you. You try to ignore it and walk on, turning to see her reassuring smile, but just a short while later you start noticing men leering and women giving exaggeratedly disapproving looks before turning away.")

        print=("She whispers to you to ignore them, and you try, but you hear a parent telling their child not to look, hear a man yell what he'd like to do to the two of you as you pass, and it's not long before you're shaking- no longer with excitement, but with fear and anxiety.")

        print=("She lets go of your hand and your heart drops from guilt that you're a little relieved that now, perhaps, the comments might stop, but mostly from the loss of contact, for letting those awful people win. You don't have to agonize for long- she only let go of your hand to wrap her arm around your shoulder to hug you close.")

        print=("It's much less subtle than the hand holding, much more likely to draw attention, and a little awkward with your different heights, but she's warm and comforting and you feel... safer. She begins talking to distract you from the people around you, and you're more than happy to just listen to the sound of her voice.")

        print=("Finally, the bookstore appears on the horizon. You let out a sigh of relief at being out of the public eye, but you don't relax- not fully.")

        print=("You want to be fully in the moment but you're still a little shaken. She tries her best to appear aloof as well, though you can see the stress on her face.")

        print=("The two of you explore the bookstore, which is indeed just as homey as Jimmy's Java, somehow, and eventually settle down in an aisle with an armful of books. You read side by side, occasionally turning to point out funny lines in your books and discuss how you feel about them, and slowly the tension melts away.")

        print=("After a while, you're no longer thinking about the walk here. You're comfortable, the books you've picked up seem to be promising, and she snorts beside you as she reads and you feel your heart skip a beat. Everything's fine- better than fine. You're happy.")

        print=("The two of you walk out of the bookstore with matching bags full of books and your arms linked, heading towards your apartment since it's closest. You don't bother glancing at the people around you- you don't need care anymore. You hear unsavory things and glimpse hatred out of the corner of your eye, but...")

        print=("It's not your problem. This isn't about Them. It's about Her.")

        print=("When you finally reach your apartment building, as you stand on the steps, she looks away shyly for a moment before leaning in and kissing you on the cheek. Your heart speeds up and you just KNOW your face is red as an apple...")

        print=("She bids you goodbye and you wave back silently, unable to speak. You feel lighter than air and you're ecstatic. You haven’t felt this giddy in quite some time... More than anything though, in spite of everything, you’re incredibly glad that you went for a walk yesterday.")

    elif you == "boy":

        print=("About halfway down the block, you pass by a man and he yells 'FAGS!' at two of you. You try to ignore it and walk on, turning to see your date's reassuring smile, but just a short while later you start noticing more men leering and muttering and women giving exaggeratedly disapproving looks before turning away.")

        print=("He whispers to you to ignore them, and you try, but you hear a parent telling their child not to look, hear a man yell about your 'sinfulness and filth', and it's not long before you're shaking- no longer with excitement, but with fear and anxiety.")

        print=("He lets go of your hand and your heart drops from guilt that you're a little relieved that now, perhaps, the comments might stop, but mostly from the loss of contact, for letting those awful people win. You don't have to agonize for long- he only let go of your hand to wrap his arm around your shoulder to hug you close.")

        print=("It's much less subtle than the hand holding, much more likely to draw attention, and a little awkward with your different heights, but he's warm and comforting and you feel... safer. He begins talking to distract you from the people around you, and you're more than happy to just listen to the sound of his voice.")

        print=("Finally, the bookstore appears on the horizon. You let out a sigh of relief at being out of the public eye, but you don't relax- not fully.")

        print=("You want to be fully in the moment but you're still a little shaken. He tries his best to appear aloof as well, though you can see the stress on his face.")

        print=("The two of you explore the bookstore, which is indeed just as homey as Jimmy's Java, somehow, and eventually settle down in an aisle with an armful of books. You read side by side, occasionally turning to point out funny lines in your books and discuss how you feel about them, and slowly the tension melts away.")

        print=("After a while, you're no longer thinking about the walk here. You're comfortable, the books you've picked up seem to be promising, and he snorts beside you as he reads and you feel your heart skip a beat. Everything's fine- better than fine. You're happy.")

        print=("The two of you walk out of the bookstore with matching bags full of books and your arms linked, heading towards your apartment since it's closest. You don't bother glancing at the people around you- you don't need care anymore. You hear unsavory things and glimpse hatred out of the corner of your eye, but...")

        print=("It's not your problem. This isn't about Them. It's about Him.")

        print=("When you finally reach your apartment building, as you stand on the steps, he looks away shyly for a moment before leaning in and kissing you on the cheek. Your heart speeds up and you just KNOW your face is red as an apple...")

        print=("He bids you goodbye and you wave back silently, unable to speak. You feel lighter than air and you're ecstatic. You haven’t felt this giddy in quite some time... More than anything though, in spite of everything, you’re incredibly glad that you went for a walk yesterday.")

elif you != them:
    if them == "boy":
        print=("The bookstore appears on the horizon and you feel excited. You wonder if you'll find any good reads today.")

        print=("The two of you explore the bookstore, which is indeed just as homey as Jimmy's Java, somehow, and eventually settle down in an aisle with an armful of books. You read side by side, occasionally turning to point out funny lines in your books and discuss how you feel about them.")

        print=("After a while, you find that you're comfortable. The books you've picked up seem to be promising, and he snorts beside you as she reads and you feel your heart skip a beat. Everything's fine- better than fine. You're happy.")

        print=("The two of you walk out of the bookstore with matching bags full of books and your arms linked, heading toward your apartment since it's closest.")

        print=("When you finally reach your apartment building, as you stand on the steps, he looks away shyly for a moment before leaning in and kissing you on the cheek. Your heart speeds up and you just KNOW your face is red as an apple...")

        print=("He bids you goodbye and you wave back silently, unable to speak. You feel lighter than air and you're ecstatic. You haven’t felt this giddy in quite some time... More than anything though, you’re incredibly glad that you went for a walk yesterday.")

    elif them == "girl":

        print=("The bookstore appears on the horizon and you feel excited. You wonder if you'll find any good reads today.")

        print=("The two of you explore the bookstore, which is indeed just as homey as Jimmy's Java, somehow, and eventually settle down in an aisle with an armful of books. You read side by side, occasionally turning to point out funny lines in your books and discuss how you feel about them.")

        print=("After a while, you find that you're comfortable. The books you've picked up seem to be promising, and she snorts beside you as she reads and you feel your heart skip a beat. Everything's fine- better than fine. You're happy.")

        print=("The two of you walk out of the bookstore with matching bags full of books and your arms linked, heading toward your apartment since it's closest.")

        print=("When you finally reach your apartment building, as you stand on the steps, she looks away shyly for a moment before leaning in and kissing you on the cheek. Your heart speeds up and you just KNOW your face is red as an apple...")

        print=("She bids you goodbye and you wave back silently, unable to speak. You feel lighter than air and you're ecstatic. You haven’t felt this giddy in quite some time... More than anything though, you’re incredibly glad that you went for a walk yesterday.")

print=("You've completed one ending of 'Them'! I encourage you to replay the game, and try different combinations. There are a total of 6 different experiences- try to play them all! Click to Exit and start again :)")

exitonclick()
