"""Mad-lib program that prompts a noun, verb,an adverb,and an adjective and inject those into a story
that you create
"""
noun = input("Enter a noun: ")
verb = input("Enter a verb: ")
adjective = input("Enter an adjective: ")
adverb = input("Enter an adverb: ")
story = "Does " + noun + verb + adjective + " food " + adverb + "?"
print(story)