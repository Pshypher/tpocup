# Program designed to simulate a game of Madlibs
# Create a story
# Prompt the user for strings to replace the various parts of speech specified
# in the story
# Print the revised story

story = \
"Radio Announcer: Thank you for tuning in today. We are here in CITY \
to celebrate \nNational Poetry Month. In just a moment, the nation's poet\
laureate, FAMOUS_PERSON, will read\n \
a poem about a(n) SINGULAR_NOUN_ONE. And here is FAMOUS_PERSON.\n\n \
FAMOUS_PERSON: Thank you, everyone. This is a very ADJECTIVE_ZERO poem\n \
I wrote about a(n) SINGULAR_NOUN_ONE.\n\n \
An Ode to a(n) SINGULAR_NOUN_ONE\n\n \
The SINGULAR_NOUN_ONE is as big as a(n) SINGULAR_NOUN_TWO.\n \
It reminds me of small PLURAL_NOUN VERB_ING_SUFFIX_ONE.\n \
O, the SINGULAR_NOUN_ONE. O, the SINGULAR_NOUN_ONE!\n \
What do ADJECTIVE_ONE people think when they see you for the first time?\n \
Perhaps they know there are happy days ahead.\n \
O, the SINGULAR_NOUN_ONE. O, the SINGULAR_NOUN_ONE!\n \
For some, you are ADJECTIVE_TWO, but for others, you are ADJECTIVE_THREE.\n \
If we are VERB_ING_SUFFIX_TWO, we pause when we think of you.\n \
May you always PRE_TENSE_VERB.\n \
O, the SINGULAR_NOUN_ONE. O, SINGULAR_NOUN_ONE!\n \
The end.\n\n \
Radio Announcer: On behalf of the poets, thank you for VERB_ING_SUFFIX_3."

city = input("City or Town: ")
famous_person = input("Famous Person: ")
singular_noun_one = input("Singular Noun: ")
adjective = input("Adjective: ")
singular_noun_two = input("Singular Noun: ")
plural_noun = input("Plural Noun: ")
verb_ing_suffix_one = input("Verb ending with \"ing\": ")
adjective_one = input("Adjective: ")
adjective_two = input("Adjective: ")
adjective_three = input("Adjective: ")
verb_ing_suffix_two = input("Verb ending with \"ing\": ")
pre_tense_verb = input("Present Tense Verb: ")
verb_ing_suffix_three = input("Verb ending with \"ing\": ")

story = story.replace("CITY", city)                                 # Dakar
story = story.replace("FAMOUS_PERSON", famous_person)               # Maya Angelou
story = story.replace("SINGULAR_NOUN_ONE", singular_noun_one)       # Raccoon
story = story.replace("ADJECTIVE_ZERO", adjective)                  # interesting
story = story.replace("SINGULAR_NOUN_TWO", singular_noun_two)       # fox
story = story.replace("PLURAL_NOUN", plural_noun)                   # men
story = story.replace("VERB_ING_SUFFIX_ONE", verb_ing_suffix_one)   # running
story = story.replace("ADJECTIVE_ONE", adjective_one)               # light
story = story.replace("ADJECTIVE_TWO", adjective_two)               # grand
story = story.replace("ADJECTIVE_THREE", adjective_three)           # slippery
story = story.replace("VERB_ING_SUFFIX_TWO", verb_ing_suffix_two)   # eating
story = story.replace("PRE_TENSE_VERB", pre_tense_verb)             # see
story = story.replace("VERB_ING_SUFFIX_3", verb_ing_suffix_three)   # listening

print()
print(story)




