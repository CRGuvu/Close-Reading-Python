### Print a welcome message
print("Welcome to Danielstown.")
print("You are member of a Anglo-Irish aristocartic family.") 
print("Your father who has died, left you the estate.")
print("Now being the sole member of your family, Try to navagate Danielstown.")


print("Your family friends the Naylors have stopped by your estate. ") 
print("They are saddend to hear of your fathers passing.")
print("To lighten the mood they invite you to a extravagant part later today.")
print("Do you attend the event, or politely decline? ")

### Prompt user for a choice
convoChoice = input("> ")

if(convoChoice == "attend"):
  print("You attend the party. You see many familes and a few officers.")
  print("As you walk in, one of the officers approaches you.")
  print("He wishes to dicuss the IRA and political events around Danielstown.")
  Print("Would you like to continue the discussion with him?")

  officerChoice = input("> ")

  if(officerChoice == "no"):
    print("You quietly disengage the conversation. ")
    print("Better to ignore it. ")
  elif(officerChoice == "yes"):
    print("You dicuss the activiy with great concern. ")
    print("From this you learn there has been more IRA activiy of recent. ")
    print("You ponder on the information you have learned and go back home. ")
  else:
    print("Invalid choice. Please enter yes or no.")
elif(convoChoice == "decline"):
  print("You are far to tired to thnk about such an event. ")
  print("You settle into bed. And fall asleep. ")
  print("As soon as the sun falls down the IRA break into your estate. ")
  Print("You never wake up, your family line ends that night. ")
else:
  print("Invalid choice. Please enter attend or decline. ")
### Next day
nextdayChoice = input("> "):
print("It's the next day. ")
print("You decide to take a walk downtown. ")
print("You pass by two men wispering in a corner. ")
print("Do you listen to them or continue walking?. ")

  if(nextdayChoice == "listen"):
    print("What was that? Something about guns in a plantation? ")
    print ("Ridiculous.")
    print ("With slight regard you continue on. ")
  elif(nextdayChoice == "contine"):
    print("You decide you rather not know what these men are whispering about. ")
    print("You continue on. ")
  else:
    print("Invalid choice. Please enter listen or continue. ")

storeChoice = input(">")
print("As you contine you .")
print("You stop inside a bakery. ")
print("Along the shelf are line with varying products, you see a one that catches your eye. ")
Print("A delicately crafed choclate cake, larger than anyone should need. ")
Print("You can tell that hours if not days went into the icing and design")
Print("Do you buy it or leave?")
  if(storeChoice == "buy"):
    print("You are in awe of it's beauty. ")
    print ("It's a shame something as grand your cake can't last forever.")
    print ("Even more unfortunate you drop it on the way back to your estate. ")
  elif(storeChoice == "leave"):
    print("While certianly beautiful you decide not to buy the cake.")
    print("Besides what use would you have for it?.")
    print("You decide to head back to your estate")
  else:
    print("Invalid choice. Please enter buy or leave.")








