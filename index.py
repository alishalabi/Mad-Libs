nouns = list()
adjectives = list()
verbs = list()

wordCount = 1

introduction = "Hello - welome to a game of Mad Libs! In this game, you will input a series of nouns, verbs, and adjectives - and the game will create a customized, hilarious short story for you."

def user_input(prompt):
    user_input = input(prompt)
    return user_input

def add_noun(noun):
    nouns.append(noun)

def add_adjective(adjective):
    adjectives.append(adjective)

def add_verb(verb):
    verbs.append(verb)

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


# def print_story():
#
#
# def run_program():
#     print(introduction)
#
#
#
# nounOne = user_input("First, give us a common noun")
# verbOne = user_input("Next, give us an action verb")
# adjectiveOne = user_input("Finally, give us an adjective")

# def user_input(prompt):
#     user_input = input(prompt)
#     return user_input

def test():
    get_nouns()
    get_adjectives()
    get_verbs()

    print(nouns)
    print(adjectives)
    print(verbs)

test()
