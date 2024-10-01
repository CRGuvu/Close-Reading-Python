### Print a welcome message
print("Welcome to Danielstown")
print("You are the sole member of a Anglo-Irish family.") 
print("Your father who owed this estate has died.")
print("We are leaving this estate to you, Try to navagate Danielstone.")
print("The Montmoranys arive, They are saddend to hear of your fathers passing.")
print("To lighten the mood they invite you to a extravagant part later today.")
print("Do you attend the event, or politely decline?")

### Prompt user for a choice
convoChoice = input("> ")

if(convoChoice == "attend"):
  print("You attend the party. You see many familes and a few officers")
  print("As you walk in, one of the officers approaches you")
  print("He wishes to dicuss the IRA and political events around Danielstown")
  Print("Would you like to continue the discussion with him?")

  officerChoice = input("> ")

  if(officerChoice == "no"):
    print("You quietly disengage the conversation.")
    print("Better to ignore it.")
  elif(officerChoice == "yes"):
    print("You dicuss the activiy with great concern.")
    print("From this you learn there has been more IRA activiy of recent.")
    print("You ponder on the information you have learned and go back home")
  else:
    print("Invalid choice. Please enter yes or no.")
elif(convoChoice == "decline"):
  print("You are far to tired to thnk about such an event.")
  print("You settle into bed. And fall asleep")
  print("The IRA invades your house in the middle of the night")
  Print("You never wake up, your family line ends that night")

### Next day
print("It's the next day")



  
  nextdayChoice = input("> "):

  if(nextdayChoice == "yes"):
    print("You open the vase and find a pile of bones!")
  elif(vaseChoice == "no"):
    print("You decide not to open the shiny vase.")
    print("As you turn to leave, you hear a cracking sound coming from the corner.")
    print("A dark figure with glowing red eyes launches at you, knocking you unconcious")
    print("You wake up in your bed. It was all a dream.")
  else:
    print("Invalid choice. Please enter yes or no.")
else:
  print("Invalid choice. Please enter attend or decline.")
