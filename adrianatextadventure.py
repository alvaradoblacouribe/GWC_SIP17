print(
"Your alarm goes off at 6:00 a.m.It's raining heavily outside and you have pain in your")

print("back that feels like metal rods being jammed into your spine. It's your first day at")
print("your new job and you don't want to be late.")

#FUNCTIONS
def morning():
    print("Your stomach is growling but oddly the the thought of food makes you sick")
    eatorskip= input("Type 'Eat' to eat a bowl of cereal or 'Skip' if you want to skip breakfast")


#MAIN CODE
print("Type 'Get Up' to start your day or 'Snooze' to go back to sleep for thirty minutes")
WakeorSnooze = input()

if WakeorSnooze == "Get Up":
    print("You decide to get an early start for the day.")
    morning()
    if eatorskip=="Eat":
        print("Because you got up so early you have enough time to sit down and breakfast")
        print("even though your stomach feels so unsettled this early in the morning")
        print("You look down at the milk in your cereal, and it was expired!!")
        print("You feel a nasty gurgling in your stomach and run to the toiled")
        print("You call in your boss sick on your first day with food poisining :(")
        print("GAME OVER.")

elif eatorskip=="Skip":
   print("You're not hungry yet anyways, so you decide to leave without breakfast")
   print("With all the time on your hands, you catch the early bus")
   print("and show up nice and early to your first day")
   print("on the job.")
   print("Congratulations! Your day met your hopes, but did not exceed them")
   print("GAME OVER.")

else:
 print("Please enter a valid response")

elif user_input == "Snooze":
      print("Uh oh! You don't hear your second alarm and end up waking up late!")
      print("You pull off your covers and quickly get dressed")
      morning()
        if eatorskip=="Eat":
         print("You decide to eat breakfast even though you are already running late ")
         print("and your stomach feels unsettled this early in the morning")
         print("You look down at the carton of milk you put in your cereal, and see it is expired!!")
         print("You feel a nasty gurgling in your stomach and run to the toiled")
         print("You call in your boss sick on your first day with food poisining :(")
         print("GAME OVER.")

        else if eatorskip=="Skip":
          print("You're not hungry yet anyways, so you decide to leave without breakfast")
          print("Because you woke up late, you miss your bus")
          print("and are now officially late for your first day of work.")
          print("You're extremely angry with yourself and keep on wondering what")
          print("would have happened if you had woken up earlier!")
          print("While you're waiting for your next bus to arrive")
          print("You decide to grab breakfast for later")
          print("You spot a bagel place across the street from your bus stop and cross the street to enter")
          print("A small bell rings as you enter and you notice the long line of people waiting to order")
          print("You're worried that if you wait to order you're now going to miss your second bus")


        else:
          print("Please enter a valid response")


          StayorLeave=input("Do you leave the bagel store or stay?")
          if StayorLeave=="Leave":
              print("You decide to leave the bagel store and wait for the bus.")
              print("You catch the second bus and are only a little bit wait to work")
              print("Your new boss is mad at you. Congratulations, your day did not meet your expectations")
              print("GAME OVER!")

          elif StayorLeave=="STAY":
              print("You decide to wait in line at the bagel place. A handsome stranger")
              print("asks if he can go in front of you. There are only 2 minutes before")
              print("your bus will arrive at the station.")
              CutorNot=input("Do you let him go in front of you?")


          else:
            print("Please enter a valid response")


              if CutorNot=="Yes":
                  print("You let the man order in front of you but he see's that you look worried")
                  print("and asks what's wrong. After hearing how you're going to be late for your")
                  print("first day of work, he is so thankful for letting him order his breakfast first")
                  print("that he offers you his company car to take you to work.")
                  print("You hit it off in the car, and decide to grab coffee together later that week")
                  print("Congratulations, in 40 years you'll be telling your grandchildren the stoy of")
                  print("how you met your husband. Your first day of work did not meet your expectations,")
                  print("but exceeded them.")
                  print("GAME OVER!")

              elif CutorNot=="No":
                  print("You get your bagel just in time and arrive to work before your boss")
                  print("is completely mad with you. Congratulations, your first day at work")
                  print("somewhat met expectations but you have no idea where your day would have gone")
                  print("if the choices you made were a little bit different.")

            else:
                print("Please enter a valid response")
