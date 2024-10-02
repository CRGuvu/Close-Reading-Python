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

  EstateChoice = input("> ")
    print("Back at your estate you settle into your chair. ")
    print ("You hear a loud knock on the door.")
    print ("Suprised you look at the door. You were not expecting any vistors ")
    Print("Do you open the door?.")
    
  if(EstateChoice == "yes"):
    if(officerChoice == "yes"):
      if(nextdayChoice == "listen"):
    print("You open the door to see armed men. ")
    print("You remember what the officer told you, and the what the two men had talked about ")
    print("These men are the IRA. ")
    print("They relize you know who they are.")
    print("Before you can talk, they break through your door. ")
    print ("Your estate is gone and so are you. ")
    Print("Ending One False connsciouness too self-aware.")

if(EstateChoice == "Yes"):
  if(officerChoice == "yes"):
    if(nextdayChoice == "continue"):
    print("You open the door to see armed men. ")
    print("You remember what the officer told you, could this be the IRA?. ")
    print("Doubful, they don't anyting like what he described. ")
    print("They ask if you wouldn't mind them cutting aross your plantation. It is quicker to get into town that way. ")
    print("You agree, and they go on thier way. You wonder a little why they are carrying so many guns? ")

if(EstateChoice == "Yes"):
   if(officerChoice == "no"):
     if(nextdayChoice == "listen"):
    print("You open the door to see armed men. ")
    print("You remember hearing those two men whisper. ")
    print("Doubful, they don't anyting like what he described ")
    print("They ask if you wouldn't mind them cutting aross your plantation. It is quicker to get into town that way. ")
    print("You agree, and they go on thier way. You wonder a little why they are carrying so many guns? ")

  elif(estateChoice == "no"):
    print("Ingoring the knocking you stay seated. ")
    print("Moments later your door is busted down. ")
    print("The IRA have invaded your estate. Your estate is gone and so are you. ")
  else:
    print("Invalid choice. Please enter yes or no.")

### following day
 Finalchoice = input("> ")

    print("The following day you awake to the sound of a warning bell. ")
    print("Frighted you run outside, ")
    print("Are you ready to see what awaits you?")
    
if(Finalchoice == "yes"):
if(storeChoice == "buy"):
if(officerChoice == "yes"):
if(nextdayChoice == "continue"):
    print("In the distance you see the same officer you, talked to approach you. ")
    print("He yells at you to follow him.")
    print ("You manage to escape your estate moments before the IRA arrives. ")
    print ("You no longer have your estate, but your mangaged to save yourself. ")
    print("End 3 bourqeoise wins")
    
elif(FinaleChoice == "yes"):
  if(officerChoice == "no"):
    if(nextdayChoice == "listen"):
      if(storeChoice == "buy"):
    print("You see an angry mob running toward your estate.")
    print("They appear to be heavliy armed. You relize this must be the IRA")
    print("The IRA have invaded your estate. Your estate is gone and so are you. ")
  
else:
    print("Invalid choice. It was a retorical question, you must select yes.")
