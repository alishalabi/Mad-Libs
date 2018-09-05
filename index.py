nouns = list()
adjectives = list()
verbs = list()

wholeStory = ""


wordCount = 1

initial = "Hello - welome to a game of Mad Libs. Here, you will input a series of nouns, verbs, and adjectives - and the game will create a customized, hilarious story - just for you!"

# Variable story lengths will be made available in V2.
introductionPromt = "To begin with, would you prefer to hear a short-lengthed tale (enter: S), a medium lengthed tale (enter: M), or a long-lenghted tale (L)"

def user_input(prompt):
    user_input = input(prompt)
    return user_input

def add_noun(noun):
    nouns.append(noun)

def add_adjective(adjective):
    adjectives.append(adjective)

def add_verb(verb):
    verbs.append(verb)

# # Variable story lengths will be made available in V2.
# def get_story(length):
#     if length == "S":
#         wordCount = 0
#         print("You have selected a short-lengthed story")
#
#     elif length == "M":
#         wordCount = 1
#         print("You have selected a medium-lengthed story")
#
#     elif length == "L":
#         wordCount = 2
#         print("You have selected a long-lengthed story")
#
#     else:
#         print("Error, you have selected an unknown value. We will set your story length to default")
# #End story length section


def get_nouns():
    index = 0
    while index <= int(wordCount):
        if index == 0:
            input_item = user_input("Please enter first noun:")
            add_noun(input_item)
            index += 1
        else:
            input_item = user_input("Please enter another noun:")
            add_noun(input_item)
            index += 1

def get_adjectives():
    index = 0
    while index <= int(wordCount):
        if index == 0:
            input_item = user_input("Please enter first adjective:")
            add_adjective(input_item)
            index += 1
        else:
            input_item = user_input("Please enter another adjective:")
            add_adjective(input_item)
            index += 1


def get_verbs():
    index = 0
    while index <= int(wordCount):
        if index == 0:
            input_item = user_input("Please enter first verb:")
            add_verb(input_item)
            index += 1
        else:
            input_item = user_input("Please enter another verb:")
            add_verb(input_item)
            index += 1

#Beginning of hard-coded story find and replace, as well as concatenation into empty string
def hard_code_story():
    global wholeStory

    nounSentenceOne = "One upon a time, in a faraway land, there lived a young " + str(nouns[0]) + " hero. "
    verbSentenceOne = "And then one day, while walking in a bright meddow, they sighted a snarling ghoul, getting ready to " + str(verbs[0]) + " . "
    adjectiveSentenceOne = "Pulling out their " + str(adjectives[0]) + " wand, the time for magical battle had come. "
    verbSentenceTwo = "The ghoul put up a mighty fight, but was eventually defeated - only to run home and " + str(verbs[1]) + " his wounds. "
    adjectiveSentenceTwo = "Feeling jubilant, the hero went home and drank lemonade until they felt " + str(adjectives[1]) + " . "
    nounSentenceTwo = "Cheering his success, the townspeople gave him showers of " + str(nouns[1]) + " for the rest of his days. "
    theEnd = "The End."

    nounSentenceOne.replace("(test_noun)", nouns[0])
    wholeStory = wholeStory + nounSentenceOne

    verbSentenceOne.replace("(test_verb)", verbs[0])
    wholeStory = wholeStory + verbSentenceOne

    adjectiveSentenceOne.replace("(test_adjective)", adjectives[0])
    wholeStory = wholeStory + verbSentenceOne

    verbSentenceTwo.replace("(test_verb)", verbs[1])
    wholeStory = wholeStory + verbSentenceTwo

    adjectiveSentenceTwo.replace("(test_adjective)", adjectives[1])
    wholeStory = wholeStory + adjectiveSentenceTwo

    nounSentenceTwo.replace("(test_noun)", nouns[1])
    wholeStory = wholeStory + nounSentenceTwo

    wholeStory = wholeStory + theEnd
# End of hardcode section

def test():
    get_nouns()
    get_adjectives()
    get_verbs()

    hard_code_story()
    print(wholeStory)

test()
