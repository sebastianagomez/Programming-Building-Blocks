print()

print("Hi! We'll play a game today. You will create a story!")
print("You will see the magic...")

print()

print("Please enter the following:")

# First part of the story

adjective = input("\nEnter an Adjective: ")
animal = input("Enter an Animal: ")
verb = input("Enter a Verb: ")
exclamation = input("Enter an Exclamation: ")
verb2 = input("Enter a Verb: ")
verb3 = input("Enter a Verb: ")

# Second part of the story

holiday = input("Enter a Holiday: ")
noun = input("Enter a Noun: ")
place = input("Enter a Place: ")
superHero = input("Enter a Super Hero: ")
adjective2 = input("Enter a Adjective: ")
bodyP = input("Enter a Body Part(plural): ")
verb4 = input("Enter a Verb: ")
adjective3 = input("Enter a Adjective: ")
noun2 = input("Enter a Noun: ")
food = input("Enter a Food: ")
pluNoun = input("Enter a Plural Noun: ")

print()

print("Your story is:")

print()

print("The other day, I was really in trouble. It all started when I saw a very\n" + f'{adjective.lower()} {animal.lower()} {verb.lower()}'+ " down the hallway. " + f'"{exclamation.capitalize()}"! ' + "I yelled. But all\nI could think to do was to " + verb2.lower() + " over and over. Miraculously,\nthat caused it to stop, but not before it tried to " + verb3.lower() + "\nright in front of my family.\n")

print("I can't believe it's already " + f'{holiday.lower()}! ' + "I can't wait to\nput on my " + f'{noun.lower()} ' + "and visit every " + f'{place.lower()} ' + "in my\nneighborhood. This year, I am going to dress up as (a)\n" + f'{superHero.capitalize()} ' + "with " + f'{adjective2.lower()} {bodyP.lower()}.' + " Before I " + f'{verb4.lower()},\n' + "I make sure to grab my " + f'{adjective3.lower()} {noun2.lower()} ' + "to hold all of\nmy " + f'{food.lower()}.' + " Finally, all of my " + f'{pluNoun.lower()} ' + "are ready to go!\n")

print("Nice story!")

