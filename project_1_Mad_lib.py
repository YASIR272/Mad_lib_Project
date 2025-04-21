# Mad Libs Generator

print("Let's play Mad Libs!\n")

# Getting user inputs
noun1 = input("Enter a noun: ")
verb1 = input("Enter a verb (past tense): ")
adjective1 = input("Enter an adjective: ")
place1 = input("Enter a place: ")
noun2 = input("Enter another noun: ")
adverb1 = input("Enter an adverb: ")

# Story template
story = f"""
One day, a {adjective1} {noun1} was walking through {place1}.
Suddenly, it {verb1} right into a {noun2}!
It looked around {adverb1} and decided to run away.
The end.
"""

# Print the final story
print("\nHere's your Mad Libs story!")
print(story)
