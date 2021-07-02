run = "run"
lieDown = "lie down"
rock = "rock"

hide = "hide"
trapped = "trapped"

yes = "yes"
no = "no"

required = "\n\nPlease enter again you answer\n\n"

print()

def intro():
    print("You don't remember anything about what happened the day before, but you wake \nup in a dark forest "
    "with no cell phone and no other way of communicating with someone. You \nare scared and you don't "
    "know why you are there. Desperately walking everywhere, you hear footsteps. \nYou notice that there is a "
    "huge bear looking at you and it starts running towards you. \nWhat do you do, RUN, LIE DOWN and wait to "
    "be mutilated or grab a nearby ROCK and throw it at the bear?\n")

    print("Run? \n"
          "Lie down? \n"
          "Rock? \n")

    choice = input(">>> ")
    if choice == run.lower():
        option_run()
    elif choice == lieDown.lower():
        option_lieDown()
    elif choice == rock.lower():
        option_rock()
    else:
        print(required)
        intro()

def option_run():
    print("\nYou run as quickly as possible, but the bear's speed is too great. You will: HIDE behind boulder, TRAPPED, "
    "so you fight or RUN towards an abandoned town.\n")

    print("Hide? \n"
          "Trapped? \n"
          "Run? \n")

    choice = input(">>> ")
    if choice == hide.lower():
        print("\nYou're easily spotted.\n\n"
              "You died!")
    elif choice == trapped.lower():
        print("\nYou're no match for an bear.\n\n"
              "You died!")
    elif choice == run.lower():
        option_run2()
    else:
        print(required)
        option_run()

def option_run2():
    print("\nWhile frantically running, you notice a rusted sword lying in the mud. \nYou quickly reach down and grab "
    "it, but miss. You try to calm your heavy breathing as you hide behind a delapitated \nbuilding, waiting for "
    "the orc to come charging around the corner. You notice a purple flower near your foot. \nDo you pick it "
    "up? YES/NO\n")

    print("Yes? \n"
          "No? \n")

    choice = input(">>> ")
    if choice == yes.lower():
        print("\nYou hear its heavy footsteps and ready yourself for the impending bear.\n\n"
              "You quickly hold out the purple flower, somehow hoping \nit will stop the bear. It does! The bear was looking for love.\n\n"
              "This got weird, but you survived!")
    elif choice == no.lower():
        print("\nYou hear its heavy footsteps and ready yourself for the impending bear.\n\n"
              "Maybe you should have picked up the flower.\n\n"
              "You died!")
    else:
        print(required)
        option_run2()

def option_lieDown():
    print("\nWelp, that was quick.\n\n"
          "You died!")

# Terminar esta ultima parte

def option_rock():
    print("\nThe is stunned, but regains control. He begins running towards you again. Will you: \nRUN, throw another"
          "ROCK or ENTER towards the nearby cave.\n")

intro()



