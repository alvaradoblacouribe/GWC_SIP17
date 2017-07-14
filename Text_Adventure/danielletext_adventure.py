start= '''
Oh NOOOOOoOOOOOOoO a huge iceberg just broke off from the Arctic, so big that mapmakers claim that the world map has to be redrawn! What do you do?'''

print (start)

print("Type 'whatever' to ignore the problem or type 'let's do something' to take action'")
user_input= input()

if user_input== "whatever":
    print("What the heck! Why? Choose either: This issue does not affect me, global warming is a Chinese hoax, or else by typing any of them below")
    user_input1= input()
    if user_input1 == "This issue does not affect me" or "this issue does not affect me'":
            print("Hmmm you only think that. Check out this article: https://medium.com/natural-resources-defense-council/climate-change-is-our-problem-we-can-solve-it-2aaf1ded1905 for compelling evidence as to why global warming is a problem for all Americans")
    elif user_input1 == "Global warming is a Chinese hoax" or "global warming is a Chinese hoax"or "Global warming is a chinese hoax"or "global warming is a chinese hoax":
            print("Hmmmm you only think that. Check out this article: https://www.washingtonpost.com/news/morning-mix/wp/2016/11/17/china-tells-trump-climate-change-is-not-a-chinese-hoax/?utm_term=.7b581d88f433 for compelling evidence as to why global warming is not a Chinese hoax")
    elif user_input1 == "else" or "Else" or "Other"or "other":
            print("Okay well please read this article to explore other opinions and facts regarding global warming: https://climate.nasa.gov/evidence/ ")


elif user_input == "let's do something":
    print("Great! Global warming is a serious issue which many politicians and people ignore, how should this issue be addressed?")
    print("Choose internet petition, letters to the senator, or organizing a demonstration by typing either option below")
    user_input2= input()
    if user_input2=="internet petition" or "Internet petition" or "petition"or "Petition":
            print("Cool! Here is how you can take online action: https://support.nature.org/site/SPageNavigator/action_center/action_center.html")
    elif user_input2=="letters" or "Letters" or "Letters to senators" or "letters to senators":
            print("Awesome! Here is a link to the contact information of all the Senators of the 50 states: https://www.senate.gov/senators/contact/ feel free to use this information to write a letter to your senator about the current state of global warming")
    elif user_input2=="demonstration"or "Demonstration" or "a demonstration" or "A demonstration":
            print("Cool! it is really hard to keep track of active movements so make sure to keep your eye out for any protests or rallies in your area. While waiting for that, enjoy this video of Bill Nye: http://www.smithsonianmag.com/videos/category/3play_1/climate-change-101-with-bill-nye-the-science/")
