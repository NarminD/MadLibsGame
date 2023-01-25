MadLibStory = """And he {} back to meet the fox.
"Goodbye," {} said.
"Goodbye," said the {}. "And now here is my secret, a very simple secret: It is only with the heart that one can see rightly; what is {} is invisible to the eye."
"What is {} is invisible to the eye," the little {} {} so that he {} be sure to remember.
"It is the time you have {} for your {} that makes your {} so important." """

print(MadLibStory)
verb1 = input("Enter a verb: ")
noun1 = input("Enter a noun: ")
noun2 = input("Enter another noun: ")
adjective1 = input("Enter an adjective: ")
adjective2 = input("Enter another adjective: ")
noun3 = input("Enter a third noun: ")
verb2 = input("Enter another verb: ")
verb3 = input("Enter a third verb: ")
adjective3 = input("Enter a third adjective: ")
noun4 = input("Enter a fourth noun: ")
noun5 = input("Enter a fifth noun: ")

print("And he {} back to meet the fox.".format(verb1))
print("\"Goodbye,\" {} said.".format(noun1))
print("\"Goodbye,\" said the {}. \"And now here is my secret, a very simple secret: It is only with the heart that one can see rightly; what is {} is invisible to the eye.\"".format(noun2, adjective1))
print("\"What is {} is invisible to the eye,\" the little {} {} so that he {} be sure to remember.".format(adjective2, noun3, verb2, verb3))
print("\"It is the time you have {} for your {} that makes your {} so important.\"".format(adjective3, noun4, noun5))