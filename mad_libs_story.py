


#Nabukenya phiona's clever story describing how her family got into trouble .




def get_article(word):
    if word[0].lower() in 'aeiou':
        return 'an'
    else:
        return 'a'

print("Please enter the following:\n")

adjective = input("adjective: ")
animal = input("animal: ")
verb1 = input("verb: ")
exclamation = input("exclamation: ").capitalize()
verb2 = input("verb: ")
verb3 = input("verb: ")

place = input("place: ")
funny_noise = input("funny noise: ")

article = get_article(adjective)

print("\nYour story is:\n")
print(f"The other day, I was really in trouble. It all started when I saw {article} {adjective} {animal} {verb1} down the hallway. \"{exclamation}!\" I yelled. But all")
print(f"I could think to do was to {verb2} over and over. Miraculously,")
print(f"that caused it to stop, but not before it tried to {verb3}")
print("right in front of my family.")

print(f"\nWe ended up running all the way to {place}, where it made a loud \"{funny_noise}!\" and vanished into thin air.")
print("I'll never forget that strange day.")
